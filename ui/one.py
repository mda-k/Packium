import customtkinter as ctk
import tkinter as tk
def mainui():
    app = ctk.CTk()
    app.geometry("400x200")
    app.overrideredirect(True)
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("dark-blue")

    def FUCKMYLIFE():
        app.quit()
        app.after(100, app.destroy())
    app.protocol("WM_DELETE_WINDOW", FUCKMYLIFE)
    app.title("Winget UI")
    app.attributes("-alpha", 0.7)
    app.attributes("-topmost", True)
    transparent_color = "#000001"
    app.attributes("-transparentcolor", transparent_color)
    app.configure(fg_color=transparent_color)
    overlayframe = ctk.CTkFrame(app, corner_radius=25)
    overlayframe.pack(fill="both", expand=True, padx=2, pady=2)
    close = ctk.CTkButton(overlayframe, text="", fg_color="gray", hover_color="white", width=10, height=10, corner_radius=20, command=lambda:FUCKMYLIFE())
    close.place(relx=1.0, rely=0.0, x=-12, y=12, anchor="ne")
    name = ctk.CTkLabel(overlayframe, text="Winget UI", fg_color="transparent", font=("Arial", 16))
    name.pack(side="top", pady=(10, 0))
    app.mainloop()