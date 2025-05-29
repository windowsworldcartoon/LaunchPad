import tkinter as tk
from tkinter import ttk
import time

class TimerApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        # Create coming soon
        self.comingsoon = ttk.Label(self, text="Coming Soon", font=("Arial", 24))
        self.comingsoon.pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Timer App")
    app = TimerApp(root)
    root.mainloop()