# Pi-Ware main UI
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import os
from functools import partial
import getpass

class ScrolledFrame(tk.Frame):
    def __init__(self, parent, vertical=True, horizontal=False):
        super().__init__(parent)

        # canvas for inner frame
        self._canvas = tk.Canvas(self)
        self._canvas.grid(row=0, column=0, sticky="news") # changed

        # create right scrollbar and connect to canvas Y
        self._vertical_bar = tk.Scrollbar(self, orient="vertical", command=self._canvas.yview)
        if vertical:
            self._vertical_bar.grid(row=0, column=1, sticky="ns")
        self._canvas.configure(yscrollcommand=self._vertical_bar.set)

        # create bottom scrollbar and connect to canvas X
        self._horizontal_bar = tk.Scrollbar(self, orient="horizontal", command=self._canvas.xview)
        if horizontal:
            self._horizontal_bar.grid(row=1, column=0, sticky="we")
        self._canvas.configure(xscrollcommand=self._horizontal_bar.set)

        # inner frame for widgets
        self.inner = tk.Frame(self._canvas, bg="red")
        self._window = self._canvas.create_window((0, 0), window=self.inner, anchor="nw")

        # autoresize inner frame
        self.columnconfigure(0, weight=1) # changed
        self.rowconfigure(0, weight=1) # changed

        # resize when configure changed
        self.inner.bind("<Configure>", self.resize)
        self._canvas.bind("<Configure>", self.frame_width)

    def frame_width(self, event):
        # resize inner frame to canvas size
        canvas_width = event.width
        self._canvas.itemconfig(self._window, width = canvas_width)

    def resize(self, event=None):
        self._canvas.configure(scrollregion=self._canvas.bbox('all'))

window = tk.Tk()
#Set global var username
global username
username = getpass.getuser()

#Set window icon
p1 = PhotoImage(file = f'/home/{username}/pi-ware/icons/logo.png')
window.iconphoto(False, p1)

#Main
window.resizable(0, 0)
window.geometry("320x500")
window.eval('tk::PlaceWindow . center')
window.title("Pi-Ware")
#Show latest news message
NewsMessagefile = open(f"/home/{username}/pi-ware/func/infomessage", "r")
NewsMessagecontent = NewsMessagefile.read()
NewsMessage = tk.Label(window, text=f"Latest news:\n{NewsMessagecontent}", font="Arial 11 bold")
NewsMessage.pack()
frame = ScrolledFrame(window)
frame.pack(expand=True, fill="both")

def show_desc(app):
    global install_script, uninstall_script, desc_win
    desc_win = tk.Toplevel(window)
    p2 = PhotoImage(file = f'/home/{username}/pi-ware/apps/{app}/icon.png')
    # Icon set for program window
    desc_win.iconphoto(False, p2)
    window.resizable(0, 0)
    desc_win.title(f"{app}")
    desc_win.geometry("320x500")
    window.withdraw()
    desc = open(f"/home/{username}/pi-ware/apps/{app}/description.txt", "r")
    desc_contents = desc.read()
    app_desc = tk.Label(desc_win, text=desc_contents, font="Arial 9")
    app_desc.pack()
    install = tk.Button(desc_win, text="INSTALL", font="Arial 11 bold", width=200, bg="darkblue", fg="white", command=install_app)
    install.pack()
    uninstall = tk.Button(desc_win, text="UNINSTALL", font="Arial 11 bold", width=200, bg="red", fg="white", command=uninstall_app)
    uninstall.pack()
    back_to_menu_button = tk.Button(desc_win, text="BACK", font="Arial 11 bold", width=200, height=2, bg="green", fg="white", command=back_to_menu)
    back_to_menu_button.pack(side = "bottom")
    ucommand = f"bash '/home/{username}/pi-ware/func/uninst' %s" % app
    command = f"bash '/home/{username}/pi-ware/func/inst' %s" % app
    install_script = "'%s'" % command
    uninstall_script = "'%s'" % ucommand

def back_to_menu(window, parent, app=None):
    parent.destroy()
    window.deiconify()

ap = next(os.walk(f"/home/{username}/pi-ware/apps"))[1]
applist = sorted(ap)
print("Current apps:\n")
for app in applist:
    print(app)
    appb = ""
    for a in app:
        if(a == " "):
            appb += "_"
        else:
            appb += a
    exec(appb + """_button =  tk.Button(frame.inner, text=app, font="Arial 11 bold", width=200, bg="gray", fg="white", command=partial(show_desc,app))""")
    exec(appb + "_button.pack()")

def install_app():
    global install_script
    print("lxterminal -e " + install_script)
    os.system("lxterminal -e " + install_script)
    
def uninstall_app():
    global uninstall_script
    print("lxterminal -e " + uninstall_script)
    os.system("lxterminal -e " + uninstall_script)
    
def back_to_menu():
    window.deiconify()
    desc_win.destroy()
    window.title("Pi-Ware")
    window.eval('tk::PlaceWindow . center')

def quit():
    window.destroy()
    
quitbutton = tk.Button(window, text="Quit", font="Arial 11 bold", width=200, bg="grey", fg="white", command=quit)
quitbutton.pack()

window.mainloop()
