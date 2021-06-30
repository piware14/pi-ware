#!/usr/bin/env python3
# Pi-Ware main UI
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import os
import webbrowser
from functools import partial
import getpass

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

# Window tabs
tab_control = Notebook(window)
apps_tab = Frame(tab_control)
news_tab = Frame(tab_control)
info_tab = Frame(tab_control)
tab_control.add(apps_tab, text="Apps")
tab_control.add(news_tab, text="News")
tab_control.add(credits_tab, text="Credits")
tab_control.pack(expand=0, fill="both")

#Show latest news message
NewsMessagefile = open(f"/home/{username}/pi-ware/func/info/latestnewsmessage", "r")
NewsMessagecontent = NewsMessagefile.read()
NewsMessage = tk.Label(news_tab, text=f"Latest news:\n{NewsMessagecontent}", font="Arial 11 bold")
NewsMessage.pack()

#Show info message
InfoMessagefile = open(f"/home/{username}/pi-ware/func/info/infomessage", "r")
InfoMessagecontent = InfoMessagefile.read()
InfoMessage = tk.Label(credits_tab, text=f"{InfoMessagecontent}", font="Arial 11 bold")
InfoMessage.pack()
#Add pi-ware website
Website = HyperLink(credits_tab, f"""https://pi-ware.ml""");
Website.pack()

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
    ucommand = f"bash /home/{username}/pi-ware/func/term/uninst '{app}'' 'Uninstalling {app}"
    command = f"bash /home/{username}/pi-ware/func/term/inst '{app}'' 'Installing {app}"
    install_script = "'%s'" % command
    uninstall_script = "'%s'" % ucommand

def back_to_menu(window, parent, app=None):
    parent.destroy()
    window.deiconify()

tree = Treeview(apps_tab)
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

quitbutton = tk.Button(window, text="Quit", font="Arial 11 bold", width=200, bg="grey", fg="white", command=quit)
quitbutton.pack(side="bottom")

window.mainloop()
