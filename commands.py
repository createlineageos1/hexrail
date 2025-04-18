import random
from termcolor import colored
import os
import time
from kernel import process_management
import webbrowser

usr = "hexrail"
os = "hexrail 1.0 emulated"
ui = "cli"

class CommandProcessor:
  @staticmethod
  @process_management(priority=3)
  def cmd():
    print("showfetch, usrdata, systurnoff, bored, ota, hme")

  @staticmethod
  @process_management(priority=1)
  def ota():
    webbrowser.open("https://www.figma.com/proto/Xl70GkHcPBv0fywmeZT2FT/hexrail-updates?node-id=1-2&p=f&t=3DvVl8pyKf0qqzeQ-0&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1")

  @staticmethod
  @process_management(priority=2)
  def usrdata():
    print(usr)

  @staticmethod
  @process_management(priority=1)
  def systurnoff():
    exit()

  @staticmethod
  @process_management(priority=3)
  def showfetch():
    print("User:", usr)
    print("OS:", os)
    print("UI:", ui)

  @staticmethod
  @process_management(priority=1)
  def hme():
      webbrowser.open("https://www.figma.com/proto/6BIq0bwjp4UNTA4k137S5L/hexmobenv?node-id=1-1587&t=VtsHSvo6nCksWXqK-0&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1")
