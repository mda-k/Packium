#imports
import customtkinter as ctk
import tkinter as tk
from PIL import Image
from pathlib import Path
from tkinter import messagebox
import sys


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


def mainui():
    app = ctk.CTk() #basic ctk
    app.geometry("300x200")
    app.overrideredirect(True)
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("dark-blue")
    def FUCKMYLIFE(): #exit
        app.destroy()
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
        names = winget_update()
        if names:
            print("one.py got the names from update.py!")
            print("got:")
            update_popup = ctk.CTkToplevel(app)
            update_popup.overrideredirect(True)
            update_popup.title("Updates")
            update_popup.geometry("400x400")
            update_popup.attributes("-topmost", True)
            transparent_color = "#000001"
            update_popup.attributes("-alpha", 0.7)
            update_popup.attributes("-transparentcolor", transparent_color)
            update_popup.configure(fg_color=transparent_color)
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
                selected = [name for name, item in checkboxes.items() if item.get() ==1]
                if not selected:
                    messagebox.showerror("Error!", "You don't have any items chosen. Either close the window, or choose an item or more to continue.")
                for selecteditem in selected:
                    print(f"Selected update: {selecteditem}")
            continuebuttonup = ctk.CTkButton(overlayframeup, text="Continue", font=("Arial", 14, "bold"), fg_color=buttoncolor, hover_color=buttoncolor_hover, width=40, height=20, corner_radius=20, command=lambda:getchecked())
            continuebuttonup.pack()
            
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
    dummybutton1 = ctk.CTkButton(optionsframe, text="", width=60, height=60, fg_color=buttoncolor, hover_color=buttoncolor_hover)
    dummybutton1.grid(row=1, column=0, padx=10, pady=10)
    dummybutton2 = ctk.CTkButton(optionsframe, text="", width=60, height=60, fg_color=buttoncolor, hover_color=buttoncolor_hover)
    dummybutton2.grid(row=1, column=1, padx=10, pady=10)
    abouticon_path = resourcesdir / "about.png"
    try:
        abouticonimg = Image.open(abouticon_path)
    except FileNotFoundError:
        messagebox.showerror("Error!", "Packium was not able to open and/or was not able to find /resources/about.png")
        abouticonimg = replacementicon512
    abouticon = ctk.CTkImage(light_image=abouticonimg, dark_image=abouticonimg, size=(40, 40))
    aboutbutton = ctk.CTkButton(optionsframe, text="", image=abouticon, width=60, height=60, fg_color=buttoncolor, hover_color=buttoncolor_hover)
    aboutbutton.grid(row=1, column=2, padx=10, pady=10)
    app.mainloop()
