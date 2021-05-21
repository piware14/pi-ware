# Pi-Ware main UI

import tkinter as tk
import os
from functools import partial
import string

window = tk.Tk()
window.resizable(0, 0)
window.geometry("320x500")
window.title("Pi-Ware")


def show_desc(app):
    global install_script,uninstall_script,desc_win
    desc_win = tk.Toplevel(window)
    desc_win.title("Pi-Ware")
    desc_win.geometry("320x500")
    window.withdraw()
    desc = open(f"/home/sajo/pi-ware/apps/{app}/description.txt", "r")
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
    ucommand = "sudo bash /home/sajo/pi-ware/apps/%s/uninstall" % app
    command = "sudo bash /home/sajo/pi-ware/apps/%s/install" % app
    install_script = "lxterminal -e '%s'" % command
    uninstall_script = "lxterminal -e '%s'" % ucommand

ap = next(os.walk("/home/sajo/pi-ware/apps"))[1]
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
    exec(appb + """_button =  tk.Button(window,
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
