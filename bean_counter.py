import tkinter as tk
from tkinter import font
import time
import os
import sys
import ctypes  # Only works on Windows

def update_counter():
    global time_left
    if time_left > 0:
        minutes, seconds = divmod(time_left, 60)
        time_format = f"{minutes:02}:{seconds:02}"
        label.config(text=f"Your PC will become a bean in: {time_format}")
        time_left -= 1
        root.after(1000, update_counter)
    else:
        label.config(text="Your PC is now a bean!")
        set_wallpaper("bean.jpg")

def resize_text(event):
    # Adjust the font size based on the window's current height
    new_size = max(13, event.height // 13)
    label_font.config(size=new_size)

def set_wallpaper(image_path):
    # Get the directory where the script is located
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_path, image_path)
    # Set the wallpaper on Windows
    ctypes.windll.user32.SystemParametersInfoW(20, 0, full_path, 3)

def disable_close():
    pass  # Do nothing when trying to close the window

# Create the main window
root = tk.Tk()
root.title("Bean Counter")
root.geometry("400x200")
root.configure(bg="red")

# Override the close button functionality
root.protocol("WM_DELETE_WINDOW", disable_close)

# Create a label to display the countdown
label_font = font.Font(family="Helvetica", size=20, weight="bold")
label = tk.Label(root, text="", font=label_font, fg="black", bg="red")
label.pack(expand=True, fill="both")

# Bind the resize event to the resize_text function
root.bind("<Configure>", resize_text)

# Initialize the countdown time (10 minutes = 600 seconds)
time_left = 10

# Start the countdown
update_counter()

# Run the application
root.mainloop()
