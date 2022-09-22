import tkinter as tk
from tkinter import ttk
import os
import logging

# Logging
logging.basicConfig(filename="Report_File.log", level=logging.INFO, format="%(asctime)s %(message)s")


# Functions
def start():
    try:
        path = entryWidget.get()
        val = os.scandir(path)
        for entry in val:
            label2 = tk.Label(window, text=entry.name)
            label2.pack()
        logging.info("The user entered a valid URL and got a list as output.")
    except FileNotFoundError:
        print("Please enter a valid URL!")
        label3 = tk.Label(window, text="Please enter a valid URL!")
        label3.pack()
        logging.error("The user entered not a valid URL.")


# Create main window
window = tk.Tk()
window.title("URL List Program")
window.geometry('1000x1000')

# Text Lable
label1 = tk.Label(window, text="Please enter a valid URL: ", font=("Arial Bold", 20), bg="lightblue", padx=30, pady=30)
label1.pack()

# Entry Widget
entryWidget = ttk.Entry(window, width=80, font=("Arial Bold", 15), foreground="green")
entryWidget.pack()

# Button Start
buttonStart = ttk.Button(window, text="Start", command=start, padding=10)
buttonStart.pack()

# Button Quit
buttonEnd = ttk.Button(window, text="Quit", command=quit, padding=10)
buttonEnd.pack()
logging.info("The user left the program.")

# Event Handler
window.mainloop()
