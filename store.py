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
    set_geometry(window, 320, 500)
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

def set_geometry(window, width, height):
    window.resizable(0, 0)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = screen_width / 2 - width / 2
    y = screen_height / 2 - height / 2
    window.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

def check_updates():
    window = tk.Tk()
    set_geometry(window, 320, 128)
    window.title("Pi-Ware update")

    blank_line = WrapLabel(window, text="\nThere is a Pi-Ware update available, please restart it to apply the changes.")
    blank_line.pack()

    ok_button = tk.Button(text="Ok", command=window.destroy)
    ok_button.pack(side="right", anchor="s");

    window.wm_protocol("WM_DELETE_WINDOW", window.destroy)
    try:
        window.mainloop()
    except KeyboardInterrupt:
        window.destroy()

def main():
    window = tk.Tk()
    set_geometry(window, 320, 500)
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
    if os.system(f"{pw_prefix}/share/pi-ware/update"):
        check_updates()
    main()
