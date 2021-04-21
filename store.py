# Pi-Ware main UI by ZachTheCoder

import tkinter as tk
import os

window = tk.Tk()
window.resizable(0, 0)
window.geometry("320x500")
window.title("Pi-Ware")

def back_to_menu():

    discord_app_button.pack_forget()
    window.title("Pi-Ware")
    all_apps_button.pack()
    editors_button.pack()
    games_button.pack()
    internet_button.pack()
    tools_button.pack()
    back_to_menu_button.pack_forget()

back_to_menu_button = tk.Button(
    text="BACK",
    font="Arial 11 bold",
    width=320,
    height=2,
    bg="green",
    fg="white",
    command=back_to_menu)


install_script = "lxterminal -e 'sudo python3 /home/pi/pi-ware/apps/Discord/install.py'"


# App button functions

def discord_app():

    discord_app_button.pack_forget()
    window.title("Pi-Ware: Discord")
    desc = open("/home/pi/pi-ware/apps/Discord/description.txt", "r")
    desc_contents = desc.read()
    blank_line.pack()
    discord_desc = tk.Label(
        text=desc_contents,
        font="Arial 9")
    discord_desc.pack()
    back_to_menu_button.pack_forget()
    blank_line.pack()
    install_discord.pack()
    install_script = "lxterminal -e 'sudo python3 /home/pi/pi-ware/apps/Discord/install.py'"

# App install button

def install_app():
    os.system(install_script)

install_discord = tk.Button(
    text="INSTALL",
    font="Arial 15 bold",
    width=200,
    bg="darkblue",
    fg="white",
    command=install_app)

# App buttons

discord_app_button = tk.Button(
    text="Discord",
    font="Arial 11 bold",
    width=320,
    bg="gray",
    fg="white",
    command=discord_app)

blank_line = tk.Label(text="")
blank_line.pack()

def all_apps():
    
    window.title("Pi-Ware: All Apps")
    all_apps_button.pack_forget()
    editors_button.pack_forget()
    games_button.pack_forget()
    internet_button.pack_forget()
    tools_button.pack_forget()
    discord_app_button.pack()
    back_to_menu_button.pack(side="bottom")
    
all_apps_button = tk.Button(
    text="All Apps",
    font="Arial 11 bold",
    width=320,
    bg="gray",
    fg="white",
    command=all_apps)

all_apps_button.pack()

editors_button = tk.Button(
    text="Editors",
    font="Arial 11 bold",
    width=320,
    bg="gray",
    fg="white")

editors_button.pack()

games_button = tk.Button(
    text="Games",
    font="Arial 11 bold",
    width=320,
    bg="gray",
    fg="white")

games_button.pack()

def internet():
    
    window.title("Pi-Ware: Internet")
    all_apps_button.pack_forget()
    editors_button.pack_forget()
    games_button.pack_forget()
    internet_button.pack_forget()
    tools_button.pack_forget()
    discord_app_button.pack()
    current_window = "internet"
    back_to_menu_button.pack(side="bottom")

internet_button = tk.Button(
    text="Internet",
    font="Arial 11 bold",
    width=320,
    bg="gray",
    fg="white",
    command=internet)

internet_button.pack()

tools_button = tk.Button(
    text="Tools",
    font="Arial 11 bold",
    width=320,
    bg="gray",
    fg="white")

tools_button.pack()


window.mainloop()
