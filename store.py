# Pi-Ware main UI

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
window.resizable(0, 0)
window.geometry("320x500")
window.title("Pi-Ware")
frame = ScrolledFrame(window)
frame.pack(expand=True, fill="both")

username = getpass.getuser()

def show_desc(app):
    global install_script, uninstall_script, desc_win
    desc_win = tk.Toplevel(window)
    desc_win.title("Pi-Ware")
    desc_win.geometry("320x500")
    window.withdraw()
    desc = open(f"/home/{username}/pi-ware/apps/{app}/description.txt", "r")
    desc_contents = desc.read()
    app_desc = tk.Label(desc_win,
        text=desc_contents,
        font="Arial 9")
    app_desc.pack()
    install = tk.Button(desc_win,
        text="INSTALL",
        font="Arial 11 bold",
        width=200,
        bg="darkblue",
        fg="white",
        command=install_app)
    install.pack()
    uninstall = tk.Button(desc_win,
        text="UNINSTALL",
        font="Arial 11 bold",
        width=200,
        bg="red",
        fg="white",
        command=uninstall_app)
    uninstall.pack()
    back_to_menu_button = tk.Button(desc_win,
    text="BACK",
    font="Arial 11 bold",
    width=200,
    height=2,
    bg="green",
    fg="white",
    command=back_to_menu)
    back_to_menu_button.pack(side = "bottom")
    ucommand = f"sudo bash /home/{username}/pi-ware/apps/%s/uninstall" % app
    command = f"sudo bash /home/{username}/pi-ware/apps/%s/install" % app
    install_script = "lxterminal -e '%s'" % command
    uninstall_script = "lxterminal -e '%s'" % ucommand
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
    exec(appb + """_button =  tk.Button(frame.inner,
            text=app,
            font="Arial 11 bold",
            width=200,
            bg="gray",
            fg="white",
            command=partial(show_desc,app))""")
    exec(appb + "_button.pack()")

def install_app():
    global install_script
    os.system(install_script)
    
def uninstall_app():
    global uninstall_script
    os.system(uninstall_script)
    
def back_to_menu():
    window.deiconify()
    desc_win.destroy()
    window.title("Pi-Ware")
    
blank_line = tk.Label(text="")
blank_line.pack()
window.mainloop()
