import tkinter as tk
import os

window = tk.Tk()
window.resizable(0, 0)
window.geometry("320x500")
window.title("Pi-Ware")

blank_line = tk.Label(text="")

blank_line.pack()

# Install/uninstall apps

def install_discord_app():
    os.system("lxterminal -e 'wget -qO- https://raw.githubusercontent.com/zachthecoder14/pi-ware-scripts/main/discord-install-32 | bash'")

def uninstall_discord_app():
    os.system("lxterminal -e 'wget -qO- https://raw.githubusercontent.com/zachthecoder14/pi-ware-scripts/main/discord-uninstall | bash'")

def install_firefox_app():
    os.system("lxterminal -e 'wget -qO- https://raw.githubusercontent.com/zachthecoder14/pi-ware-scripts/main/firefox-install | bash'")

def uninstall_firefox_app():
    os.system("lxterminal -e 'wget -qO- https://raw.githubusercontent.com/zachthecoder14/pi-ware-scripts/main/firefox-uninstall | bash'")


# App windows

def discord_app_window():
    discord_app_button.pack_forget()
    firefox_app_button.pack_forget()
    description_file = open("/home/pi/pi-ware/apps/Discord/description.txt")
    description = description_file.read()

    description_contents = tk.Label(
        text=description,
        font="Arial 9")
    
    description_contents.pack()

    discord_install_button = tk.Button(
        text="INSTALL",
        font="Arial 11 bold",
        width=150,
        bg="green",
        fg="white",
        command=install_discord_app)

    discord_install_button.pack()

    discord_uninstall_button = tk.Button(
        text="UNINSTALL",
        font="Arial 11 bold",
        width=150,
        bg="red",
        fg="white",
        command=uninstall_discord_app)

    discord_uninstall_button.pack()

def firefox_app_window():
    discord_app_button.pack_forget()
    firefox_app_button.pack_forget()
    description_file = open("/home/pi/pi-ware/apps/Firefox/description.txt")
    description = description_file.read()

    description_contents = tk.Label(
        text=description,
        font="Arial 9")
    
    description_contents.pack()

    firefox_install_button = tk.Button(
        text="INSTALL",
        font="Arial 11 bold",
        width=150,
        bg="green",
        fg="white",
        command=install_firefox_app)

    firefox_install_button.pack()

    firefox_uninstall_button = tk.Button(
        text="UNINSTALL",
        font="Arial 11 bold",
        width=150,
        bg="red",
        fg="white",
        command=uninstall_firefox_app)

    firefox_uninstall_button.pack()

# App buttons

discord_app_button = tk.Button(
    text="Discord",
    font="Arial 11",
    width=320,
    bg="gray",
    fg="white",
    command=discord_app_window)

discord_app_button.pack()

firefox_app_button = tk.Button(
    text="Firefox",
    font="Arial 11",
    width=320,
    bg="gray",
    fg="white",
    command=firefox_app_window)

firefox_app_button.pack()


window.mainloop()
