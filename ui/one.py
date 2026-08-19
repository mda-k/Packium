#imports
import customtkinter as ctk
import tkinter as tk
from PIL import Image
from pathlib import Path
from tkinter import messagebox
import sys
import time
import threading
from CTkColorPicker import AskColor
import shutil


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
    #appearance variables
    context = {**globals(), **locals()}
    sizeidxb = 5
    sizeidxbh = 5
    optionspath = currentdir / "options.packium"
    defaultoptionspath = currentdir / "default.packium"
    with open(optionspath, "r", encoding="utf-8") as optionsfile:
        for line in optionsfile:
            line.strip()
            print(line)
            if "=" in line:
                print(f"found =: {line}")
                exec(line, context)
    buttoncolor = context.get("buttoncolor")
    bttoncolor_hover = context.get("bttoncolor_hover")
    iconpack = context.get("iconpack")
    replacementicon_color = context.get("replacementicon_color")
    replacementicon512 = context.get("replacementicon512")
    replacementiconapp = context.get("replacementiconapp")
    sizeidxb = context.get("sizeidxb", sizeidxb)
    sizeidxbh = context.get("sizeidxbh", sizeidxbh)
    maingeometry = context.get("maingeometry")
    appearancemode = context.get("appearancemode")
    defaultcolortheme = context.get("defaultcolortheme")
    wopacity = context.get("wopacity")
    
    print(f"button color: {buttoncolor}") #color of the buttons
    print(f"hover button color: {bttoncolor_hover}") #color of the button when hovered over
    print(f"icon pack set that Packium is using: {iconpack}") 
    print(f"replacement icon color: {replacementicon_color}")#color of the replacement icons
    print(f"replacement icon 512x512 for the buttons: {replacementicon512}") #replacement icon for buttons.
    print(f"replacement icon for the program: {replacementiconapp}") #the replacement icon of the app itself
    print(f"size of the icons: {sizeidxb}") #the normal size of the icons
    print(f"size of the icons when hovered over: {sizeidxbh}") #hover size of the icons
    print(f"main packium window geometry: {maingeometry}") #geometry of the main packium window...
    print(f"appearance mode is: {appearancemode}") #theme, light or dark, blah blah
    print(f"default color theme is: {defaultcolortheme}") #color theme
    print(f"opacity of the program is: {wopacity}") #opacity of the windows
    
    
    app = ctk.CTk()
    app.geometry(maingeometry)
    app.overrideredirect(True)
    ctk.set_appearance_mode(appearancemode)
    ctk.set_default_color_theme(defaultcolortheme)
    def FUCKMYLIFE(): #exit
        app.destroy()
        app.quit()
    app.protocol("WM_DELETE_WINDOW", FUCKMYLIFE)
    def normalstatebuttons():
        updatebutton.configure(state="normal")
        downloadbutton.configure(state="normal")
        uninstallbutton.configure(state="normal")
        settingsbutton.configure(state="normal")
        discordbutton.configure(state="normal")
        aboutbutton.configure(state="normal")
    def disabledstatebuttons():
        updatebutton.configure(state="disabled")
        downloadbutton.configure(state="disabled")
        uninstallbutton.configure(state="disabled")
        settingsbutton.configure(state="disabled")
        discordbutton.configure(state="disabled")
        aboutbutton.configure(state="disabled")
    app.title("Packium")
    app.attributes("-topmost", True)
    transparent_color = "#000001"
    app.attributes("-alpha", wopacity)
    app.attributes("-transparentcolor", transparent_color)
    app.configure(fg_color=transparent_color)
    
    #icon
    appicon = resourcesdir / "icon.ico"
    try:
        app.iconbitmap(appicon)
    except Exception:
        messagebox.showerror("Error!", "Packium was not able to open and/or was not able to find /resources/icon.ico.")
        appicon = replacementiconapp
        
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
        disabledstatebuttons()
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
                update_popup.attributes("-alpha", wopacity)
                update_popup.attributes("-transparentcolor", transparent_color)
                update_popup.configure(fg_color=transparent_color)
                update_popup.grab_set()
                update_popup.focus_set()
                appicon = resourcesdir / "icon.ico"
                try:
                    update_popup.after(200, lambda: update_popup.iconbitmap(appicon))
                except Exception:
                    messagebox.showerror("Error", "Packium was not able to open and/or was not able to find /resources/icon.ico.")
                    appicon = replacementiconapp
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
                    normalstatebuttons()
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
                       
                    if selectedids:
                        messagebox.showinfo("Notice", "You have pressed the continue button. Packium may or may not freeze for as long as the updates last, since the script is waiting for the subprocess to be done. Please do not kill or interfere with Packium.")
                        messagebox.showinfo("Notice", "A command prompt window will open, so you can see where the update process is standing.")
                        continuebuttonup.configure(state="disabled", text="Working...")
                        def afterrunupdatethread():
                            
                            print(f"the update is done.")
                            messagebox.showinfo("Task done!", "All the selected programs have been updated!")
                            normalstatebuttons()
                            update_popup.destroy()
                        def runupdatethread():
                            cmd = ["winget", "upgrade", *selectedids]
                            subprocess.run(cmd, creationflags=subprocess.CREATE_NEW_CONSOLE)
                            time.sleep(1)
                            app.after(0, lambda: afterrunupdatethread())
                        threading.Thread(target=runupdatethread, daemon=True).start()
                        
                continuebuttonup = ctk.CTkButton(overlayframeup, text="Continue", font=("Arial", 14, "bold"), fg_color=buttoncolor, hover_color=bttoncolor_hover, width=40, height=20, corner_radius=20, command=lambda:getchecked())
                continuebuttonup.pack(pady=10)
    def settingsbuttonpressed():
        print("settings button pressed.")
        disabledstatebuttons()
        settings_popup = ctk.CTkToplevel(app)
        settings_popup.overrideredirect(True)
        settings_popup.title("Settings")
        settings_popup.geometry("400x500")
        settings_popup.attributes("-topmost", True)
        transparent_color = "#000001"
        settings_popup.attributes("-alpha", wopacity)
        settings_popup.attributes("-transparentcolor", transparent_color)
        settings_popup.configure(fg_color=transparent_color)
        settings_popup.grab_set()
        settings_popup.focus_set()
        appicon = resourcesdir / "icon.ico"
        try:
            settings_popup.after(200, lambda: settings_popup.iconbitmap(appicon))
        except Exception:
            messagebox.showerror("Error", "Packium was not able to open and/or was not able to find /resources/icon.ico.")
            appicon = replacementiconapp
        def startmove(event):
            settings_popup.x = event.x
            settings_popup.y = event.y
        def move(event):
            deltax = event.x - settings_popup.x
            deltay = event.y - settings_popup.y
            x = settings_popup.winfo_x() + deltax
            y = settings_popup.winfo_y() + deltay
            settings_popup.geometry(f"+{x}+{y}")
        def enterdangerzone(event=None):
            dangerzoneframe.configure(fg_color="#320504")
        def leavedangerzone(event=None):
            dangerzoneframe.configure(fg_color="#191919")
        def enterdangerzoneresetbutton(event=None): #i know i can use hover_color= blah blah, but because of the new bindings, i do have to use this..
            dangerzoneframe.configure(fg_color="#320504")
            resetbutton.configure(fg_color="#a31c1c")
        def leavedangerzoneresetbutton(event=None):
            dangerzoneframe.configure(fg_color="#191919")
            resetbutton.configure(fg_color=buttoncolor)
        def exitsb():
            normalstatebuttons()
            settings_popup.destroy()
        overlayframesb = ctk.CTkFrame(settings_popup, corner_radius=25)
        overlayframesb.pack(fill="both", expand=True)
        overlayframesb.bind("<Button-1>", startmove)
        overlayframesb.bind("<B1-Motion>", move)
        closesb = ctk.CTkButton(overlayframesb, text="", fg_color="white", hover_color="gray", width=8, height=8, corner_radius=4, command=lambda:exitsb())
        closesb.place(relx=1.0, rely=0.0, x=-12, y=12, anchor="ne")
        settingslabel = ctk.CTkLabel(overlayframesb, text="Settings", font=("Arial", 16, "bold"), text_color="white")
        settingslabel.pack()
        settingslabel.bind("<Button-1>", startmove)
        settingslabel.bind("<B1-Motion>", move)
        
        overlayframesbscrollable = ctk.CTkScrollableFrame(settings_popup, corner_radius=25)
        
        
        generalfieldframe = ctk.CTkFrame(overlayframesb, corner_radius=10, fg_color="#191919")
        generalfieldframe.pack(fill="x", expand=False, pady=(0, 10), padx=20)
        generalfieldframelabel = ctk.CTkLabel(generalfieldframe, text="General settings", font=("Arial", 16, "bold"), text_color="white")
        generalfieldframelabel.pack()
        appthemefieldlabel = ctk.CTkLabel(generalfieldframe, text="The theme of Packium:", font=("Arial", 16), text_color="white")
        appthemefieldlabel.pack(anchor="w", padx=10, pady=(0, 0))
        appthemeoptions = ["Light", "Dark", "System"]
        appthemefield = ctk.CTkOptionMenu(generalfieldframe, values=appthemeoptions, dynamic_resizing=False, fg_color=buttoncolor, corner_radius=20)
        appthemefield.set(appearancemode)
        appthemefield.pack(anchor="w", padx=10, pady=(0, 10))
        iconpackfieldlabel = ctk.CTkLabel(generalfieldframe, text="The icon pack that Packium uses:", font=("Arial", 16), text_color="white")
        iconpackfieldlabel.pack(anchor="w", padx=10, pady=(0, 0))
        iconpackoptions = ["Light", "Dark"]
        iconpackfield = ctk.CTkOptionMenu(generalfieldframe, values=iconpackoptions, dynamic_resizing=False, fg_color=buttoncolor, corner_radius=20)
        iconpackfield.set(iconpack)
        iconpackfield.pack(anchor="w", padx=10, pady=(0, 10))
        generalfieldframe.bind("<Button-1>", startmove)
        generalfieldframe.bind("<B1-Motion>", move)
        generalfieldframelabel.bind("<Button-1>", startmove)
        generalfieldframelabel.bind("<B1-Motion>", move)
        appthemefieldlabel.bind("<Button-1>", startmove)
        appthemefieldlabel.bind("<B1-Motion>", move)



        buttonfieldframe = ctk.CTkFrame(overlayframesb, corner_radius=10, fg_color="#191919")
        buttonfieldframe.pack(fill="x", expand=False, pady=(0, 10), padx=20)
        buttonfieldframelabel = ctk.CTkLabel(buttonfieldframe, text="Settings related to buttons", font=("Arial", 16, "bold"), text_color="white")
        buttonfieldframelabel.pack()
        buttoncolorfieldlabel = ctk.CTkLabel(buttonfieldframe, text="Color of the buttons:", font=("Arial", 16), text_color="white")
        buttoncolorfieldlabel.pack(anchor="w", padx=10, pady=(0, 0))
        buttoncolorfield = ctk.CTkButton(buttonfieldframe, text=buttoncolor, font=("Arial", 16), fg_color=buttoncolor, hover_color=bttoncolor_hover, width=40, height=20, corner_radius=20, command=lambda:pickbuttoncolor())
        buttoncolorfield.pack(anchor="w", padx=10, pady=(0, 10))
        
        buttonhovercolorfieldlabel = ctk.CTkLabel(buttonfieldframe, text="Color of the buttons when hovered over:", font=("Arial", 16), text_color="white")
        buttonhovercolorfieldlabel.pack(anchor="w", padx=10, pady=(0, 0))
        buttonhovercolorfield = ctk.CTkButton(buttonfieldframe, text=bttoncolor_hover, font=("Arial", 16), fg_color=bttoncolor_hover, hover_color=bttoncolor_hover, width=40, height=20, corner_radius=20, command=lambda:pickbuttoncolorhover())
        buttonhovercolorfield.pack(anchor="w", padx=10, pady=(0, 10))
        buttonfieldframe.bind("<Button-1>", startmove)
        buttonfieldframe.bind("<B1-Motion>", move)
        buttonfieldframelabel.bind("<Button-1>", startmove)
        buttonfieldframelabel.bind("<B1-Motion>", move)
        buttoncolorfieldlabel.bind("<Button-1>", startmove)
        buttoncolorfieldlabel.bind("<B1-Motion>", move)
        buttonhovercolorfieldlabel.bind("<Button-1>", startmove)
        buttonhovercolorfieldlabel.bind("<B1-Motion>", move)
        
        
        dangerzoneframe = ctk.CTkFrame(overlayframesb, corner_radius=10, fg_color="#191919")
        dangerzoneframe.pack(fill="x", expand=False, pady=(0, 10), padx=20)
        dangerzoneframelabel = ctk.CTkLabel(dangerzoneframe, text="Danger zone", font=("Arial", 16, "bold"), text_color="white")
        dangerzoneframelabel.pack()
        resetbutton = ctk.CTkButton(dangerzoneframe, text="set settings back to default", font=("Arial", 16), fg_color=buttoncolor, width=40, height=20, corner_radius=20, command=lambda:resetsettings())
        resetbutton.pack(pady=(0, 10))
        dangerzoneframe.bind("<Button-1>", startmove)
        dangerzoneframe.bind("<B1-Motion>", move)
        dangerzoneframelabel.bind("<Button-1>", startmove)
        dangerzoneframelabel.bind("<B1-Motion>", move)
        dangerzoneframe.bind("<Enter>", enterdangerzone)
        dangerzoneframe.bind("<Leave>", leavedangerzone)
        dangerzoneframelabel.bind("<Enter>", enterdangerzone)
        dangerzoneframelabel.bind("<Leave>", leavedangerzone)
        resetbutton.bind("<Enter>", enterdangerzoneresetbutton)
        resetbutton.bind("<Leave>", leavedangerzoneresetbutton)
        
        applybutton = ctk.CTkButton(overlayframesb, text="Apply", font=("Arial", 16, "bold"), fg_color=buttoncolor, hover_color=bttoncolor_hover, width=40, height=20, corner_radius=20, command=lambda:applysettings())
        applybutton.place(relx=1.0, rely=1.0, x=-12, y=-12, anchor="se")
        cancelbutton = ctk.CTkButton(overlayframesb, text="Cancel", font=("Arial", 16, "bold"), fg_color=buttoncolor, hover_color=bttoncolor_hover, width=40, height=20, corner_radius=20, command=lambda:cancelsettings())
        cancelbutton.place(relx=0.0, rely=1.0, x=12, y=-12, anchor="sw")
        buttoncolor_TEMP = None
        bttoncolor_hover_TEMP = None
        def resetsettings():
            confirmreset = messagebox.askyesno("Are you sure?", "Are you sure you want to reset your Packium appearance settings?")
            if confirmreset:
                print("user confirmed.")
                shutil.copyfile(defaultoptionspath, optionspath)
                print("settings have been set to the default!")
                messagebox.showinfo("Notice", "Settings have been set to the default!")
                exitsb()
            else:
                print("user changed their mind.")

        def cancelsettings():
            print("cancel settings button pressed.")
            exitsb()
        def pickbuttoncolor():
            print("button color button pressed.")
            nonlocal buttoncolor_TEMP
            buttoncolor_pick = AskColor()
            buttoncolor_TEMP = buttoncolor_pick.get()
            if buttoncolor_TEMP :
                print(f"selected color is {buttoncolor_TEMP}")
                buttoncolorfield.configure(text=buttoncolor_TEMP)
                buttoncolorfield.configure(fg_color=buttoncolor_TEMP)
        def pickbuttoncolorhover():
            print("button hover color button pressed.")
            nonlocal bttoncolor_hover_TEMP
            buttoncolorhover_pick = AskColor()
            bttoncolor_hover_TEMP = buttoncolorhover_pick.get()
            if bttoncolor_hover_TEMP :
                print(f"selected color is {bttoncolor_hover_TEMP}")
                buttonhovercolorfield.configure(text=bttoncolor_hover_TEMP)
                buttonhovercolorfield.configure(fg_color=bttoncolor_hover_TEMP)
        def applysettings():
            buttoncolorchanged = None
            buttonhovercolorchanged = None
            themechanged = None
            iconpackchanged = None
            print("apply settings button pressed.")
            appearancemode_TEMP = appthemefield.get()
            print(appearancemode_TEMP)

            if appearancemode != appearancemode_TEMP:
                themechanged = True
            else:
                themechanged = False
            iconpack_TEMP = iconpackfield.get()
            if iconpack != iconpack_TEMP:
                iconpackchanged = True
            else:
                iconpackchanged = False
            nonlocal buttoncolor_TEMP
            nonlocal bttoncolor_hover_TEMP
            print(f"button color value in settings is: {buttoncolor_TEMP}")
            if buttoncolor_TEMP is not None:
                buttoncolorchanged = True
                print("user changed the color of the buttons, applying that.")
            if buttoncolor_TEMP is None:
                buttoncolorchanged = False
                print("user has not changed the color of the buttons.")
            if bttoncolor_hover_TEMP is not None:
                buttonhovercolorchanged = True
                print("user changed the hover color of the buttons, applying that")
            if bttoncolor_hover_TEMP is None:
                buttonhovercolorchanged = False
                print("user has not changed the hvoer color of the buttons.")
            with open(optionspath, "r", encoding="utf-8") as optionsfilereads:
                olines = optionsfilereads.readlines()
            with open(optionspath, "w", encoding="utf-8") as optionsfilewrite:
                 for line in olines:
                    print(line)
                    if line.startswith("bttoncolor_hover"):
                        if buttonhovercolorchanged == True:
                            optionsfilewrite.write(f'bttoncolor_hover = "{bttoncolor_hover_TEMP}"\n')
                            print("wrote it (bttoncolor_hover)")
                        elif buttonhovercolorchanged == False or buttonhovercolorchanged == None:
                            optionsfilewrite.write(line)
                    elif line.startswith("buttoncolor"):
                        if buttoncolorchanged == True:
                            optionsfilewrite.write(f'buttoncolor = "{buttoncolor_TEMP}"\n')
                            print("wrote it (buttoncolor)")
                        elif buttoncolorchanged == False or buttoncolorchanged == None:
                            optionsfilewrite.write(line)
                    elif line.startswith("appearancemode"):
                        if themechanged == True:
                            optionsfilewrite.write(f'appearancemode = "{appearancemode_TEMP}"\n')
                            print("wrote it (appearancemode/theme)")
                        elif themechanged == False or themechanged == None:
                            optionsfilewrite.write(line)
                    elif line.startswith("iconpack"):
                        if iconpackchanged == True:
                            optionsfilewrite.write(f'iconpack = "{iconpack_TEMP}"\n')
                            print("wrote it (iconpack)")
                        elif iconpackchanged == False or iconpackchanged == None:
                            optionsfilewrite.write(line)
                    else:
                        optionsfilewrite.write(line)
            if buttoncolorchanged == True or buttonhovercolorchanged == True or themechanged == True or iconpackchanged == True:
                messagebox.showinfo("Notice", "To see the changes, you have to restart the program.")
            print("settings applied.")
            exitsb()

                
                
                
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
    packiumiconpackvalueisfucked = None
    updateicon_path_dark = resourcesdir / "updatedark.png"
    updateicon_path = resourcesdir / "update.png"
    print(updateicon_path)
    print(updateicon_path_dark)
    try:
        if iconpack == "Light":
            updateiconimg = Image.open(updateicon_path)
        elif iconpack == "Dark":
            updateiconimg = Image.open(updateicon_path_dark)
        else:
            updateiconimg = replacementicon512
            packiumiconpackvalueisfucked = True
    except FileNotFoundError:
        updateiconimg = replacementicon512
        messagebox.showerror("Error!", "Packium was not able to open and/or was not able to find the update icon (aka /resources/update.png or /resources/updatedark.png).")
    updateicon = ctk.CTkImage(light_image=updateiconimg, dark_image=updateiconimg, size=(sizeidxb, sizeidxb))
    updatebutton = ctk.CTkButton(optionsframe, text="", image=updateicon, width=60, height=60, fg_color=buttoncolor, hover_color=bttoncolor_hover, command=lambda:updatebutton_pressed())
    updatebutton.grid(row=0, column=0, padx=10, pady=10)

    downloadicon_path = resourcesdir / "download.png"
    downloadicon_path_dark = resourcesdir / "downloaddark.png"
    try:
        if iconpack == "Light":
            downloadiconimg = Image.open(downloadicon_path)
        elif iconpack == "Dark":
            downloadiconimg = Image.open(downloadicon_path_dark)
        else:
            downloadiconimg = replacementicon512
            packiumiconpackvalueisfucked = True
    except FileNotFoundError:
        messagebox.showerror("Error!", "Packium was not able to open and/or was not able to find the download icon (aka /resources/download.png or /resources/downloaddark.png).")
        downloadiconimg = replacementicon512
    downloadicon = ctk.CTkImage(light_image=downloadiconimg, dark_image=downloadiconimg, size=(sizeidxb, sizeidxb))
    downloadbutton = ctk.CTkButton(optionsframe, text="", image=downloadicon, width=60, height=60, fg_color=buttoncolor, hover_color=bttoncolor_hover)
    downloadbutton.grid(row=0, column=1, padx=10, pady=10)
        
        
    uninstallicon_path = resourcesdir / "uninstall.png"
    uninstallicon_path_dark = resourcesdir / "uninstalldark.png"
    try:
        if iconpack == "Light":
            uninstalliconimg = Image.open(uninstallicon_path)
        elif iconpack == "Dark":
            uninstalliconimg = Image.open(uninstallicon_path_dark)
        else:
            uninstalliconimg = replacementicon512
            packiumiconpackvalueisfucked = True
    except FileNotFoundError:
        messagebox.showerror("Error!", "Packium was not able to open and/or was not able to find the uninstall icon (aka /resources/uninstall.png or /resources/uninstalldark.png).")
        uninstalliconimg = replacementicon512
    uninstallicon =  ctk.CTkImage(light_image=uninstalliconimg, dark_image=uninstalliconimg, size=(sizeidxb, sizeidxb))
    uninstallbutton = ctk.CTkButton(optionsframe, text="", image=uninstallicon, width=60, height=60, fg_color=buttoncolor, hover_color=bttoncolor_hover)
    uninstallbutton.grid(row=0, column=2, padx=10, pady=10)
    
    

    def discordbuttonclicked():
        discordinvite()
        print("discord invite")
    discordicon_path = resourcesdir / "discord.png"
    discordicon_path_dark = resourcesdir / "discorddark.png"
    try:
        if iconpack == "Light":
            discordiconimg = Image.open(discordicon_path)
        elif iconpack == "Dark":
            discordiconimg = Image.open(discordicon_path_dark)
        else:
            discordiconimg = replacementicon512
            packiumiconpackvalueisfucked = True
    except FileNotFoundError:
        messagebox.showerror("Error!", "Packium was not able to open and/or was not able to find the discord icon (aka /resources/discord.png or /resources/discorddark.png).")
        discordiconimg = replacementicon512
    discordicon = ctk.CTkImage(light_image=discordiconimg, dark_image=discordiconimg, size=(sizeidxb, sizeidxb))
    discordbutton = ctk.CTkButton(optionsframe, text="", image=discordicon, width=60, height=60, fg_color=buttoncolor, hover_color=bttoncolor_hover, command=lambda:discordbuttonclicked())
    discordbutton.grid(row=1, column=1, padx=10, pady=10)
    
    
    
    settingsicon_path = resourcesdir / "settings.png"
    settingsicon_path_dark = resourcesdir / "settingsdark.png"
    try:
        if iconpack == "Light":
            settingsiconimg = Image.open(settingsicon_path)
        elif iconpack == "Dark":
            settingsiconimg = Image.open(settingsicon_path_dark)
        else:
            settingsiconimg = replacementicon512
            packiumiconpackvalueisfucked = True
    except FileNotFoundError:
        messagebox.showerror("Error!", "Packium was not able to open and/or was not able to find the settings icon (aka /resources/settings.png or /resources/settingsdark.png).")
        settingsiconimg = replacementicon512
    settingsicon = ctk.CTkImage(light_image=settingsiconimg, dark_image=settingsiconimg, size=(sizeidxb, sizeidxb))
    settingsbutton = ctk.CTkButton(optionsframe, text="", image=settingsicon, width=60, height=60, fg_color=buttoncolor, hover_color=bttoncolor_hover, command=lambda:settingsbuttonpressed())
    settingsbutton.grid(row=1, column=0, padx=10, pady=10)
    
    abouticon_path = resourcesdir / "about.png"
    abouticon_path_dark = resourcesdir / "aboutdark.png"
    try:
        if iconpack == "Light":
            abouticonimg = Image.open(abouticon_path)
        elif iconpack == "Dark":
            abouticonimg = Image.open(abouticon_path_dark)
        else:
            abouticonimg = replacementicon512
            packiumiconpackvalueisfucked = True
    except FileNotFoundError:
        messagebox.showerror("Error!", "Packium was not able to open and/or was not able to find the about icon (aka /resources/about.png or /resources/aboutdark.png).")
        abouticonimg = replacementicon512
    abouticon = ctk.CTkImage(light_image=abouticonimg, dark_image=abouticonimg, size=(sizeidxb, sizeidxb))
    aboutbutton = ctk.CTkButton(optionsframe, text="", image=abouticon, width=60, height=60, fg_color=buttoncolor, hover_color=bttoncolor_hover)
    aboutbutton.grid(row=1, column=2, padx=10, pady=10)
    if packiumiconpackvalueisfucked == True:
        messagebox.showerror("Error!", 'Packium could not read the iconpack value in /ui/options.packium. You can manually edit the options file to iconpack = "Dark" or iconpack = "Light" to fix this, or just reset your appearance settings.')
    else:
        pass
    #hoverfuncs
    timerid = None
    currentsize = sizeidxb 
    def hoveran(tidxub):
        nonlocal timerid, sizeidxb, sizeidxbh, currentsize
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
        hoveran(sizeidxbh)
    def hoverupdateleave(event=None):
        nonlocal timerid
        if timerid is not None:
            updatebutton.after_cancel(timerid)
            timerid = None
        hoveran(sizeidxb)
        updateicon.configure(size=(sizeidxb, sizeidxb))
    updatebutton.bind("<Enter>", hoverupdate)
    updatebutton.bind("<Leave>", hoverupdateleave)
    
    timeriddb = None
    def hoverand(tidxdb):
        nonlocal timeriddb, sizeidxb, sizeidxbh, currentsize
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
        hoverand(sizeidxbh)
    def hoverupdateleaved(event=None):
        nonlocal timeriddb
        if timeriddb is not None:
            downloadbutton.after_cancel(timeriddb)
            timeriddb = None
        hoverand(sizeidxb)
        downloadicon.configure(size=(sizeidxb, sizeidxb))
    downloadbutton.bind("<Enter>", hoverupdated)
    downloadbutton.bind("<Leave>", hoverupdateleaved)
    
    timeriduib = None
    def hoveranui(tidxuib):
        nonlocal timeriduib, sizeidxb, sizeidxbh, currentsize
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
        hoveranui(sizeidxbh)
    def hoverupdateleaveui(event=None):
        nonlocal timeriduib
        if timeriduib is not None:
            uninstallbutton.after_cancel(timeriduib)
            timeriduib = None
        hoveranui(sizeidxb)
        uninstallicon.configure(size=(sizeidxb, sizeidxb))
    uninstallbutton.bind("<Enter>", hoverupdateui)
    uninstallbutton.bind("<Leave>", hoverupdateleaveui)
    
    timeridseb = None
    def hoverans(tidxsb):
        nonlocal timeridseb, sizeidxb, sizeidxbh, currentsize
        if currentsize == tidxsb:
            timeridseb = None
            return
        if currentsize < tidxsb:
            currentsize += 1
        else:
            currentsize -= 1
        try:
            settingsicon.configure(size=(currentsize, currentsize))
        except Exception:
            pass
        timeridseb = settingsbutton.after(20, hoverans, tidxsb)
    def hoverupdates(event=None ):
        nonlocal timeridseb
        if timeridseb is not None:
            settingsbutton.after_cancel(timeridseb)
            timeridseb = None
        hoverans(sizeidxbh)
    def hoverupdateleaves(event=None):
        nonlocal timeridseb
        if timeridseb is not None:
            settingsbutton.after_cancel(timeridseb)
            timeridseb = None
        hoverans(sizeidxb)
        settingsicon.configure(size=(sizeidxb, sizeidxb))
    settingsbutton.bind("<Enter>", hoverupdates)
    settingsbutton.bind("<Leave>", hoverupdateleaves)
    
    timeriddib = None
    def hoverandi(tidxdib):
        nonlocal timeriddib, sizeidxb, sizeidxbh, currentsize
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
        hoverandi(sizeidxbh)
    def hoverupdateleavedi(event=None):
        nonlocal timeriddib
        if timeriddib is not None:
            discordbutton.after_cancel(timeriddib)
            timeriddib = None
        hoverandi(sizeidxb)
        discordicon.configure(size=(sizeidxb, sizeidxb))
    discordbutton.bind("<Enter>", hoverupdatedi)
    discordbutton.bind("<Leave>", hoverupdateleavedi)
    
    timeridab = None
    def hoverana(tidxab):
        nonlocal timeridab, sizeidxb, sizeidxbh, currentsize
        if currentsize == tidxab:
            timeridab = None
            return
        if currentsize < tidxab:
            currentsize += 1
        else:
            currentsize -= 1
        try:
            abouticon.configure(size=(currentsize, currentsize))
        except Exception:
            pass
        timeridab = aboutbutton.after(20, hoverana, tidxab)
    def hoverupdatea(event=None ):
        nonlocal timeridab
        if timeridab is not None:
            aboutbutton.after_cancel(timeridab)
            timeridab = None
        hoverana(sizeidxbh)
    def hoverupdateleavea(event=None):
        nonlocal timeridab
        if timeridab is not None:
            aboutbutton.after_cancel(timeridab)
            timeridab = None
        hoverana(sizeidxb)
        abouticon.configure(size=(sizeidxb, sizeidxb))
    aboutbutton.bind("<Enter>", hoverupdatea)
    aboutbutton.bind("<Leave>", hoverupdateleavea)
    
    app.mainloop()
