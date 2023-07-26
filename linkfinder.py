import tkinter as tk
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests

def find_js_links():
    url = entry_url.get()
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        js_links = []
        for script in soup.find_all('script'):
            src = script.get('src')
            if src and src.endswith('.js'):
                js_links.append(src)

        if js_links:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "\n".join(js_links))
        else:
            messagebox.showinfo("Result", "No JavaScript links found on the page.")

    except requests.exceptions.MissingSchema:
        messagebox.showerror("Error", "Invalid URL. Please provide a valid URL.")
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Unable to fetch data from the URL. Please check your internet connection.")

# Create the main application window
root = tk.Tk()
root.title("JS Links Finder")
root.geometry("400x400")

# URL input field
label_url = tk.Label(root, text="Enter Web Application URL:")
label_url.pack()
entry_url = tk.Entry(root, width=40)
entry_url.pack()

# Find button
find_button = tk.Button(root, text="Find JS Links", command=find_js_links)
find_button.pack()

# Result text box
result_text = tk.Text(root, wrap=tk.WORD, height=20, width=50)
result_text.pack()

root.mainloop()
