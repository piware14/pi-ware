#!/usr/bin/env python3
# Pi-Ware Settings UI
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

#Set global inable/disable scripts
global enable
global disable

#Import custom  pi-ware functions
import classes

window = tk.Tk()

#Functions
def show_desc(apt,*args):
    mainwinx = str(window.winfo_x())
    mainwiny = str(window.winfo_y())
    item = tree.selection()[0]
    app = tree.item(item,"text")
    global enable, disable, desc_win
    desc_win = tk.Toplevel(window)
    p2 = PhotoImage(file = f'/home/{username}/pi-ware/func/settings/options/{app}/icon.png')
    # Icon set for program window
    desc_win.iconphoto(False, p2)
    window.resizable(0, 0)
    desc_win.title(f"{app}")
    print("320x500+" + mainwinx + "+" + mainwiny)
    desc_win.geometry("320x500+" + mainwinx + "+" + mainwiny)
    window.withdraw()
    desc = open(f"/home/{username}/pi-ware/func/settings/options/{app}/description", "r")
    desc_contents = desc.read()
    text_box = Text(desc_win, height=12, width=40)
    text_box.pack()
    text_box.insert('end', desc_contents)
    text_box.config(state='disabled')

    enablebutton = tk.Button(desc_win, text="Enable", font="Arial 11 bold", width=200, bg="darkblue", fg="white", command=enable_setting)
    enablebutton.pack()
    disableutton = tk.Button(desc_win, text="Disable", font="Arial 11 bold", width=200, bg="red", fg="white", command=disable_setting)
    disablebutton.pack()
    ucommand = f"""bash /home/{username}/pi-ware/func/term/uninst '{app}' 'Uninstalling {app}'"""
    command = f"""bash /home/{username}/pi-ware/func/term/inst '{app}' 'Installing {app}'"""
    install_script = "'%s'" % command
    uninstall_script = "'%s'" % ucommand
    back_to_menu_button = tk.Button(desc_win, text="BACK", font="Arial 11 bold", width=200, height=2, bg="green", fg="white", command=back_to_menu)
    back_to_menu_button.pack(side = "bottom")
    desc_win.protocol("WM_DELETE_WINDOW",back_to_menu)

def back_to_menu(window, parent, app=None):
    parent.destroy()
    window.deiconify()

def install_app():
    global enable
    if IsDev == "True":
        print(f"bash /home/{username}/pi-ware/func/term/term-run {install_script}")
    os.system(f"bash /home/{username}/pi-ware/func/term/term-run {install_script}")

def uninstall_app():
    global disable
    if IsDev == "True":
        print(f"bash /home/{username}/pi-ware/func/term/term-run {uninstall_script}")
    os.system(f"bash /home/{username}/pi-ware/func/term/term-run {uninstall_script}")

def back_to_menu():
    window.deiconify()
    desc_win.destroy()
    window.title("Pi-Ware Settings")
    #window.eval('tk::PlaceWindow . center')

def quit():
    window.destroy()

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
window.geometry("330x500")
window.eval('tk::PlaceWindow . center')
window.title("Pi-Ware Settings")

# Window tabs
tab_control = Notebook(window)
prefrence_tab = Frame(tab_control)
news_tab = Frame(tab_control)
credits_tab = Frame(tab_control)
DEV_tab = Frame(tab_control)
tab_control.add(news_tab, text="News")
tab_control.add(prefrence_tab, text="Prefrence")
#Show dev tab if dev files are found
if IsDev == "True":
    tab_control.add(DEV_tab, text="Dev")
tab_control.pack(expand=0, fill="both")

#Show DEV stuff
PiWareVersionFile = open(f"/home/{username}/.local/share/pi-ware/version", "r")
PiWareVersioncontent = PiWareVersionFile.read()

files = folders = 0
for _, dirnames, filenames in os.walk(f"/home/{username}/pi-ware/func/settings/options"):
    files += len(filenames)
    folders += len(dirnames)
    InstallibleApps = "{:,} avilible settings".format(folders)

PiWareVersion = tk.Label(DEV_tab, text=f"Pi-Ware Version:\n{PiWareVersioncontent}", font="Arial 11 bold")
PiWareInstallableApps = tk.Label(DEV_tab, text=f"{InstallibleApps}", font="Arial 11 bold")
PiWareVersion.pack()
PiWareInstallableApps.pack()

#Show latest news message
NewsMessagefile = open(f"/home/{username}/pi-ware/func/info/settingsmessage", "r")
NewsMessagecontent = NewsMessagefile.read()
NewsMessage = tk.Label(news_tab, text=f"Latest news:\n{NewsMessagecontent}", font="Arial 11 bold")
NewsMessage.pack()

tree = Treeview(prefrence_tab)
tree.pack(expand=YES, fill=BOTH)
tree.column("#0", minwidth=0, width=330, stretch=NO)
s = Style()
s.configure('Treeview', rowheight=35)
ap = next(os.walk(f"/home/{username}/pi-ware/func/settings/options"))[1]
applist = sorted(ap)
print("Current settings:\n")
for app in applist:
    print(app)
    appb = ""
    for a in app:
        if(a == " "):
            appb += "_"
        else:
            appb += a
    tree.bind("<<TreeviewSelect>>", partial(show_desc,app))
    exec("""tree.insert('', 'end', text=f"{app}"_button)""")

ScrollForMore = tk.Label(prefrence_tab, text="Scroll down for more settings.", font="Arial 11 bold")
ScrollForMore.pack()

quitbutton = tk.Button(window, text="Quit", font="Arial 11 bold", width=200, bg="grey", fg="white", command=quit)
quitbutton.pack(side="bottom")

window.mainloop()
