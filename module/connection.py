import subprocess
import sys

from module.defualt_log import normal_log, error, warn

def change_dns(wired_connection_name: str, dns_service: dict):
  if dns_service != None and wired_connection_name != None:
    try:
      cmd = f"sudo nmcli connection modify \"{wired_connection_name}\" \
        ipv4.dns \"{str(dns_service["primary"]) + " " + str(dns_service["secondary"])}\""

      subprocess.call(cmd, shell=True)
    except Exception as err:
      error(f"Programme exit with error:{err}")

      warn("Make sure you are running programme from root")
      warn("Did you install requirements?")
      sys.exit()

    normal_log("DNS successfully changed")

    warn("Recommaned to reconnect to your wired connection")
    warn("If you are using browser or terminal please close and open it again")

    # TODO: Add auto reconnecting to script

    return True
  else:
    return 0
