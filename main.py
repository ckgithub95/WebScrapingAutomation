import tkinter as tk
from tkinter import messagebox
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


# def scrape_data(url):
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#
#         data = []
#         table = soup.find('table')  # Example for a table
#         if table:
#             rows = table.find_all('tr')
#             for row in rows:
#                 cols = row.find_all('td')
#                 cols = [ele.text.strip() for ele in cols]
#                 data.append(cols)
#
#         if data:
#             columns = ['Column' + str(i) for i in range(1, len(data[0]) + 1)]
#             df = pd.DataFrame(data, columns=columns)  # Adjust columns as needed
#             file_path = os.path.join(os.getcwd(), 'scraped_data.xlsx')
#             df.to_excel(file_path, index=False)
#
#             messagebox.showinfo("Success", f"Data scraped and saved to {file_path}")
#         else:
#             messagebox.showinfo("No Data", "No data found on the page")
#     else:
#         messagebox.showerror("Error", "Failed to retrieve the webpage")


# Function to maximize the window on the screen
def maximize_window(root):
    root.state('zoomed')


# Create the login window
login_window = tk.Tk()
login_window.title("Login Page")

# Maximize the window
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


def open_scrape_window():
    # Create a new window
    scrape_window = tk.Tk()
    scrape_window.title("Scrape Data")

    # Maximize the window
    maximize_window(scrape_window)

    # URL label and entry
    url_label = tk.Label(scrape_window, text="Enter URL to scrape:")
    url_label.pack(pady=10)
    url_entry = tk.Entry(scrape_window, width=50)
    url_entry.pack(pady=5)

    def scrape_button_command():
        url = url_entry.get()
        web_scrape.scrape_data(url)

    # Scrape button
    scrape_button = tk.Button(scrape_window, text="Scrape Data", command=scrape_button_command)
    scrape_button.pack(pady=20)

    scrape_window.mainloop()


login_window.mainloop()
