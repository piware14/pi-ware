'''
   ▄████████    ▄███████▄    ▄███████▄    ▄████████         ▄███████▄ ▄██   ▄   
  ███    ███   ███    ███   ███    ███   ███    ███        ███    ███ ███   ██▄ 
  ███    ███   ███    ███   ███    ███   ███    █▀         ███    ███ ███▄▄▄███ 
  ███    ███   ███    ███   ███    ███   ███               ███    ███ ▀▀▀▀▀▀███ 
▀███████████ ▀█████████▀  ▀█████████▀  ▀███████████      ▀█████████▀  ▄██   ███ 
  ███    ███   ███          ███                 ███        ███        ███   ███ 
  ███    ███   ███          ███           ▄█    ███        ███        ███   ███ 
  ███    █▀   ▄████▀       ▄████▀       ▄████████▀  ███   ▄████▀       ▀█████▀  


       ▄▄▄▄ ▓██   ██▓    ██▓    ▓█████  ██░ ██  ▄▄▄▄▄█████▓ █    ██  ██▓███   ▒█████   ██▓ ███▄    █ ▄▄▄█████▓ ▒█████   █     █░
▓█████▄▒██  ██▒   ▓██▒    ▓█   ▀ ▓██░ ██▒▒████▄   ▓  ██▒ ▓▒ ██  ▓██▒▓██░  ██▒▒██▒  ██▒▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▒██▒  ██▒▓█░ █ ░█░
▒██▒ ▄██▒██ ██░   ▒██░    ▒███   ▒██▀▀██░▒██  ▀█▄ ▒ ▓██░ ▒░▓██  ▒██░▓██░ ██▓▒▒██░  ██▒▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░▒██░  ██▒▒█░ █ ░█ 
▒██░█▀  ░ ▐██▓░   ▒██░    ▒▓█  ▄ ░▓█ ░██ ░██▄▄▄▄██░ ▓██▓ ░ ▓▓█  ░██░▒██▄█▓▒ ▒▒██   ██░░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒██   ██░░█░ █ ░█ 
░▓█  ▀█▓░ ██▒▓░   ░██████▒░▒████▒░▓█▒░██▓ ▓█   ▓██▒ ▒██▒ ░ ▒▒█████▓ ▒██▒ ░  ░░ ████▓▒░░██░▒██░   ▓██░  ▒██▒ ░ ░ ████▓▒░░░██▒██▓ 
░▒▓███▀▒ ██▒▒▒    ░ ▒░▓  ░░░ ▒░ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒ ░░   ░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░░ ▒░▒░▒░ ░▓  ░ ▒░   ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ░ ▓░▒ ▒  
▒░▒   ░▓██ ░▒░    ░ ░ ▒  ░ ░ ░  ░ ▒ ░▒░ ░  ▒   ▒▒ ░   ░    ░░▒░ ░ ░ ░▒ ░       ░ ▒ ▒░  ▒ ░░ ░░   ░ ▒░    ░      ░ ▒ ▒░   ▒ ░ ░  
 ░    ░▒ ▒ ░░       ░ ░      ░    ░  ░░ ░  ░   ▒    ░       ░░░ ░ ░ ░░       ░ ░ ░ ▒   ▒ ░   ░   ░ ░   ░      ░ ░ ░ ▒    ░   ░  
 ░     ░ ░            ░  ░   ░  ░ ░  ░  ░      ░  ░           ░                  ░ ░   ░           ░              ░ ░      ░    hehehehehehehehehehe! 
      ░░ ░
                                         

'''

import getpass
import json

global username
username = getpass.getuser()

class App():
    def __init__(self, name, architecture):
        self.architecture = architecture
        self.path = f"/home/{username}/pi-ware/apps/{name}/"
        self.icon = self.path + "icon.png"
        self.icon200 = self.path + "icon-200.png"
        self.name = name
        try:
            self.website = open(self.path + "website").read()
        except:
            self.website = "\n\nWebsite not available"
            
        self.description = open(self.path + "description.txt").read()
        self.install = self.path + "install"
        self.uninstall = self.path + "uninstall"
        
def parseApps():
    file = open(f'/home/{username}/pi-ware/apps/apps.json')
    data = list(json.load(file).items())
    applist = list()
    for app in data:
        applist.append(App(app[0], app[1]))

    return applist


