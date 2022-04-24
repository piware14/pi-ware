#!/usr/bin/env python3
# Pi-Ware main UI
from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedStyle
import tkinter as tk
import os
import webbrowser
from functools import partial
import getpass
import json
from screeninfo import get_monitors
from datetime import date

#Set global var username
global username
username = getpass.getuser()

#set global vsb to make scrollbar perfect
global vsb

todays_date = date.today()

#Set global install/uninstall scripts
global install_script
global uninstall_script
telemetry = None

#Import custom  pi-ware functions
import classes

window = Tk()
s = Style()

#Functions
def istherefile(file):
    try:
        file_tst = open(file)
        file_tst.close()
    except FileNotFoundError:
        return False
    else:
        return True

def callback(url):
   webbrowser.open_new_tab(url)

def error(mode,message,contact):
    #Create window
    ErrorWindow = Toplevel(window)
    #Set window icon based on arg 1
    icon = PhotoImage(file = f'/home/{username}/pi-ware/icons/error-{mode}.png')
    #print(f'/home/{username}/pi-ware/icons/error-{mode}.png')
    ErrorWindow.iconphoto(False, icon)
    ErrorWindow.title("Error!")
    canvas = Canvas(ErrorWindow, width = 35,  height = 35)
    canvas.pack()
    canvas.create_image(10,10, anchor=NW, image=icon)
    errorhappened = Label(ErrorWindow, text = "An error occurred!")
    #error message
    errormessage = Label(ErrorWindow, text = message)
    #If contact is set to true, and telemetry is enabled, send us an error message.
    if contact == "True":
        error_message = {"error": "fatal", "action": "imedient", "reason": f"{message}"}
        #print(error_message)
        with open('error.json', 'w') as json_file:
            json.dump(error_message, json_file)
            if telemetry == "True":
                print("Sending log to pi-ware HQ")
            else:
                print(f"Error saved at: '/home/{username}/pi-ware/store/error.json'")
                
    #Ok button
    okbutton = Button(ErrorWindow, text = "ok",command=quit)
    #Pack all items
    errorhappened.pack()
    errormessage.pack()
    okbutton.pack()
    ErrorWindow.mainloop()

def show_desc(apt,*args):
    # Gets the size of the mainwindow
    wingeo = window.geometry()
    item = tree.selection()[0]
    app = tree.item(item,"text").replace(' ✔', '')
    #print(app)
    global install_script, uninstall_script, desc_win, ficon
    desc_win = Toplevel(window)
    if istherefile(f'/home/{username}/pi-ware/apps/{app}/icon.png'):
      ficon = f'/home/{username}/pi-ware/apps/{app}/icon.png'
    else:
      ficon = f'/home/{username}/pi-ware/icons/app-no-icon.png'
    p2 = PhotoImage(file = ficon)
    # Icon set for program window
    desc_win.iconphoto(False, p2)
    window.resizable(0, 0)
    desc_win.title(f"{app}")
    #print("320x500+" + mainwinx + "+" + mainwiny)
    # Makes sure the new window is the same size as the old one
    desc_win.geometry(wingeo)
    desc_win.configure(background=s.lookup('TFrame', 'background'))
    #style = ThemedStyle(desc_win)
    #style.set_theme("arc")
    window.withdraw()
    if istherefile(f"/home/"+username+"/pi-ware/apps/"+app+"/description.txt"):
        desc = open(f"/home/"+username+"/pi-ware/apps/"+app+"/description.txt", "r")
    else:
        print("/home/"+username+"/pi-ware/apps/"+app+"/description.txt")
        desc = open(f"/home/{username}/pi-ware/func/info/def-description.txt", "r")
    desc_contents = desc.read()
    text_box = Text(desc_win, height=12, width=40)
    text_box.pack()
    text_box.insert('end', desc_contents)
    text_box.config(state='disabled')
    #Old description box:
    #app_desc = tk.Label(desc_win, text=desc_contents, font="Arial 9")
    #app_desc.pack()
    #Check if website file exists
    if istherefile(f"/home/{username}/pi-ware/apps/{app}/website"):
            websiteurlfile = open(f'/home/{username}/pi-ware/apps/{app}/website', 'r')
            websiteurl = websiteurlfile.readlines()
            # Strips the newline character
            for line in websiteurl:
                #print("{}".format(line.strip()))
                #Website = classes.HyperLink(desc_win, f"""{line}""");
                #Website.pack()

                Website = Label(desc_win, text=line,font=('Arial', 11), cursor="hand2")
                s.configure(Website, foreground='blue')
                Website.pack()
                Website.bind("<Button-1>", lambda e:
                callback(line))
    #Buttons
    install = Button(desc_win, text="INSTALL", width=200, command=lambda:install_app(app), style="install.TButton")
    uninstall = Button(desc_win, text="UNINSTALL", width=200, command=lambda:uninstall_app(app), style="uninstall.TButton")
    back_to_menu_button = Button(desc_win, text="BACK", width=200, command=back_to_menu, style="back.TButton")
    s.configure("install.TButton", foreground='blue', background='blue', font=("Arial", 11))
    s.configure("uninstall.TButton", foreground='red', background='red', font=("Arial", 11))
    s.configure("back.TButton", foreground='green', background='green', font=("Arial", 11))
    #Commands
    ucommand = f"""bash /home/{username}/pi-ware/func/term/uninst '{app}' 'Uninstalling {app}'"""
    command = f"""bash /home/{username}/pi-ware/func/term/inst '{app}' 'Installing {app}'"""
    install_script = "'%s'" % command
    uninstall_script = "'%s'" % ucommand
    #Pack all buttons
    if istherefile(f"/home/{username}/.local/share/pi-ware/inst/{app}"):
        uninstall.pack()
    else:
        install.pack()
    back_to_menu_button.pack(side = "bottom")
    desc_win.protocol("WM_DELETE_WINDOW",back_to_menu)

def back_to_menu(window, parent, app=None):
    parent.destroy()
    window.deiconify()

def install_app(app):
    global install_script
    if IsDev == "True":
        print(f"bash /home/{username}/pi-ware/func/term/term-run {install_script}")
    os.system(f"bash /home/{username}/pi-ware/func/term/term-run {install_script}")
    os.system(f"touch /home/{username}/.local/share/pi-ware/installedapps.json")
    print(app)
    print(username)
    os.chdir(r'/home/'+username+'/.local/share/pi-ware')
    os.listdir()
    prechange = open('installedapps.json', 'r')
    data = json.load(prechange)
    print(data)
    data[app] = "Installed"
    prechange.close()
    with open('/home/'+username+'/.local/share/pi-ware/installedapps.json', 'w') as json_file:
        json.dump(data, json_file)
    

def uninstall_app(app):
    global uninstall_script
    if IsDev == "True":
        print(f"bash /home/{username}/pi-ware/func/term/term-run {uninstall_script}")
    os.system(f"bash /home/{username}/pi-ware/func/term/term-run {uninstall_script}")
    print(app)
    print(username)
    os.chdir(r'/home/'+username+'/.local/share/pi-ware')
    os.listdir()
    prechange = open('installedapps.json', 'r')
    data = json.load(prechange)
    print(data)
    data[app] = "Uninstalled"
    prechange.close()
    with open('/home/'+username+'/.local/share/pi-ware/installedapps.json', 'w') as json_file:
        json.dump(data, json_file)

def back_to_menu():
    window.deiconify()
    desc_win.destroy()
    window.title("Pi-Ware")

def quit():
    window.destroy()

#Check for certain files
#Check if apps.json exists
if not istherefile(f"/home/{username}/pi-ware/apps/apps.json"):
    error("critical", "Apps.json not found!", True)
else:
    #Read apps.json
    with open(f"/home/{username}/pi-ware/apps/apps.json") as f:
        archdata = json.load(f)

#Check if dev files exist
if not istherefile(f"/home/{username}/pi-ware/.dev"):
    IsDev = "False"
else:
    IsDev = "True"

#Set window icon
if todays_date.month == "12":
    wico = f'/home/{username}/pi-ware/icons/logo-full-christmas.png'
else:
    wico = f'/home/{username}/pi-ware/icons/logo-full.png'
p1 = PhotoImage(file = f'{wico}')
window.iconphoto(False, p1)

#Main
width = None
height = None
for m in get_monitors():
    width = (m.width/2)-165
    height = m.height/2-250
    #print(height)
    #print(width)

#Create an instance of tkinter frame
#splash_win = Tk()
#Set the title of the window
#splash_win.title("Pi-Ware")
#Define the size of the window or frame
#splash_win.geometry("330x500+" + str(int(width)) + "+" + str(int(height)))
#Remove border of the splash Window
#splash_win.overrideredirect(True)
#Define the label of the window
#splash_label= Label(splash_win, text= "Hello World!", foreground= "green", font= ('Times New Roman', 40)).pack(pady=20)
window.resizable(0, 0)
window.geometry("330x500+" + str(int(width)) + "+" + str(int(height)))
#window.eval('tk::PlaceWindow . center')
window.title("Pi-Ware")
style = ThemedStyle(window)
global systheme
if istherefile(f"/home/{username}/.local/share/pi-ware/theme"):
    PiWareTheme = open(f"/home/{username}/.local/share/pi-ware/theme", "r")
    systheme = PiWareTheme.read()
    print(systheme)
    
    style.set_theme(systheme.strip())
else:
    systheme = "arc"
tabtext = "Apps"

def addscroll(event):
    selected = event.widget.select()
    tabtext = event.widget.tab(selected, "text")
    if (tabtext != "Apps"):
        vsb.place_forget()
    elif (tabtext  == "Apps"):
        vsb.place(x=310, y=60, height=380)
    #print(tabtext)

# Window tabs
tab_control = Notebook(window)
apps_tab = Frame(tab_control)
news_tab = Frame(tab_control)
credits_tab = Frame(tab_control)
DEV_tab = Frame(tab_control)
tab_control.bind("<<NotebookTabChanged>>", addscroll)
tab_control.add(apps_tab, text="Apps")
tab_control.add(news_tab, text="News")
tab_control.add(credits_tab, text="Credits")

#Show dev stuff if dev files are found
if IsDev == "True":
    tab_control.add(DEV_tab, text="Dev")
    print("App arcitectures:")
    print(archdata)
tab_control.pack(expand=0, fill="both")

#Show DEV stuff
PiWareVersionFile = open(f"/home/{username}/.local/share/pi-ware/version", "r")
PiWareVersioncontent = PiWareVersionFile.read()

files = folders = 0
for _, dirnames, filenames in os.walk(f"/home/{username}/pi-ware/apps"):
    files += len(filenames)
    folders += len(dirnames)
    InstallibleApps = "{:,} installible Apps".format(folders)

PiWareVersion = Label(DEV_tab, text=f"Pi-Ware Version:\n{PiWareVersioncontent}", font="Arial 11 bold")
PiWareInstallableApps = Label(DEV_tab, text=f"{InstallibleApps}", font="Arial 11 bold")
PiWareAppAARCH = Label(DEV_tab, text=f"{archdata}", font="Arial 11 bold")
PiWareInstallableApps.configure(anchor="center")
PiWareVersion.pack()
PiWareInstallableApps.pack()
#PiWareAppAARCH.pack()

#Show latest news message
NewsMessagefile = open(f"/home/{username}/pi-ware/func/info/latestnewsmessage", "r")
NewsMessagecontent = NewsMessagefile.read()
NewsMessage = Label(news_tab, text=f"Latest news:\n{NewsMessagecontent}", font="Arial 11 bold")
NewsMessage.config(justify=tk.CENTER)
NewsMessage.pack()

#Show info message
InfoMessagefile = open(f"/home/{username}/pi-ware/func/info/infomessage", "r")
InfoMessagecontent = InfoMessagefile.read()
InfoMessage = Label(credits_tab, text=f"{InfoMessagecontent}", font="Arial 11 bold")
InfoMessage.config(justify=tk.CENTER)
InfoMessage.pack()

#Show commit links
commitmessage = Label(credits_tab, text=f"To see commits, please go to the link below.", font="Arial 11 bold")
commitmessage.config(justify=tk.CENTER)
commitmessage.pack()

commit = Label(credits_tab, text="https://github.com/piware14/pi-ware/graphs/contributors",font=('Arial', 9), cursor="hand2")
s.configure(commit, foreground='blue')
commit.pack()
commit.bind("<Button-1>", lambda e:
callback("https://github.com/piware14/pi-ware/graphs/contributors"))

#Add pi-ware website
piwarewebsite = Label(credits_tab, text=f"To vist the pi-ware website, click the link below.", font="Arial 11 bold")
piwarewebsite.config(justify=tk.CENTER)
piwarewebsite.pack()
Website = Label(credits_tab, text="https://pi-ware.ml",font=('Arial', 9), cursor="hand2")
s.configure(Website, foreground='blue')
Website.pack()
Website.bind("<Button-1>", lambda e:
callback("https://pi-ware.ml"))

tree = Treeview(apps_tab)
vsb = Scrollbar(window, orient="vertical", command=tree.yview)
tree.pack(expand=YES, fill=BOTH)
tree.column("#0", minwidth=0, width=350, stretch=True)
s.configure('Treeview', rowheight=35)
s.map('Treeview', foreground = [('active', '!disabled', 'green')],
                     background = [('active', 'black')])
ap = next(os.walk(f"/home/{username}/pi-ware/apps"))[1]
applist = sorted(ap)
print("Current apps:\n")

os.chdir(r'/home/'+username+'/.local/share/pi-ware')
prechangedata = open('installedapps.json', 'r')
installdata = json.load(prechangedata)

for app in applist:
    print(app)
    installed = False
    if app in installdata:
        if installdata[app] == "Installed":
            installed = True
    print(installed)
    check = ""
    if installed:
        check = " ✔"
    appb = ""
    for a in app:
        if(a == " "):
            appb += "_"
        else:
            appb += a
    #tree.bind("<Button-1>", print(app))
    tree.bind("<ButtonRelease-1>", partial(show_desc,app))
    if istherefile(f'/home/{username}/pi-ware/apps/{app}/icon.png'):
        aico = f'/home/{username}/pi-ware/apps/{app}/icon.png'
    else:
        aico = f'/home/{username}/pi-ware/icons/app-no-icon.png'
        print("/////////////////////////")
    #print(f"{appb}_button =  PhotoImage(file=f'{aico}')")
    exec(f"{appb}_button =  PhotoImage(file=f'{aico}')")
    exec("""tree.insert('', 'end', text=f"{app}{check}",image=""" + appb + """_button)""")

vsb.place(x=310, y=60, height=380)
tree.configure(yscrollcommand=vsb.set)
if (tabtext != "Apps"):
    vsb.place_forget()
ScrollForMore = Label(apps_tab, text="Scroll down for more apps.", font="Arial 11 bold")
ScrollForMore.pack()
quitbutton = Button(window, text="Quit", width=200, style="goback.TButton", command=quit)
s.configure("goback.TButton", foreground='grey', background='grey', font=("Arial", 11))
quitbutton.pack(side="bottom")

window.mainloop()
