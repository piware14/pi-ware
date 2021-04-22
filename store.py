# Pi-Ware main UI by ZachTheCoder
#test

import tkinter as tk
import os

os.system("cd /home/pi/pi-ware")
os.system("git pull")

window = tk.Tk()
window.resizable(0, 0)
window.geometry("320x500")
window.title("Pi-Ware")


window.mainloop()
