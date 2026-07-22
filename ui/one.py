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
            update_popup.title("List of available updates.")
            update_popup.geometry("550x500")
            update_popup.attributes("-topmost", True)
            transparent_color = "#000001"
            update_popup.attributes("-alpha", 0.7)
            update_popup.attributes("-transparentcolor", transparent_color)
            update_popup.configure(fg_color=transparent_color)
            def exitup():
                update_popup.destroy()
            overlayframeup = ctk.CTkFrame(update_popup, corner_radius=25)
            overlayframeup.pack()
            closeup = ctk.CTkButton(overlayframeup, text="", fg_color="white", hover_color="gray", width=8, height=8, corner_radius=4, command=lambda:exitup())
            closeup.place(relx=1.0, rely=0.0, x=-12, y=12, anchor="ne")
            avail = ctk.CTkLabel(overlayframeup, text="Available updates", font=("Arial", 16, "bold"), text_color="white")
            avail.pack(pady=2)
            list_frame = ctk.CTkScrollableFrame(overlayframeup, fg_color="transparent", corner_radius=25)
            list_frame.pack(padx=7, pady=0, fill="both", expand=True)
            for name in names:
                lbl = ctk.CTkLabel(list_frame, text=name, anchor="w", font=("Arial", 12, "bold"))
                lbl.pack(padx=10, pady=5, fill="x")
            
    
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
