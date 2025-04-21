import ctypes
import functools
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('kernel.log'),
                              logging.StreamHandler()])

ERROR_PROCESS_MANAGEMENT = "0xe1_kernel"
ERROR_MEMORY_EXHAUSTION = "0xe2_kernel"

class Process:
    def __init__(self, pid, name, memory_id, priority=0):
        self.pid = pid
        self.name = name
        self.memory_id = memory_id
        self.priority = priority

class MemoryManager:
    def __init__(self):
        self.allocated_memory = {}

    def allocate_memory(self, size):
        mem = ctypes.create_string_buffer(size)
        self.allocated_memory[id(mem)] = (mem, size)
        return id(mem)

    def deallocate_memory(self, mem_id):
        mem, size = self.allocated_memory.pop(mem_id, (None, None))
        if mem is not None:
            ctypes.cast(mem, ctypes.c_void_p).value = 0
            ctypes.pythonapi.PyMem_Free(mem)

class Kernel:
    def __init__(self):
        self.processes = []
        self.memory_manager = MemoryManager()
        self.next_pid = 1

    def process_exists(self, pid):
        for process in self.processes:
            if process.pid == pid:
                return True
        return False

    def create_process(self, name, priority=0, memory_size=1024):
        for process in self.processes:
            if process.pid == 0:
                logging.warning("Kernel process already exists. Cannot create another process with the same PID.")
                return
        if len(self.processes) >= 1000:
            logging.error("Memory exhaustion: Maximum number of processes reached.")
            self.kernel_panic("Memory exhaustion", ERROR_MEMORY_EXHAUSTION)
        pid = self.next_pid
        self.next_pid += 1
        process_memory_id = self.memory_manager.allocate_memory(memory_size)
        process = Process(pid, name, process_memory_id, priority)
        self.processes.append(process)
        logging.info(f"Process created - PID: {pid}, Name: {name}, Memory: {memory_size} bytes.")
        return pid

    def kill_process(self, pid):
        if pid == 0:
            logging.warning("Cannot kill the Kernel process.")
            return
        for i, process in enumerate(self.processes):
            if process.pid == pid:
                self.memory_manager.deallocate_memory(process.memory_id)
                del self.processes[i]
                logging.info(f"Process terminated - PID: {pid}, Name: {process.name}")
                return
        logging.warning(f"Process with PID {pid} not found.")

    def kernel_panic(self, message, error_code):
        logging.error(f"KERNEL PANIC: {message}, error Code: {error_code}, restarting the system may fix the issue.")
        exit()

kernel = Kernel()

def process_management(priority=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                pid = kernel.create_process(func.__name__, priority=priority)
                result = func(*args, **kwargs)
                kernel.kill_process(pid)
                return result
            except Exception as e:
                logging.error(f"Kernel error occured: {e}")
                kernel.kernel_panic("Process management error", ERROR_PROCESS_MANAGEMENT)
        return wrapper
    return decorator

def kernel_main():
    kernel = Kernel()
    while True:
        try:
            logging.debug("Kernel is running")
            time.sleep(1)
        except Exception as e:
            logging.error(f"Error in kernel main loop: {e}")


if __name__ == "__main__":
    kernel_main()
