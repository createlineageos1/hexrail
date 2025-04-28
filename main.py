import os 
import sys
import time
import commands
from datetime import date
from termcolor import colored
from commands import CommandProcessor
from kernel import Kernel


cp = CommandProcessor()

ascii = """
 _                         _ _ 
 | |                       (_) |
 | |__   _____  ___ __ __ _ _| |
 | '_ \ / _ \ \/ / '__/ _` | | |
 | | | |  __/>  <| | | (_| | | |
 |_| |_|\___/_/\_\_|  \__,_|_|_|
                   
"""

def loading():
    for i in range(0, 101):
        time.sleep(0.0099)
        sys.stdout.write("\rStarting hexrail.. " + str(i) + "%")
        sys.stdout.flush()

    print(ascii)
    print("\n H E X R A I L")

system_commands = [
    'cp.cmd',
    'cp.bored',
    'cp.showfetch',
    'cp.systurnoff',
    'cp.ota',
    'cp.usrdata',
    'cp.hme',
    'cp.watch',
    'cp.movie'
]

kernel = Kernel()

loading()

c = colored
print(c("hexrail under APACHE-2.0 LICENSE.", "yellow"))

today = date.today()
print("Today's date:", today)
c = colored
print(c("security patch: 1 march 2024", "red"))
while True:
    user_input = input(f"usr@hexrail:{os.curdir}/$>> ").split(" ")
    entered_command = user_input[0]
    args = user_input[1:]
    
    command_found = False
    
    for command_str in system_commands:
        command_name = command_str.split('.')[-1]
        if command_name == entered_command:
            try:
                command_func = eval(command_str)
                command_func(*args)
                command_found = True
                break
            except Exception as e:
                print(f"Error while executing the command '{entered_command}': {e}")
                break
    if not command_found:
        print(f"Command '{entered_command}' not found.")
