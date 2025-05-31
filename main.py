import os 
import sys
import time
from datetime import date
from termcolor import colored
from commands import CommandProcessor
from kernel import Kernel
from package_manager import ensure_dirs, list_repo_packages, list_installed_packages, install_package, run_package, help_menu
import webbrowser
import subprocess

uiboot = input("Do you want to boot into Hexroid UI? (y/n): ").strip().lower()

if uiboot == 'y':
    webbrowser.open("https://www.figma.com/proto/6BIq0bwjp4UNTA4k137S5L/hexmobenv?node-id=1-417&t=JoCsnjV4sPCr4Qxk-0&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1")

else:
    print("Booting...")

password = input("Set a password for Hexroid: ")

os.system("cls" if os.name == "nt" else "clear")

password_confirm = input("Enter password: ")

cp = CommandProcessor()

ascii = r"""

 /$$   /$$                                         /$$       /$$
| $$  | $$                                        |__/      | $$
| $$  | $$  /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$  /$$  /$$$$$$$
| $$$$$$$$ /$$__  $$|  $$ /$$/ /$$__  $$ /$$__  $$| $$ /$$__  $$
| $$__  $$| $$$$$$$$ \  $$$$/ | $$  \__/| $$  \ $$| $$| $$  | $$
| $$  | $$| $$_____/  >$$  $$ | $$      | $$  | $$| $$| $$  | $$
| $$  | $$|  $$$$$$$ /$$/\  $$| $$      |  $$$$$$/| $$|  $$$$$$$
|__/  |__/ \_______/|__/  \__/|__/       \______/ |__/ \_______/
                                                                
                                                                
"""

if password == password_confirm:
    print("Password set successfully.")

else:
    print("Password doesn't match.")
    sys.exit("Exiting...")


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
    'cp.movie',
]

kernel = Kernel()

loading()

today = date.today()
print("Today's date:", today)
c = colored
while True:
    user_input = input(f"Enter command or app name 'cmd' for help:").split(" ")
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
