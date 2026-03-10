import time
import threading
import tkinter as tk
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

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
        toggle_key = key_entry.get()
    except:
        pass


# Giver Keyboard Listening et Thread
threading.Thread(target=clicker, daemon=True).start()
listener = Listener(on_press=toggle_event)
listener.start()

# GUI Setup
root = tk.Tk()
root.title("AutoClicker")
root.geometry("400x300")


tk.Label(root, text="Toggle CPS").pack()
cps_entry = tk.Entry(root)
cps_entry.insert(0, cps,)
cps_entry.pack()

tk.Label(root, text="Toggle Start/End Key").pack()
key_entry = tk.Entry(root)
key_entry.insert(0, toggle_key)
key_entry.pack()

tk.Button(root, text="Update Settings", command=update_settings).pack()

root.mainloop()