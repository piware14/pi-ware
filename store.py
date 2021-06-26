# Pi-Ware main UI
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import os
from functools import partial
import getpass

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
    app_desc = tk.Label(desc_win, text=desc_contents, font="Arial 9")
    app_desc.pack()
    install = tk.Button(desc_win, text="INSTALL", font="Arial 11 bold", width=200, bg="darkblue", fg="white", command=install_app)
    install.pack()
    uninstall = tk.Button(desc_win, text="UNINSTALL", font="Arial 11 bold", width=200, bg="red", fg="white", command=uninstall_app)
    uninstall.pack()
    back_to_menu_button = tk.Button(desc_win, text="BACK", font="Arial 11 bold", width=200, height=2, bg="green", fg="white", command=back_to_menu)
    back_to_menu_button.pack(side = "bottom")
    ucommand = f"bash /home/{username}/pi-ware/func/uninst '{app}'' 'Uninstalling {app}"
    command = f"bash /home/{username}/pi-ware/func/inst '{app}'' 'Installing {app}"
    install_script = "'%s'" % command
    uninstall_script = "'%s'" % ucommand

def back_to_menu(window, parent, app=None):
    parent.destroy()
    window.deiconify()
tree = Treeview(window)
tree.pack(expand=YES, fill=BOTH)
tree.column("#0", minwidth=0, width=320, stretch=NO)
s = Style()
s.configure('Treeview', rowheight=35)
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
    tree.bind("<<TreeviewSelect>>", partial(show_desc,app))
    exec(appb + """_button =  PhotoImage(file=f'/home/{username}/pi-ware/apps/{app}/icon.png')""")
    exec("""tree.insert('', 'end', text=f"{app}",image=""" + appb + """_button)""")
def install_app():
    global install_script
    print(f"bash /home/{username}/pi-ware/func/term-run {install_script}")
    os.system(f"bash /home/{username}/pi-ware/func/term-run {install_script}")

def uninstall_app():
    global uninstall_script
    print(f"bash /home/{username}/pi-ware/func/term-run {uninstall_script}")
    os.system(f"bash /home/{username}/pi-ware/func/term-run {uninstall_script}")

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