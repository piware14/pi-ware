#!/usr/bin/env python3
# Pi-Ware main UI
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import os
import webbrowser
from functools import partial
import getpass

#Set global var username
global username
username = getpass.getuser()

#Import custom  pi-ware functions
import function
import classes

window = tk.Tk()

#Test
# Using readlines()
file1 = open(f'/home/{username}/pi-ware/.dev', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))

#Check if dev files exist
filepath = f"/home/{username}/pi-ware/.dev"
try:
    file_tst = open(filepath)
    file_tst.close()

except FileNotFoundError:
    IsDev = "False"

else:
     IsDev = "True"

#Set window icon
p1 = PhotoImage(file = f'/home/{username}/pi-ware/icons/logo.png')
window.iconphoto(False, p1)

#Main
window.resizable(0, 0)
window.geometry("320x500")
window.eval('tk::PlaceWindow . center')
window.title("Pi-Ware")

# Window tabs
tab_control = Notebook(window)
apps_tab = Frame(tab_control)
news_tab = Frame(tab_control)
credits_tab = Frame(tab_control)
DEV_tab = Frame(tab_control)
tab_control.add(apps_tab, text="Apps")
tab_control.add(news_tab, text="News")
tab_control.add(credits_tab, text="Credits")
#Show dev tab if dev files are found
if IsDev == "True":
    tab_control.add(DEV_tab, text="Dev")
tab_control.pack(expand=0, fill="both")

#Show DEV stuff
PiWareVersionFile = open(f"/home/{username}/.local/share/pi-ware/version", "r")
PiWareVersioncontent = PiWareVersionFile.read()

files = folders = 0
for _, dirnames, filenames in os.walk(f"/home/{username}/pi-ware/apps"):
  # ^ this idiom means "we won't be using this value"
    files += len(filenames)
    folders += len(dirnames)
    InstallibleApps = "{:,} installible Apps".format(folders)

PiWareVersion = tk.Label(DEV_tab, text=f"Pi-Ware Version:\n{PiWareVersioncontent}", font="Arial 11 bold")
PiWareInstallableApps = tk.Label(DEV_tab, text=f"{InstallibleApps}", font="Arial 11 bold")
PiWareVersion.pack()
PiWareInstallableApps.pack()

#Show latest news message
NewsMessagefile = open(f"/home/{username}/pi-ware/func/info/latestnewsmessage", "r")
NewsMessagecontent = NewsMessagefile.read()
NewsMessage = tk.Label(news_tab, text=f"Latest news:\n{NewsMessagecontent}", font="Arial 11 bold")
NewsMessage.pack()

#Show info message
InfoMessagefile = open(f"/home/{username}/pi-ware/func/info/infomessage", "r")
InfoMessagecontent = InfoMessagefile.read()
InfoMessage = tk.Label(credits_tab, text=f"{InfoMessagecontent}", font="Arial 11 bold")
InfoMessage.pack()

#Add pi-ware website
Website = classes.HyperLink(credits_tab, f"""https://pi-ware.ml""");
Website.pack()

tree = Treeview(apps_tab)
tree.pack(expand=YES, fill=BOTH)
tree.column("#0", minwidth=0, width=320, stretch=NO)
s = Style()
s.configure('Treeview', rowheight=35)
ap = next(os.walk(f"/home/{username}/pi-ware/apps"))[1]
applist = sorted(ap)
print("Current apps:\n")
for app in applist:
    print(app)
    appb = ""
    for a in app:
        if(a == " "):
            appb += "_"
        else:
            appb += a
    tree.bind("<<TreeviewSelect>>", partial(function.show_desc,app))
    exec(appb + """_button =  PhotoImage(file=f'/home/{username}/pi-ware/apps/{app}/icon.png')""")
    exec("""tree.insert('', 'end', text=f"{app}",image=""" + appb + """_button)""")

quitbutton = tk.Button(window, text="Quit", font="Arial 11 bold", width=200, bg="grey", fg="white", command=function.quit)
quitbutton.pack(side="bottom")

window.mainloop()
