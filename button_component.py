import tkinter as tk


class ButtonComponent:
    def __init__(self, parent, title, command):
        self.button = tk.Button(parent, text=title, command=command)
        self.button.pack(side="top", pady=(10, 0), fill="x")
