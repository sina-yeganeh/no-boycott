'''
  (C) Licence: MIT Licence - 2024

  No Boycott - First-only terminal tool for changing anti-
  boycotting DNS for Iran. Totally free and user friendly.
'''

from sys import exit
from os import geteuid

import subprocess

try:
  from colorama import Fore
except:
  answ = input("It seems you do not have requiremnts installed, Do you want to install them[Y/n]:")
  if answ == "n":
    exit()
  else:
    try:
      print("Installing ...")
      result = subprocess.call(
        "pip install colorama"
      )

      print("Output is:", result)
    except:
      print("Couldn't instal packages")
      exit()

from module import banner, connection, defualt_log

if geteuid() != 0:
  defualt_log.error("Please run script as root")
  exit()

# TODO: Write about me and tool
ABOUT = \
"""
 
"""

DNS = {
  "403_service": {
    "primary": "10.202.10.202",
    "secondary": "10.202.10.102"
  },
  "shecan": {
    "primary": "178.22.122.100",
    "secondary": "185.51.200.2"
  },
  "host_iran": {
    "primary": "172.29.0.100",
    "secondary": "172.29.2.100"
  },
  "begzar": {
    "primary": "185.55.226.26",
    "secondary": "185.55.225.25"
  },
  "electro": {
    "primary": "78.157.42.101",
    "secondary": "78.157.42.100"
  }
}

subprocess.call("clear")

banner.banner()
defualt_log.normal_log("Tool only work for Debian base linux distro")

def menu_option(number: int, option_name: str) -> None:
  print(
    Fore.RED + "[" +
    Fore.WHITE + str(number) +
    Fore.RED + "] " +
    Fore.WHITE + option_name
  )

def get_input(input_text) -> int:
  try:
    return input(
      Fore.BLUE + input_text +
      Fore.YELLOW
    )
  except KeyboardInterrupt:
    defualt_log.error(f"Exit with error:{KeyboardInterrupt}")
    exit()

is_running = True
while is_running:
  menu_option(1, "Change DNS")
  menu_option(2, "About Tool")
  menu_option(3, "Exit\n")
  number = int(get_input(" -> Number $ "))
  match number:
    case 1:
      print("\n")
      n = 1
      for service_name in DNS:
        menu_option(n, service_name)
        n += 1

      service_name = get_input("\n -> Service Name $ ")
      wired_name = get_input(" -> WiFi Name $ ")

      connection.change_dns(
        wired_name,
        DNS[service_name]
      )
    case 2:
      print(ABOUT)
    case 3:
      defualt_log.normal_log("Goodluck")
      exit()
