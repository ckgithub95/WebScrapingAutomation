import tkinter as tk
from tkinter import messagebox
import main
import web_scrape
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


def login():
    """
    This is login function, user authentication through static credentials.
    :return: Authentication result
    """
    username = username_entry.get()
    password = password_entry.get()
    # Simulate a login process (replace with actual login logic)
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
        login_window.destroy()  # Close the login window
        open_scrape_window()  # Open the new window
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")


login_window = main.login_window
login_window.title("Login Page")

# Maximize the window
maximize_window = main.maximize_window()
maximize_window(login_window)

# Username label and entry
username_label = tk.Label(login_window, text="Username")
username_label.pack(pady=10)
username_entry = tk.Entry(login_window)
username_entry.pack(pady=5)

# Password label and entry
password_label = tk.Label(login_window, text="Password")
password_label.pack(pady=10)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack(pady=5)

# Login button
login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack(pady=20)
