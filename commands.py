import random
from termcolor import colored
import webbrowser
from kernel import process_management
import os
import subprocess

usr = "hexroid"
os_version = "hexrail 1.3 KERNEL_UPDATE"
ui = "CLI_based"

class CommandProcessor:
    @staticmethod
    @process_management(priority=1)
    def ota():
        print("Opening OTA link...")
        webbrowser.open("https://www.figma.com/proto/Xl70GkHcPBv0fywmeZT2FT/hexrail-updates?node-id=1-2&p=f&t=3DvVl8pyKf0qqzeQ-0&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1")

    @staticmethod
    @process_management(priority=2)
    def usrdata():
        print(usr)

    @staticmethod
    @process_management(priority=1)
    def systurnoff():
        confirm = input("Are you sure you want to turn off the Hexroid system? (yes/no): ")
        if confirm.lower() == "yes":
            print("System turning off...")
            exit()
        else:
            print("Cancelled.")

    @staticmethod
    @process_management(priority=3)
    def showfetch():
        print("User:", usr)
        print("OS:", os_version)
        print("UI:", ui)

    @staticmethod
    @process_management(priority=1)
    def hme():
        print("Opening HexMobEnv...")
        webbrowser.open("https://www.figma.com/proto/6BIq0bwjp4UNTA4k137S5L/hexmobenv?node-id=1-1587&t=VtsHSvo6nCksWXqK-0&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1")

    @staticmethod
    @process_management(priority=1)
    def bored():
        bored_commands = [
            "play a game",
            "watch a movie",
            "read a book",
            "go for a walk",
            "listen to music",
            "try a new recipe",
            "learn something new",
            "call a friend",
            "do some exercise",
            "meditate"
        ]
        print("You can:", random.choice(bored_commands))

    @staticmethod
    @process_management(priority=1)
    def watch():
        print("Opening YouTube...")
        webbrowser.open("https://www.youtube.com/")

    @staticmethod
    @process_management(priority=1)
    def movie():
        print("Opening Netflix...")
        webbrowser.open("https://www.netflix.com/")

    @staticmethod
    @process_management(priority=1)
    def cmd():
        """Basic command processor"""
        print(colored("Welcome to HexrailTV CLI.", "green"))
        print(colored("Available commands:", "cyan"))
        print(colored("showfetch - Display system information", "yellow"))
        print(colored("usrdata - Display user data", "yellow"))
        print(colored("systurnoff - Turn off the system", "yellow"))
        print(colored("ota - Open OTA update page", "yellow"))
        print(colored("hme - Open HexMobEnv page", "yellow"))
        print(colored("bored - Suggest an activity when bored", "yellow"))
        print(colored("watch - Open YouTube", "yellow"))
        print(colored("movie - Open Netflix", "yellow"))
        print(colored("exit - Exit the system", "yellow"))
