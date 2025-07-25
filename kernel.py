import functools
import logging
import sys
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("system_kernel.log"),
        logging.StreamHandler()
    ]
)

KERNEL_ERRORS = {
    'PROCESS_FAIL': '0xF1',
    'MEMORY_OVERFLOW': '0xF2'
}

class Process:
    def __init__(self, name, memory_block, priority=1):
        self.name = name
        self.memory_block = memory_block
        self.priority = priority
        self.pid = id(self)

class Memory:
    def __init__(self):
        self.storage = {}

    def alloc(self, size):
        try:
            block = bytearray(size)
            self.storage[id(block)] = block
            return block
        except MemoryError:
            raise Exception("Memory allocation failed")

    def free(self, block):
        self.storage.pop(id(block), None)

class Kernel:
    def __init__(self, max_processes=1000):
        self.memory = Memory()
        self.process_list = []
        self.max_processes = max_processes

    def spawn(self, name, priority=1, mem_size=1024):
        if len(self.process_list) >= self.max_processes:
            self.panic("Process limit exceeded", KERNEL_ERRORS['MEMORY_OVERFLOW'])
        block = self.memory.alloc(mem_size)
        proc = Process(name, block, priority)
        self.process_list.append(proc)
        return proc.pid

    def destroy(self, pid):
        proc = next((p for p in self.process_list if p.pid == pid), None)
        if proc:
            self.memory.free(proc.memory_block)
            self.process_list.remove(proc)
        else:
            logging.warning(f"Attempted to destroy unknown PID: {pid}")

    def panic(self, msg, code):
        logging.critical(f"KERNEL PANIC: {msg} | Code: {code}")
        sys.exit(1)

kernel = Kernel()

def process_management(priority=1, mem_size=1024):
    def wrap(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            pid = None
            result = None
            try:
                pid = kernel.spawn(func.__name__, priority, mem_size)
                result = func(*args, **kwargs)
            except Exception as e:
                logging.error(f"Error in process '{func.__name__}': {e}")
                kernel.panic("Process fail", KERNEL_ERRORS['PROCESS_FAIL'])
            finally:
                if pid:
                    kernel.destroy(pid)
            return result
        return inner
    return wrap
