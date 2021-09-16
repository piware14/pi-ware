# Pi-Ware update GUI

import tkinter as tk
import os

#Create window
window = tk.Tk()
window.title("Update Pi-Ware")
window.geometry("510x500")

#Functions
def update():
    os.system("bash $HOME/pi-ware/func/term/term-run 'bash $HOME/pi-ware/updater' 'Updating pi-ware'")
    window.destroy()

#Heading
heading = tk.Label(window,text="""Update Pi-Ware""",font="Arial 25 bold")

#Descripton
description1 = tk.Label(window,text="""A new Pi-Ware update is available.""",font="Arial 15")
description2 = tk.Label(window,text="""Click the 'update' button to proceed.""",font="Arial 15")

#Button
update_button = tk.Button(window,text="UPDATE",font="Arial 15 bold",bg="green",fg="white",width=100,height=4,command=update)

#Pack items
heading.pack()
description1.pack()
description2.pack()
update_button.pack(side="bottom")

window.mainloop()

