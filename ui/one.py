import customtkinter as ctk
import tkinter as tk
from PIL import Image
from pathlib import Path
import sys
currentdir = Path(__file__).resolve().parent
print(currentdir)	#ui
rootdir = currentdir.parent
print(rootdir)		#root
resourcesdir = rootdir  / "resources"
print(resourcesdir)
if str(rootdir) not in sys.path:
    sys.path.insert(0, str(rootdir))
if str(currentdir) not in sys.path:
    sys.path.insert(0, str(currentdir))
if str(resourcesdir) not in sys.path:
    sys.path.insert(0, str(resourcesdir))
def mainui():
    app = ctk.CTk()
    app.geometry("300x200")
    app.overrideredirect(True)
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("dark-blue")

    def FUCKMYLIFE():
        app.quit()
        app.after(100, app.destroy())
    app.protocol("WM_DELETE_WINDOW", FUCKMYLIFE)
    app.title("Winget UI")
    app.attributes("-topmost", True)
    transparent_color = "#000001"
    app.attributes("-alpha", 0.7)
    app.attributes("-transparentcolor", transparent_color)
    app.configure(fg_color=transparent_color)
    overlayframe = ctk.CTkFrame(app, corner_radius=25)
    overlayframe.pack(fill="both", expand=True, padx=2, pady=2)
    close = ctk.CTkButton(overlayframe, text="", fg_color="white", hover_color="gray", width=8, height=8, corner_radius=4, command=lambda:FUCKMYLIFE())
    close.place(relx=1.0, rely=0.0, x=-12, y=12, anchor="ne")
    name = ctk.CTkLabel(overlayframe, text="Packium", fg_color="transparent", font=("Arial", 16, "bold"), text_color="white")
    name.pack(side="top", pady=(2, 0))
    optionsframe = ctk.CTkFrame(overlayframe, corner_radius=25, fg_color="transparent")
    optionsframe.pack()
    updateicon_path = resourcesdir / "update.png"
    print(updateicon_path)
    updateiconimg = Image.open(updateicon_path)
    updateicon = ctk.CTkImage(light_image=updateiconimg, dark_image=updateiconimg, size=(30, 30))
    updatebutton = ctk.CTkButton(optionsframe, text="", image=updateicon, width=60, height=60, fg_color="#3b3b3b", hover_color="#787878")
    updatebutton.grid(row=0, column=0, padx=10, pady=10)
    dummybutton = ctk.CTkButton(optionsframe, text="", width=60, height=60, fg_color="#3b3b3b", hover_color="#787878")
    dummybutton.grid(row=0, column=1, padx=10, pady=10)
    dummybutton0 = ctk.CTkButton(optionsframe, text="", width=60, height=60, fg_color="#3b3b3b", hover_color="#787878")
    dummybutton0.grid(row=0, column=2, padx=10, pady=10)
    dummybutton1 = ctk.CTkButton(optionsframe, text="", width=60, height=60, fg_color="#3b3b3b", hover_color="#787878")
    dummybutton1.grid(row=1, column=0, padx=10, pady=10)
    dummybutton2 = ctk.CTkButton(optionsframe, text="", width=60, height=60, fg_color="#3b3b3b", hover_color="#787878")
    dummybutton2.grid(row=1, column=1, padx=10, pady=10)
    dummybutton3 = ctk.CTkButton(optionsframe, text="", width=60, height=60, fg_color="#3b3b3b", hover_color="#787878")
    dummybutton3.grid(row=1, column=2, padx=10, pady=10)
    app.mainloop()
