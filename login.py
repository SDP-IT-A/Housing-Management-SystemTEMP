import tkinter as tk
from tkinter import messagebox
from tkinter import *
from path_relative import *
from admin_menu import adminmenu
from res_menu import residentpage

def login_module():
    global username,password
    filename = "user_passwd.txt"
    with open(filename, "r") as file:
        lines = file.readlines()
        user_credentials = {line.split(',')[0].strip(): line.split(',')[1].strip() for line in lines}
    filename = "admin_passwd.txt"
    with open(filename, "r") as file:
        lines = file.readlines()
        admin_credentials = {line.split(',')[0].strip(): line.split(',')[1].strip() for line in lines}

    def login():
        global username,password
        username = username_entry.get()
        password = password_entry.get()

        if username in user_credentials:
            if password == user_credentials[username]:
                window.destroy()
                residentpage(username,password)
            else:
                messagebox.showerror("Login Error", "Incorrect password!")
        elif username in admin_credentials:
            if password == admin_credentials[username]:
                window.destroy()
                adminmenu(username,password)
            else:
                messagebox.showerror("Login Error", "Incorrect password!")
        else:
            messagebox.showerror("Login Error", "Unknown username!")

    window = tk.Tk()
    window.title("Login")
    window.geometry('1200x613')
    window.title('PGP Resident Login')
    window.resizable(False, False)
    image_background = PhotoImage(file=relative_to_assets("login_page.png"))
    label = tk.Label(window, image=image_background)
    label.place(x=0, y=0)

    username_label = tk.Label(window, text="Username:", font=("Arial", 16))
    username_label.place(x=500, y=415, anchor="e")
    username_entry = tk.Entry(window, font=("Arial", 16))
    username_entry.place(x=510, y=400, width=200)

    password_label = tk.Label(window, text="Password:", font=("Arial", 16))
    password_label.place(x=500, y=465, anchor="e")
    password_entry = tk.Entry(window, show="*", font=("Arial", 16))
    password_entry.place(x=510, y=450, width=200)

    login_button = tk.Button(window, text="Login", command=login, font=("Arial", 16))
    login_button.place(x=600, y=500, width=100, height=40)

    window.mainloop()