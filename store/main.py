#!/usr/bin/env python3
# Pi-Ware main UI
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import os
import webbrowser
from functools import partial
import getpass
import json

#Set global var username
global username
username = getpass.getuser()

#Set global install/uninstall scripts
global install_script
global uninstall_script

#Import custom  pi-ware functions
#import function
import classes

window = tk.Tk()

#Functions
def error(mode,message,contact):
    #Create window
    ErrorWindow = tk.Toplevel(window)
    #Set window icon based on arg 1
    icon = PhotoImage(file = f'/home/{username}/pi-ware/icons/error-{mode}.png')
    # Icon set for error window
    ErrorWindow.iconphoto(False, icon)
    errorhappened = tk.Label(ErrorWindow, text = "An error occurred!")
    #error message
    errormessage = tk.Label(ErrorWindow, text = message)
    #If contact is set to true, and telemetry is enabled, send us an error message.
    if contact == "True":
        error_message = {"error": "fatal", "action": "imedient"}
        with open('error.txt', 'w') as json_file:
            json.dump(error_message, json_file)
            if telemetry == "True":
                error_message = {"error": "fatal", "action": "imedient"}
                with open('error.txt', 'w') as json_file:
                    json.dump(error_message, json_file)
    #Ok button
    okbutton = tk.Button(newWindow, text = "ok")
    #Pack all items
    errorhappened.pack()
    errormessage.pack()
    okbutton.pack()

def show_desc(apt,*args):
    mainwinx = str(window.winfo_x())
    mainwiny = str(window.winfo_y())
    item = tree.selection()[0]
    app = tree.item(item,"text")
    global install_script, uninstall_script, desc_win
    desc_win = tk.Toplevel(window)
    p2 = PhotoImage(file = f'/home/{username}/pi-ware/apps/{app}/icon.png')
    # Icon set for program window
    desc_win.iconphoto(False, p2)
    window.resizable(0, 0)
    desc_win.title(f"{app}")
    print("320x500+" + mainwinx + "+" + mainwiny)
    desc_win.geometry("320x500+" + mainwinx + "+" + mainwiny)
    window.withdraw()
    desc = open(f"/home/{username}/pi-ware/apps/{app}/description.txt", "r")
    desc_contents = desc.read()
    text_box = Text(desc_win, height=12, width=40)
    text_box.pack()
    text_box.insert('end', desc_contents)
    text_box.config(state='disabled')
    #Old description box:
    #app_desc = tk.Label(desc_win, text=desc_contents, font="Arial 9")
    #app_desc.pack()
    #Check if website file exists
    try:
        file_tst = open(f"/home/{username}/pi-ware/apps/{app}/website")
        file_tst.close()
    except FileNotFoundError:
        Web = "False"
    else:
        Web = "True"
    #Add website from file
    if Web == "True":
            websiteurlfile = open(f'/home/{username}/pi-ware/apps/{app}/website', 'r')
            websiteurl = websiteurlfile.readlines()
            # Strips the newline character
            for line in websiteurl:
                #print("{}".format(line.strip()))
                Website = classes.HyperLink(desc_win, f"""{line}""");
                Website.pack()
    #Buttons
    install = tk.Button(desc_win, text="INSTALL", font="Arial 11 bold", width=200, bg="darkblue", fg="white", command=install_app)
    uninstall = tk.Button(desc_win, text="UNINSTALL", font="Arial 11 bold", width=200, bg="red", fg="white", command=uninstall_app)
    back_to_menu_button = tk.Button(desc_win, text="BACK", font="Arial 11 bold", width=200, height=2, bg="green", fg="white", command=back_to_menu)
    #Commands
    ucommand = f"""bash /home/{username}/pi-ware/func/term/uninst '{app}' 'Uninstalling {app}'"""
    command = f"""bash /home/{username}/pi-ware/func/term/inst '{app}' 'Installing {app}'"""
    install_script = "'%s'" % command
    uninstall_script = "'%s'" % ucommand
    #Pack all buttons
    install.pack()
    uninstall.pack()
    back_to_menu_button.pack(side = "bottom")
    desc_win.protocol("WM_DELETE_WINDOW",back_to_menu)

def back_to_menu(window, parent, app=None):
    parent.destroy()
    window.deiconify()

def install_app():
    global install_script
    if IsDev == "True":
        print(f"bash /home/{username}/pi-ware/func/term/term-run {install_script}")
    os.system(f"bash /home/{username}/pi-ware/func/term/term-run {install_script}")

def uninstall_app():
    global uninstall_script
    if IsDev == "True":
        print(f"bash /home/{username}/pi-ware/func/term/term-run {uninstall_script}")
    os.system(f"bash /home/{username}/pi-ware/func/term/term-run {uninstall_script}")

def back_to_menu():
    window.deiconify()
    desc_win.destroy()
    window.title("Pi-Ware")

def quit():
    window.destroy()

#Check for certain files
#Check if apps.json exists
try:
    file_tst = open(f"/home/{username}/pi-ware/apps/apps.json")
    file_tst.close()
except FileNotFoundError:
    error("critical", "Apps.json not found!", True)
else:
     #Read apps.json
     with open(f"/home/{username}/pi-ware/apps/apps.json") as f:
       archdata = json.load(f)

#Check if dev files exist
try:
    file_tst = open(f"/home/{username}/pi-ware/.dev")
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
window.geometry("330x500")
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
#Show dev stuff if dev files are found
if IsDev == "True":
    tab_control.add(DEV_tab, text="Dev")
    print("App arcitectures:")
    print(archdata)
tab_control.pack(expand=0, fill="both")

#Show DEV stuff
PiWareVersionFile = open(f"/home/{username}/.local/share/pi-ware/version", "r")
PiWareVersioncontent = PiWareVersionFile.read()

files = folders = 0
for _, dirnames, filenames in os.walk(f"/home/{username}/pi-ware/apps"):
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

#Show commit links
commitmessage = tk.Label(credits_tab, text=f"To see commits, please go to the link below.", font="Arial 11 bold")
commitmessage.pack()
commit = classes.HyperLink(credits_tab, f"""https://github.com/piware14/pi-ware/graphs/contributors""");
commit.pack()

#Add pi-ware website
piwarewebsite = tk.Label(credits_tab, text=f"To vist the pi-ware website, click the link below.", font="Arial 11 bold")
piwarewebsite.pack()
Website = classes.HyperLink(credits_tab, f"""https://pi-ware.ml""");
Website.pack()

tree = Treeview(apps_tab)
tree.pack(expand=YES, fill=BOTH)
tree.column("#0", minwidth=0, width=330, stretch=NO)
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
    tree.bind("<<TreeviewSelect>>", partial(show_desc,app))
    exec(appb + """_button =  PhotoImage(file=f'/home/{username}/pi-ware/apps/{app}/icon.png')""")
    exec("""tree.insert('', 'end', text=f"{app}",image=""" + appb + """_button)""")

ScrollForMore = tk.Label(apps_tab, text="Scroll down for more apps.", font="Arial 11 bold")
ScrollForMore.pack()

quitbutton = tk.Button(window, text="Quit", font="Arial 11 bold", width=200, bg="grey", fg="white", command=quit)
quitbutton.pack(side="bottom")

window.mainloop()
