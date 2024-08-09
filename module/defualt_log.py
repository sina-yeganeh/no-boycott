from colorama import Fore

def normal_log(text: str) -> None:
  print(
    Fore.RED + "[" +
    Fore.GREEN + "*" +
    Fore.RED + "] " +
    Fore.WHITE + text
  )

def error(err_msg: str) -> None:
  print(
    Fore.RED + "[!] " +
    Fore.WHITE + err_msg
  )

def warn(warn_msg:str) -> None:
  print(
    Fore.RED + "[" +
    Fore.YELLOW + "#" +
    Fore.RED + "] " +
    Fore.WHITE + warn_msg
  )
