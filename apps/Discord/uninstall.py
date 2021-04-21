# Discord install script by ZachTheCoder

import os
import time
import install_data

data = open("install_data.py", "w")

if install_data.discord_is_installed == False:
    print("""Discord is not installed.
Closing in 5 seconds.""")

if install_data.discord_is_installed == True:
    print("Uninstalling Discord...")
    time.sleep(2)
    os.system("sudo apt purge -y webcord")
    os.system("clear")
    print("""Successfully uninstalled Discord.
Closing in 10 seconds.""")
