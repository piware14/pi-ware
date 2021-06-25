# Pi-Ware settings GUI

#Import tk and os
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import os
from functools import partial
import getpass

#Variables
global username
username = getpass.getuser()

#Set window info
window = tk.Tk()
window.title("Pi-Ware Settings")

#Set window image
p1 = PhotoImage(file = f'/home/{username}/pi-ware/icons/logo.png')

# Icon set for program window
window.iconphoto(False, p1)
window.geometry("500x500")
heading = tk.Label(window,text="""Pi-Ware Settings""",font="Arial 15 bold")
heading.pack()

#Functions
def change(setting, mode):
    os.system(f"lxterminal -e 'bash $HOME/pi-ware/func/settings {setting} {mode}'")

def show_desc(app):
    global change, desc_win
    desc_win = tk.Toplevel(window)
    window.resizable(0, 0)
    desc_win.title(f"{app}")
    desc_win.geometry("320x500")
    window.withdraw()
    desc = open(f"/home/{username}/pi-ware/func/settings/{app}/setting.txt", "r")
    desc_contents = desc.read()
    app_desc = tk.Label(desc_win, text=desc_contents, font="Arial 9")
    app_desc.pack()
    install = tk.Button(desc_win, text="INSTALL", font="Arial 11 bold", width=200, bg="darkblue", fg="white", command=desc_win.destroy)
    install.pack()
    back_to_menu_button = tk.Button(desc_win, text="BACK", font="Arial 11 bold", width=200, height=2, bg="green", fg="white", command=back_to_menu)
    back_to_menu_button.pack(side = "bottom")
    ucommand = f"bash '/home/{username}/pi-ware/func/uninst' %s" % app
    command = f"bash '/home/{username}/pi-ware/func/inst' %s" % app
    install_script = "'%s'" % command
    uninstall_script = "'%s'" % ucommand

def back_to_menu(window, parent, app=None):
    parent.destroy()
    window.deiconify()

def back_to_menu():
    window.deiconify()
    desc_win.destroy()
    window.title("Pi-Ware")
    window.eval('tk::PlaceWindow . center')

#Buttons
se = next(os.walk(f"/home/{username}/pi-ware/func/settings/"))[1]
settingslist = sorted(se)
print("Current settings:\n")
for app in settingslist:
    print(app)
    appb = ""
    for a in app:
        if(a == " "):
            appb += "_"
        else:
            appb += a
    exec(appb + f"""_button =  tk.Button(frame.inner, text=Change {app} settings, font="Arial 11 bold", width=200, bg="darkblue", fg="white"""")
    exec(appb + "_button.pack()")

#updatersettings_button = tk.Button(window,text="Change updater settings",font="Arial 11 bold",width=200,bg="darkblue",fg="white",command=change)
quit_button = tk.Button(window,text="Quit",font="Arial 11 bold",width=100,height=4,bg="green",fg="white",command=change)

#Main
description = tk.Label(window,text="""Change the settings of pi-ware.""",font="Arial 12")
description.pack()
#updatersettings_button.pack()
quit_button.pack(side="bottom")
window.mainloop()
