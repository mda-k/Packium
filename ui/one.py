#imports
import customtkinter as ctk
import tkinter as tk
from PIL import Image
from pathlib import Path
from tkinter import messagebox
import sys
import time
import threading


#directories
currentdir = Path(__file__).resolve().parent
print(currentdir)	#ui
rootdir = currentdir.parent
print(rootdir)		#root
resourcesdir = rootdir  / "resources"
print(resourcesdir)
functionsdir = rootdir / "functions"
print(functionsdir)
if str(rootdir) not in sys.path:
    sys.path.insert(0, str(rootdir))
if str(currentdir) not in sys.path:
    sys.path.insert(0, str(currentdir))
if str(resourcesdir) not in sys.path:
    sys.path.insert(0, str(resourcesdir))
if str(functionsdir) not in sys.path:
    sys.path.insert(0, str(functionsdir))
    
    
#functions
from update import *
from about import *
from discordinvite import *

def mainui():
    app = ctk.CTk() #basic ctk
    app.geometry("300x200")
    app.overrideredirect(True)
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("dark-blue")
    def FUCKMYLIFE(): #exit
        app.destroy()
        app.quit()
    app.protocol("WM_DELETE_WINDOW", FUCKMYLIFE)
    app.title("Packium")
    app.attributes("-topmost", True)
    transparent_color = "#000001"
    app.attributes("-alpha", 0.7)
    app.attributes("-transparentcolor", transparent_color)
    app.configure(fg_color=transparent_color)
    
    
    #appearance variables
    buttoncolor = "#3b3b3b"
    buttoncolor_hover = "#787878"
    replacementicon_color = "#3b3b3b"
    replacementicon512 = Image.new("RGB", (512, 512), color=replacementicon_color)
    
    
    #icon
    appicon = resourcesdir / "icon.ico"
    try:
        app.iconbitmap(appicon)
    except Exception:
        messagebox.showerror("Error!", "Packium was not able to open and/or was not able to find /resources/icon.ico.")
        appicon = Image.new("RGB", (32, 32), color=replacementicon_color)
        
    #rounded corner frame
    overlayframe = ctk.CTkFrame(app, corner_radius=25)
    overlayframe.pack(fill="both", expand=True, padx=2, pady=2)
    close = ctk.CTkButton(overlayframe, text="", fg_color="white", hover_color="gray", width=8, height=8, corner_radius=4, command=lambda:FUCKMYLIFE())
    close.place(relx=1.0, rely=0.0, x=-12, y=12, anchor="ne")
    name = ctk.CTkLabel(overlayframe, text="Packium", fg_color="transparent", font=("Arial", 16, "bold"), text_color="white")
    name.pack(side="top", pady=(2, 0))
    optionsframe = ctk.CTkFrame(overlayframe, corner_radius=25, fg_color="transparent")
    optionsframe.pack()
    
    
    #button functions
    
    def updatebutton_pressed():
        print("update button pressed.")
        updatebutton.configure(state="disabled")
        messagebox.showinfo("Notice", "Winget may or may not reinstall the program to it's original path. I haven't been able to figure out how it's possible to force Winget to keep the updated program at it's original path, especially if some vendors just do not accept Winget's --location parameter. Before using the program's update feature, you should know, that some programs might be moved to the C: drive, the vendor's hardcoded/default installation path.")
        def fetchupdates():
            name_id_dict = winget_update()
            app.after(0, lambda: onfetchedupdates(name_id_dict))
        
        threading.Thread(target=fetchupdates, daemon=True).start()
        def onfetchedupdates(name_id_dict):
            names = list(name_id_dict.keys())
            ids = list(name_id_dict.values())
            if names and ids:
                print("one.py got the names from update.py!")
                print(f"got: {names}")
                print("one got the ids from update.py!")
                print(f"got: {ids}")
                update_popup = ctk.CTkToplevel(app)
                update_popup.overrideredirect(True)
                update_popup.title("Updates")
                update_popup.geometry("400x400")
                update_popup.attributes("-topmost", True)
                transparent_color = "#000001"
                update_popup.attributes("-alpha", 0.7)
                update_popup.attributes("-transparentcolor", transparent_color)
                update_popup.configure(fg_color=transparent_color)
                update_popup.grab_set()
                update_popup.focus_set()
                appicon = resourcesdir / "icon.ico"
                try:
                    update_popup.after(200, lambda: update_popup.iconbitmap(appicon))
                except Exception:
                    messagebox.showerror("Error", "Packium was not able to open and/or was not able to find /resources/icon.ico.")
                    appicon = Image.new("RGB", (32, 32), color=replacementicon_color)
                def startmove(event):
                    update_popup.x = event.x
                    update_popup.y = event.y
                def move(event):
                    deltax = event.x - update_popup.x
                    deltay = event.y - update_popup.y
                    x = update_popup.winfo_x() + deltax
                    y = update_popup.winfo_y() + deltay
                    update_popup.geometry(f"+{x}+{y}")
                def exitup():
                    updatebutton.configure(state="normal")
                    update_popup.destroy()
                overlayframeup = ctk.CTkFrame(update_popup, corner_radius=25)
                overlayframeup.pack(fill="both", expand=True)
                overlayframeup.bind("<Button-1>", startmove)
                overlayframeup.bind("<B1-Motion>", move)
                closeup = ctk.CTkButton(overlayframeup, text="", fg_color="white", hover_color="gray", width=8, height=8, corner_radius=4, command=lambda:exitup())
                closeup.place(relx=1.0, rely=0.0, x=-12, y=12, anchor="ne")
                avail = ctk.CTkLabel(overlayframeup, text="Available updates", font=("Arial", 16, "bold"), text_color="white")
                avail.pack(pady=2)
                avail.bind("<Button-1>", startmove)
                avail.bind("<B1-Motion>", move)
                list_frame = ctk.CTkScrollableFrame(overlayframeup, fg_color="transparent", corner_radius=25)
                list_frame.pack(padx=8, pady=0, fill="both", expand=True)
                list_frame.bind("<Button-1>", startmove)
                list_frame.bind("<B1-Motion>", move)
                checkboxes = {}
                for name in names:
                    item = ctk.CTkCheckBox(list_frame, text=name, font=("Arial", 12, "bold"), checkbox_width=20, checkbox_height=20, corner_radius=6)
                    item.pack(padx=10, pady=5, fill="x", anchor="w")
                    checkboxes[name] = item
                def getchecked():
                    selectedids = []
                    selected = [name for name, item in checkboxes.items() if item.get() ==1]
                    if not selected:
                        messagebox.showerror("Error!", "You don't have any items chosen. Either close the window, or choose an item or more to continue.")
                    for selecteditem in selected:
                        print(f"Selected update: {selecteditem}")
                    
                        selectedids.append(name_id_dict[(selecteditem)])
                        print(f"added id to the list. the list: {selectedids}")
                        messagebox.showinfo("Notice", "You have pressed the continue button. Packium may or may not freeze for as long as the updates last, since the script is waiting for the subprocess to be done. Please do not kill or interfere with Packium.")
                        messagebox.showinfo("Notice", "A command prompt window will open, so you can see where the update process is standing.")
                    if selectedids:
                        continuebuttonup.configure(state="disabled", text="Working...")
                        def afterrunupdatethread():
                            
                            print(f"the update is done.")
                            messagebox.showinfo("Task done!", "All the selected programs have been updated!")
                            updatebutton.configure(state="normal")
                            update_popup.destroy()
                        def runupdatethread():
                            cmd = ["winget", "upgrade", *selectedids]
                            subprocess.run(cmd, creationflags=subprocess.CREATE_NEW_CONSOLE)
                            time.sleep(1)
                            app.after(0, lambda: afterrunupdatethread())
                        threading.Thread(target=runupdatethread, daemon=True).start()
                        
                continuebuttonup = ctk.CTkButton(overlayframeup, text="Continue", font=("Arial", 14, "bold"), fg_color=buttoncolor, hover_color=buttoncolor_hover, width=40, height=20, corner_radius=20, command=lambda:getchecked())
                continuebuttonup.pack(pady=10)
            
    def startmove(event):
        app.x = event.x
        app.y = event.y
    def move(event):
        deltax = event.x - app.x
        deltay = event.y - app.y
        x = app.winfo_x() + deltax
        y = app.winfo_y() + deltay
        app.geometry(f"+{x}+{y}")
    overlayframe.bind("<Button-1>", startmove)
    overlayframe.bind("<B1-Motion>", move)
    name.bind("<Button-1>", startmove)
    name.bind("<B1-Motion>", move)
    optionsframe.bind("<Button-1>", startmove)
    optionsframe.bind("<B1-Motion>", move)
    
    #buttons
    updateicon_path = resourcesdir / "update.png"
    print(updateicon_path)
    try:
        updateiconimg = Image.open(updateicon_path)
    except FileNotFoundError:
        updateiconimg = replacementicon512
        messagebox.showerror("Error!", "Packium was not able to open and/or was not able to find /resources/update.png.")
    updateicon = ctk.CTkImage(light_image=updateiconimg, dark_image=updateiconimg, size=(40, 40))
    updatebutton = ctk.CTkButton(optionsframe, text="", image=updateicon, width=60, height=60, fg_color=buttoncolor, hover_color=buttoncolor_hover, command=lambda:updatebutton_pressed())
    updatebutton.grid(row=0, column=0, padx=10, pady=10)

    downloadicon_path = resourcesdir / "download.png"
    try:
        downloadiconimg = Image.open(downloadicon_path)
    except FileNotFoundError:
        messagebox.showerror("Error!", "Packium was not able to open and/or was not able to find /resources/download.png.")
        downloadiconimg = replacementicon512
    downloadicon = ctk.CTkImage(light_image=downloadiconimg, dark_image=downloadiconimg, size=(40, 40))
    downloadbutton = ctk.CTkButton(optionsframe, text="", image=downloadicon, width=60, height=60, fg_color=buttoncolor, hover_color=buttoncolor_hover)
    downloadbutton.grid(row=0, column=1, padx=10, pady=10)
        
        
    uninstallicon_path = resourcesdir / "uninstall.png"
    try:
        uninstalliconimg = Image.open(uninstallicon_path)
    except FileNotFoundError:
        messagebox.showerror("Error!", "Packium was not able to open and/or was not able to find /resources/uninstall.png.")
        uninstalliconimg = replacementicon512
    uninstallicon =  ctk.CTkImage(light_image=uninstalliconimg, dark_image=uninstalliconimg, size=(40, 40))
    uninstallbutton = ctk.CTkButton(optionsframe, text="", image=uninstallicon, width=60, height=60, fg_color=buttoncolor, hover_color=buttoncolor_hover)
    uninstallbutton.grid(row=0, column=2, padx=10, pady=10)
    
    
    
        
        
        
    def discordbuttonclicked():
        discordinvite()
        print("discord invite")
    discordicon_path = resourcesdir / "discord.png"
    try:
        discordiconimg = Image.open(discordicon_path)
    except FileNotFoundError:
        messagebox.showerror("Error!", "Packium was not able to open and/or was not able to find /resources/discord.png.")
        discordiconimg = replacementicon512
    discordicon = ctk.CTkImage(light_image=discordiconimg, dark_image=discordiconimg, size=(40, 40))
    discordbutton = ctk.CTkButton(optionsframe, text="", image=discordicon, width=60, height=60, fg_color=buttoncolor, hover_color=buttoncolor_hover, command=lambda:discordbuttonclicked())
    discordbutton.grid(row=1, column=1, padx=10, pady=10)
    
    
    
    
    
    settingsicon_path = resourcesdir / "settings.png"
    try:
        settingsiconimg = Image.open(settingsicon_path)
    except FileNotFoundError:
        messagebox.showerror("Error!", "Packium was not able to open and/or was not able to find /resources/settings.png.")
        settingsiconimg = replacementicon512
    settingsicon = ctk.CTkImage(light_image=settingsiconimg, dark_image=settingsiconimg, size=(40, 40))
    settingsbutton = ctk.CTkButton(optionsframe, text="", image=settingsicon, width=60, height=60, fg_color=buttoncolor, hover_color=buttoncolor_hover)
    settingsbutton.grid(row=1, column=0, padx=10, pady=10)
    abouticon_path = resourcesdir / "about.png"
    try:
        abouticonimg = Image.open(abouticon_path)
    except FileNotFoundError:
        messagebox.showerror("Error!", "Packium was not able to open and/or was not able to find /resources/about.png")
        abouticonimg = replacementicon512
    abouticon = ctk.CTkImage(light_image=abouticonimg, dark_image=abouticonimg, size=(40, 40))
    aboutbutton = ctk.CTkButton(optionsframe, text="", image=abouticon, width=60, height=60, fg_color=buttoncolor, hover_color=buttoncolor_hover)
    aboutbutton.grid(row=1, column=2, padx=10, pady=10)
    
    
    #hoverfuncs
    timerid = None
    sizeidxub = 40
    currentsize = sizeidxub
    sizeidxubh = 44
    def hoveran(tidxub):
        nonlocal timerid, sizeidxub, sizeidxubh, currentsize
        if currentsize == tidxub:
            timerid = None
            return
        if currentsize < tidxub:
            currentsize += 1
        else:
            currentsize -= 1
        try:
            updateicon.configure(size=(currentsize, currentsize))
        except Exception:
            pass
        timerid = updatebutton.after(20, hoveran, tidxub)
    def hoverupdate(event=None ):
        nonlocal timerid
        if timerid is not None:
            updatebutton.after_cancel(timerid)
            timerid = None
        hoveran(sizeidxubh)
    def hoverupdateleave(event=None):
        nonlocal timerid
        if timerid is not None:
            updatebutton.after_cancel(timerid)
            timerid = None
        hoveran(sizeidxub)
        updateicon.configure(size=(sizeidxub, sizeidxub))
    updatebutton.bind("<Enter>", hoverupdate)
    updatebutton.bind("<Leave>", hoverupdateleave)
    
    timeriddb = None
    sizeidxdb = 40
    currentsize = sizeidxdb
    sizeidxdbh = 44
    def hoverand(tidxdb):
        nonlocal timeriddb, sizeidxdb, sizeidxdbh, currentsize
        if currentsize == tidxdb:
            timeriddb = None
            return
        if currentsize < tidxdb:
            currentsize += 1
        else:
            currentsize -= 1
        try:
            downloadicon.configure(size=(currentsize, currentsize))
        except Exception:
            pass
        timeriddb = downloadbutton.after(20, hoverand, tidxdb)
    def hoverupdated(event=None ):
        nonlocal timeriddb
        if timeriddb is not None:
            downloadbutton.after_cancel(timeriddb)
            timeriddb = None
        hoverand(sizeidxdbh)
    def hoverupdateleaved(event=None):
        nonlocal timeriddb
        if timeriddb is not None:
            downloadbutton.after_cancel(timeriddb)
            timeriddb = None
        hoverand(sizeidxdb)
        downloadicon.configure(size=(sizeidxdb, sizeidxdb))
    downloadbutton.bind("<Enter>", hoverupdated)
    downloadbutton.bind("<Leave>", hoverupdateleaved)
    
    timeriduib = None
    sizeidxuib = 40
    currentsize = sizeidxuib
    sizeidxuibh = 44
    def hoveranui(tidxuib):
        nonlocal timeriduib, sizeidxuib, sizeidxuibh, currentsize
        if currentsize == tidxuib:
            timeriduib = None
            return
        if currentsize < tidxuib:
            currentsize += 1
        else:
            currentsize -= 1
        try:
            uninstallicon.configure(size=(currentsize, currentsize))
        except Exception:
            pass
        timeriduib = uninstallbutton.after(20, hoveranui, tidxuib)
    def hoverupdateui(event=None ):
        nonlocal timeriduib
        if timeriduib is not None:
            uninstallbutton.after_cancel(timeriduib)
            timeriduib = None
        hoveranui(sizeidxuibh)
    def hoverupdateleaveui(event=None):
        nonlocal timeriduib
        if timeriduib is not None:
            uninstallbutton.after_cancel(timeriduib)
            timeriduib = None
        hoveranui(sizeidxuib)
        uninstallicon.configure(size=(sizeidxuib, sizeidxuib))
    uninstallbutton.bind("<Enter>", hoverupdateui)
    uninstallbutton.bind("<Leave>", hoverupdateleaveui)
    
    
    timeriddib = None
    sizeidxdib = 40
    currentsize = sizeidxdib
    sizeidxdibh = 44
    def hoverandi(tidxdib):
        nonlocal timeriddib, sizeidxdib, sizeidxdibh, currentsize
        if currentsize == tidxdib:
            timeriddib = None
            return
        if currentsize < tidxdib:
            currentsize += 1
        else:
            currentsize -= 1
        try:
            discordicon.configure(size=(currentsize, currentsize))
        except Exception:
            pass
        timeriddib = discordbutton.after(20, hoverandi, tidxdib)
    def hoverupdatedi(event=None ):
        nonlocal timeriddib
        if timeriddib is not None:
            discordbutton.after_cancel(timeriddib)
            timeriddib = None
        hoverandi(sizeidxdibh)
    def hoverupdateleavedi(event=None):
        nonlocal timeriddib
        if timeriddib is not None:
            discordbutton.after_cancel(timeriddib)
            timeriddib = None
        hoverandi(sizeidxdib)
        discordicon.configure(size=(sizeidxdib, sizeidxdib))
    discordbutton.bind("<Enter>", hoverupdatedi)
    discordbutton.bind("<Leave>", hoverupdateleavedi)
    
    app.mainloop()
