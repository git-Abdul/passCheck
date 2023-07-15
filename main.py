import os
import math
import string

import customtkinter as ctk
from customtkinter import *
from PIL import Image

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")

def refresh():
    text = ""
    strings.set(text)

def toggle_password_visibility():
    global password_visible
    password_visible = not password_visible
    if password_visible:
        e.configure(show="")
    else:
        e.configure(show="•")

def center_window(w):
    w.update_idletasks()
    width = w.winfo_width()
    height = w.winfo_height()
    x_offset = math.floor((w.winfo_screenwidth() - width) / 2)
    y_offset = math.floor((w.winfo_screenheight() - height) / 2)
    w.geometry(f"+{x_offset}+{y_offset}")

def update_password_strength():
    password = e.get()
    strength = check_password_strength(password)
    strength_label.configure(text=strength)

def check_password_strength(password):
    # Define your password strength criteria and logic here
    if len(password) < 6:
        strength = "Very Weak"
        color = "#b40d1b"
    elif len(password) < 8:
        strength = "Weak"
        color = "#ce9178"
    elif len(password) < 10:
        strength = "Moderate"
        color = "#ffd300"
    else:
        has_digit = any(char.isdigit() for char in password)
        has_special = any(char in string.punctuation for char in password)
        
        if has_digit and has_special:
            strength = "Strong"
            color = "#51bbff"
        elif has_digit or has_special:
            strength = "Better"
            color = "#7fb788"
        else:
            strength = "Good"
            color = "#7fb766"

    strength_label.configure(text=strength, text_color=color)


root = ctk.CTk()
root.title("Pass Check")
root.geometry('395x175')
root.iconbitmap("icon.ico")
root.resizable(False, False)
ctk.set_appearance_mode("System")

global strings
strings = StringVar()

password_visible = False

Poppins = CTkFont(
    family= "Segoe UI",
    size =25,
    weight="bold",
)

root.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(30,30))
root.refresh_image = ctk.CTkImage(Image.open(os.path.join(image_path, "refresh.png")), size=(15, 15))
root.show_image = ctk.CTkImage(Image.open(os.path.join(image_path, "show.png")), size=(15, 15))

title = ctk.CTkLabel(root, text="Pass Check", font=Poppins, image=root.logo_image, compound="left")
title.grid(row=0, pady=20, padx=110, sticky='n')

frame = ctk.CTkFrame(root, corner_radius=50, bg_color='transparent')
frame.grid(row=1, pady=10, padx=(70, 0), sticky='w')

refresh = ctk.CTkButton(frame, command=refresh, image=root.refresh_image, text=None, width=15, height=27, fg_color="#3978FF")
refresh.grid(row=0, column=0)

show_hide_button = ctk.CTkButton(frame, command=toggle_password_visibility, image=root.show_image, text=None, width=15, height=27, fg_color="#3978FF")
show_hide_button.grid(row=0, column=1, padx=(5, 0))

e = ctk.CTkEntry(frame, placeholder_text="Enter Password:", show="•", width=175, textvariable=strings)
e.grid(row=0, column=2, padx=(5, 0))
e.bind("<KeyRelease>", lambda event: update_password_strength())

strength_label = ctk.CTkLabel(root, text="", font=("Seoge UI", 15))
strength_label.grid(row=2, pady=10)

root.after(0, lambda: center_window(root))
root.mainloop()
