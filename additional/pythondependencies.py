import subprocess
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.withdraw()
x = messagebox.askyesno("Do you want to proceed?", "This program will install python modules that are dependencies for Packium. Do you want to continue?")
if x:
    subprocess.run(["py", "-m", "pip", "install", "customtkinter", "ctkcolorpicker", "pillow"], text=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
else:
    exit()