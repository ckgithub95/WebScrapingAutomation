import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


def scrape_data(url):
    """
    This is web scraping function which take URL and return data of that present on URL in excel.
    :param url: user_data
    :return: scrape data into excel
    """
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        data = []
        table = soup.find('table')  # Example for a table
        if table:
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                data.append(cols)

        if data:
            columns = ['Column' + str(i) for i in range(1, len(data[0]) + 1)]
            df = pd.DataFrame(data, columns=columns)  # Adjust columns as needed
            file_path = os.path.join(os.getcwd(), 'scraped_data.xlsx')
            df.to_excel(file_path, index=False)

            messagebox.showinfo("Success", f"Data scraped and saved to {file_path}")
        else:
            messagebox.showinfo("No Data", "No data found on the page")
    else:
        messagebox.showerror("Error", "Failed to retrieve the webpage")
