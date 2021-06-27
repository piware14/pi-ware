# Pi-Ware setup window

from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import os
from functools import partial
import getpass

#Create window
window = tk.Tk()

#Set global var username
global username
username = getpass.getuser()

#Set window icon
p1 = PhotoImage(file = f'/home/{username}/pi-ware/icons/logo.png')
window.iconphoto(False, p1)

#Set window title, size, and location
window.title("Setup Pi-Ware")
window.geometry("300x200")
window.eval('tk::PlaceWindow . center')

heading = tk.Label(window, text="""Setup Pi-Ware""", font="Arial 15 bold")
heading.pack()

def StoreData(Data, Location):
    os.system(f"echo '{Data}' > {Location}")
    window.destroy()

def retrieve_input():
    inputValue=textBox.get("1.0", "end-1c")
    StoreData(inputValue, "$HOME/.local/share/pi-ware/passwd")

Thankforinstall = tk.Label(window, text="""Thanks for installing pi-ware! \nLet's set some things up.""", font="Arial 12")
Thankforinstall.pack()

description = tk.Label(window, text="""First enter your password:""", font="Arial 12")
description.pack()

textBox=tk.Text(window, height=1, width=10)
textBox.pack()

buttonCommit=tk.Button(window, height=1, width=10, text="Enter", command=lambda: retrieve_input())
buttonCommit.pack()

window.mainloop()
