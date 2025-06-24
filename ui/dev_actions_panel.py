import tkinter as tk
from tkinter import messagebox
import os
import sys

def show_actions_panel(batter_height_in, strikezone_on):
    # Use a dict to return updated state
    panel_result = {'strikezone_on': strikezone_on}

    def toggle_strikezone():
        panel_result['strikezone_on'] = not panel_result['strikezone_on']
        btn_strikezone.config(
            text=f"Strikezone: {'ON' if panel_result['strikezone_on'] else 'OFF'}"
        )
        with open("strikezone_state.txt", "w") as f:
            f.write("on" if panel_result['strikezone_on'] else "off")

    def restart_system():
        window.destroy()
        messagebox.showinfo("Restart", "Restarting system...")
        os.execl(sys.executable, sys.executable, *sys.argv)

    window = tk.Tk()
    window.title("Actions Panel")
    window.geometry("250x180")

    tk.Label(window, text=f"Batter Height: {batter_height_in} in", font=("Arial", 12)).pack(pady=10)
    global btn_strikezone
    btn_strikezone = tk.Button(
        window,
        text=f"Strikezone: {'ON' if strikezone_on else 'OFF'}",
        width=20,
        command=toggle_strikezone
    )
    btn_strikezone.pack(pady=10)
    tk.Button(window, text="Restart System", width=20, command=restart_system).pack(pady=10)
    tk.Label(window, text="Close this window to return.", font=("Arial", 9)).pack(pady=10)
    window.mainloop()
    return panel_result
if __name__ == "__main__":
    show_actions_panel(batter_height_in=70, strikezone_on = True)
