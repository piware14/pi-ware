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
    os.system("lxterminal -e 'bash $HOME/pi-ware/func/settings'")

#Buttons
install = tk.Button(window,text="INSTALL",font="Arial 11 bold",width=200,bg="darkblue",fg="white",command=change)
update_button = tk.Button(window,text="UPDATE",font="Arial 11 bold",bg="green",fg="white",width=100,height=4,command=change)

#Main
description = tk.Label(window,text="""Change the settings of pi-ware.""",font="Arial 12")
description.pack()
install.pack()
update_button.pack()
window.mainloop()
