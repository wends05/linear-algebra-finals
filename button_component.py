import tkinter as tk


class ButtonComponent:
    def __init__(self, parent, command):
        self.button = tk.Button(parent, text="Plot Graph", command=command)
        self.button.pack(pady=10)