# Pi-Ware setup window

from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import os
from functools import partial
import getpass
import datetime

#Set global var username
global username
username = getpass.getuser()

p1 = ""

#Date calc
current_time = datetime.datetime.now()

print(current_time)

if current_time.month == "12":
    if current_time.day == "25":
        print("Merry Christmas from the pi-ware team!")
        p1 = PhotoImage(file = f'/home/{username}/pi-ware/icons/logo-christmas.png')

#Create window
window = tk.Tk()

#Set window icon
window.iconphoto(False, p1)

#Set window title, size, and location
window.title("Setup Pi-Ware")
window.geometry("800x500")
window.eval('tk::PlaceWindow . center')

#Functions
def StoreData(Data, Location):
    os.system(f"echo '{Data}' > {Location}")
    window.destroy()

#Define labels
heading = tk.Label(window, text="""Setup Pi-Ware""", font="Arial 15 bold")
Thankforinstall = tk.Label(window, text="""Thanks for installing pi-ware!\nLet's set some things up.""", font="Arial 12")
description = tk.Label(window, text="""Do you want Pi-Ware to upload erros, logs and app info to the pi-ware team?\nPlease note, the pi-ware-team can not use this data to:\ntrack, monitor, or identify you.""", font="Arial 12")

#Define buttons
YesButton=tk.Button(window, height=1, width=10, text="Yes", command=lambda: StoreData("True", "$HOME/.local/share/pi-ware/telementry"))
NoButton=tk.Button(window, height=1, width=10, text="No", command=lambda: StoreData("False", "$HOME/.local/share/pi-ware/telementry"))

#Pack objects
heading.pack()
Thankforinstall.pack()
description.pack()
YesButton.pack()
NoButton.pack()

window.mainloop()
