#!/usr/bin/env python3
# Pi-Ware main UI

import tkinter as tk
import os
from os.path import dirname, realpath
from functools import partial

pw_prefix = dirname(dirname(realpath(__file__)));
apps_dir = f"{pw_prefix}/share/pi-ware/apps/";

class WrapLabel(tk.Label):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, wraplength=315, justify="center", *args, **kwargs)

class AppButton(tk.Button):
    def __init__(self, parent, app, fg=None, command=None, *args, **kwargs):
        super().__init__(parent,
            font="Arial 11 bold",
            width=200,
            fg=(fg or "white"),
            command=partial(command, parent, app),
        *args, **kwargs)

def show_desc(window, app):
    desc_win = tk.Toplevel(window)
    desc_win.title(f"{app} on Pi-Ware")
    desc_win.geometry("320x500")
    desc_win.wm_protocol("WM_DELETE_WINDOW", partial(back_to_menu, window, desc_win))
    window.withdraw()

    with open(f"{apps_dir}/{app}/description.txt", "r") as desc:
        desc_contents = desc.read()
        app_desc = WrapLabel(desc_win,
            text=desc_contents,
            font="Arial 9")
        app_desc.pack()

    install = AppButton(desc_win, app,
        text="INSTALL",
        bg="darkblue",
        command=install_app)
    uninstall = AppButton(desc_win, app,
        text="UNINSTALL",
        bg="red",
        command=uninstall_app)
    back = AppButton(desc_win, app,
        text="BACK",
        height=2,
        bg="green",
        command=partial(back_to_menu, window))

    install.pack()
    uninstall.pack()
    back.pack(side = "bottom")

def install_app(parent, app):
    command = f"sudo bash {apps_dir}/{app}/install"
    install_script = f"x-terminal-emulator -e '{command}'"
    os.system(install_script)
    
def uninstall_app(parent, app):
    ucommand = f"sudo bash {apps_dir}/{app}/uninstall"
    uninstall_script = f"x-terminal-emulator -e '{ucommand}'"
    os.system(uninstall_script)
    
def back_to_menu(window, parent, app=None):
    parent.destroy()
    window.deiconify()

def main():
    window = tk.Tk()
    window.resizable(0, 0)
    window.geometry("320x500")
    window.title("Pi-Ware")

    blank_line = tk.Label(text="")
    blank_line.pack()

    applist = next(os.walk(apps_dir))[1]
    print("Current apps:\n")
    for app in applist:
        print(app)
        button = AppButton(window, app, text=app, bg="gray", command=show_desc)
        button.pack()

    window.wm_protocol("WM_DELETE_WINDOW", window.destroy)
    try:
        window.mainloop()
    except KeyboardInterrupt:
        window.destroy()

if __name__ == "__main__":
    main()
