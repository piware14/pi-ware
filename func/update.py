# Pi-Ware update GUI

import tkinter as tk
import os

window = tk.Tk()
window.title("Update Pi-Ware")
window.geometry("500x500")

heading = tk.Label(window,text="""Update Pi-Ware""",font="Arial 15 bold")
heading.pack()

def update():
    os.system("lxterminal -e 'bash $HOME/pi-ware/updater'")
    window.destroy

update_button = tk.Button(window,text="UPDATE",font="Arial 11 bold",bg="green",fg="white",width=100,height=4,command=update)
update_button.pack(side="bottom")

description = tk.Label(window,text="""A new Pi-Ware update is available. Click the 'update' button to proceed.""",font="Arial 12")
description.pack()

window.mainloop()
