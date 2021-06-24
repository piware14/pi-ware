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
    exec(appb + f"""_button =  tk.Button(frame.inner, text=Change {app} settings, font="Arial 11 bold", width=200, bg="darkblue", fg="white", command=change({app}, {mode})""")
    exec(appb + "_button.pack()")

#updatersettings_button = tk.Button(window,text="Change updater settings",font="Arial 11 bold",width=200,bg="darkblue",fg="white",command=change)
quit_button = tk.Button(window,text="Quit",font="Arial 11 bold",width=100,height=4,bg="green",fg="white",command=change)

#Main
description = tk.Label(window,text="""Change the settings of pi-ware.""",font="Arial 12")
description.pack()
#updatersettings_button.pack()
quit_button.pack(side="bottom")
window.mainloop()
