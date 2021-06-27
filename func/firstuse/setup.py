# Pi-Ware setup window

import tkinter as tk
import os

window = tk.Tk()
window.title("Setup Pi-Ware")
window.geometry("500x500")

heading = tk.Label(window,text="""Setup Pi-Ware""",font="Arial 15 bold")
heading.pack()

def StoreData(Data, Location):
    os.system(f"echo '{Data}' > {Location}")
    window.destroy()

def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    print(inputValue)

Thankforinstall = tk.Label(window,text="""Thanks for installing pi-ware! \nLet's set some things up.""",font="Arial 12")
Thankforinstall.pack()

description = tk.Label(window,text="""First enter your password:""",font="Arial 12")
description.pack()

textBox=tk.Text(window, height=2, width=10)
textBox.pack()

buttonCommit=Button(root, height=1, width=10, text="Enter", command=lambda: retrieve_input())
buttonCommit.pack()

window.mainloop()
