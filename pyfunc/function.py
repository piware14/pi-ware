from tkinter import *
from tkinter.ttk import *
import tkinter as tk

def show_desc(apt,*args):
    item = tree.selection()[0]
    app = tree.item(item,"text")
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
    text_box = Text(desc_win, height=12, width=40)
    text_box.pack()
    text_box.insert('end', desc_contents)
    text_box.config(state='disabled')
    #Disabled for now.
    #app_desc = tk.Label(desc_win, text=desc_contents, font="Arial 9")
    #app_desc.pack()
    #Check if website file exist
    filepath = f"/home/{username}/pi-ware/apps/{app}/website"
    try:
            file_tst = open(filepath)
            file_tst.close()

    except FileNotFoundError:
            Web = "False"

    else:
            Web = "True"

    #Add website from file
    if Web == "True":
            websiteurlfile = open(f"/home/{username}/pi-ware/apps/{app}/website", "r")
            websiteurl = websiteurlfile.read()
            Website = classes.HyperLink(desc_win, f"""{websiteurl}""");
            Website.pack()

    install = tk.Button(desc_win, text="INSTALL", font="Arial 11 bold", width=200, bg="darkblue", fg="white", command=install_app)
    install.pack()
    uninstall = tk.Button(desc_win, text="UNINSTALL", font="Arial 11 bold", width=200, bg="red", fg="white", command=uninstall_app)
    uninstall.pack()
    back_to_menu_button = tk.Button(desc_win, text="BACK", font="Arial 11 bold", width=200, height=2, bg="green", fg="white", command=back_to_menu)
    back_to_menu_button.pack(side = "bottom")
    desc_win.protocol("WM_DELETE_WINDOW",back_to_menu)

def back_to_menu(window, parent, app=None):
    parent.destroy()
    window.deiconify()

def install_app():
    global install_script
    #print(f"bash /home/{username}/pi-ware/func/term/term-run {install_script}")
    os.system(f"bash /home/{username}/pi-ware/func/term/term-run {install_script}")

def uninstall_app():
    global uninstall_script
    #print(f"bash /home/{username}/pi-ware/func/term/term-run {uninstall_script}")
    os.system(f"bash /home/{username}/pi-ware/func/term/term-run {uninstall_script}")

def back_to_menu():
    window.deiconify()
    desc_win.destroy()
    window.title("Pi-Ware")
    window.eval('tk::PlaceWindow . center')

def quit():
    window.destroy()
