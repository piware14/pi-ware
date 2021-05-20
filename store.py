#!/usr/bin/env python3
# Pi-Ware main UI

import sys
import os
import json
import webbrowser
import tkinter as tk
from os.path import dirname, realpath
from functools import partial

pw_prefix = dirname(dirname(realpath(__file__))) + "/.local"
apps_dir = "/home/pi/pi-ware/apps/"
icon: tk.PhotoImage

class WrapLabel(tk.Label):
    def __init__(self, parent, justify=None, font=None, *args, **kwargs):
        super().__init__(parent,
            wraplength=315,
            font=(font or "Arial 9"),
            justify=(justify or "center"),
        *args, **kwargs)

class HyperLink(tk.Label):
	def __init__(self, parent, url, text=None, fg=None, cursor=None, *args, **kwargs):
		self.url = url;
		super().__init__(parent, text=(text or url),
            fg=(fg or "blue"),
            cursor=(cursor or "hand2"),
            font="Arial 9",
        *args, **kwargs)
		self.bind("<Button-1>", self.web_open);

	def web_open(self, event):
		return webbrowser.open(self.url);

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
    set_geometry(desc_win, 320, 500)
    desc_win.wm_protocol("WM_DELETE_WINDOW", partial(back_to_menu, window, desc_win))
    window.withdraw()

    app_website = None
    with open(f"{apps_dir}/{app}/meta.json", "r") as fd:
        tmp = fd.read().replace("\\\n", "").replace("\n", "").replace("\t", "")
        meta = json.loads(tmp)
        app_desc = WrapLabel(desc_win, text=f"""\n{meta["description"]}""")
        app_desc.pack()
        if "attr" in meta:
            app_attr = WrapLabel(desc_win, text=f"""\nSubmitted by: {meta["attr"]}""")
            app_attr.pack()
        if "website" in meta:
            app_website = HyperLink(desc_win, f"""{meta["website"]}""");
            app_website.pack()

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

    back.pack(side="bottom")
    uninstall.pack(side="bottom")
    install.pack(side="bottom")

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
    window.resizable(False, False)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = screen_width / 2 - width / 2
    y = screen_height / 2 - height / 2
    window.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
    window.iconphoto(False, icon)

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
    global icon
    window = tk.Tk()
    icon = tk.PhotoImage(file=f"{pw_prefix}/share/icons/pi-ware.png")
    set_geometry(window, 320, 500)
    window.title("Pi-Ware")

    blank_line = WrapLabel(window, text="\nPlease select an app to install\n")
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
    if not os.system("/home/pi/pi-ware/update"):
        check_updates()
    sys.exit(main())
