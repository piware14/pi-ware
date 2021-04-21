# Discord install script by ZachTheCoder

import os
import time
import install_data

data = open("install_data.py", "w")

if install_data.discord_is_installed == True:
    print("""Discord is already installed.
Closing in 5 seconds.""")

elif install_data.discord_is_installed == False:
    print("Installing Discord...")
    time.sleep(2)
    os.system("wget https://github.com/SpacingBat3/electron-discord-webapp/releases/download/v1.3.0/webcord_1.3.0_armhf.deb")
    os.system('sudo apt -fy install ~/webcord_1.3.0_armhf.deb || error "Failed to install Discord!"')
    os.system("rm -f ~/webcord_1.3.0_armhf.deb")
    os.system("clear")
    data.write("discord_is_installed = True")
    print("""Successfully installed Discord.
Closing in 10 seconds.""")
