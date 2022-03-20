# Pi-Ware update GUI

from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedStyle
import tkinter as tk
import os
from screeninfo import get_monitors

#Create window
window = tk.Tk()
window.title("Update Pi-Ware")

width = None
height = None
for m in get_monitors():
    width = (m.width)-(162*2)
    height = 35
    print(height)
    print(width)

window.geometry("320x200+" + str(int(width)) + "+" + str(int(height)))
style = ThemedStyle(window)
style.set_theme("arc")
window.configure(bg='#f5f6f7')

#Functions
def update():
    os.system("bash $HOME/pi-ware/func/term/term-run 'bash $HOME/pi-ware/updater' 'Updating pi-ware'")
    window.destroy()

#Heading
heading = Label(window,text="""Update Pi-Ware""",font=('Arial', 15))

#Descripton
description1 = Label(window,text="""A new Pi-Ware update is available.""",font="Arial 13")
description2 = Label(window,text="""Click the 'update' button to proceed.""",font="Arial 13")

#Button
update_button = Button(window,text="UPDATE",width=100,command=update,style="update.TButton")
style.configure("update.TButton", foreground='green', background='green', font=("Arial", 15))

#Pack items
heading.pack()
description1.pack()
description2.pack()
update_button.pack(side="bottom")

window.mainloop()

