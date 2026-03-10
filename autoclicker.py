import time
import threading
import tkinter as tk
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

# Define variables, Define Functions, Start backgroud tasks (threading), GUI Setup

mouse = Controller()
clicking = False
cps = 10
toggle_key = "F6"

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            time.sleep(1 / cps)
        else:
            time.sleep(0.1)

def toggle_event(key):
    global clicking
    try:
        k = key.char if hasattr(key, 'char') else key.name
        if k.upper() == toggle_key.upper():
            clicking = not clicking
    except:
        pass

def update_settings():
    global cps, toggle_key
    try:
        cps = int(cps_entry.get())
        if cps <= 0:
            cps = 1
        toggle_key = key_entry.get()
    except ValueError:
        pass


# Giver Keyboard Listening et Thread
threading.Thread(target=clicker, daemon=True).start()
listener = Listener(on_press=toggle_event)
listener.start()

# GUI Setup
root = tk.Tk()
root.title("AutoClicker")
root.geometry("450x400")
root.configure(padx=10, pady=10)

# Box (parent)
interval_frame = tk.LabelFrame(root, text="Click interval", padx=10, pady=10)
interval_frame.pack(fill="x", pady=5)

# Changed time_container from .pack to .grid
time_container = tk.Frame(interval_frame)
time_container.grid()

# Toggle CPS
tk.Label(interval_frame, text="Toggle CPS:").grid(row=0, column=0, sticky="w", pady=2)
cps_entry = tk.Entry(interval_frame)
cps_entry.insert(0, cps)
cps_entry.grid(row=0, column=1, padx=10, pady=2)

# Toggle Start/End Key
tk.Label(interval_frame, text="Toggle Start/End Key:").grid(row=1, column=0, sticky="w", pady=2)
key_entry = tk.Entry(interval_frame)
key_entry.insert(0, toggle_key)
key_entry.grid(row=1, column=1, padx=10, pady=2)
# Update Settings button
tk.Button(root, text="Update Settings", command=update_settings).pack()

root.mainloop()
