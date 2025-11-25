import tkinter as tk
from tkinter import messagebox


class InputComponent:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.frame.pack(side="left", fill="y", padx=10, pady=10)

        self.inputs = {}
        self.labels = ["Complex SP", "Infra SP", "Maintenance SP", "Test SP"]

        for label in self.labels:
            row = tk.Frame(self.frame)
            row.pack(fill="x", pady=5)

            tk.Label(row, text=label).pack(side="left")

            entry = tk.Entry(row, width=10)
            entry.pack(side="right")

            self.inputs[label] = entry

    def get_values(self):
        """
        Returns values as floats. If any field is empty or invalid,
        returns None for that field.
        """
        results = []
        for label in self.labels:
            val = self.inputs[label].get().strip()
            if val == "":
                messagebox.showerror("Missing Input", f"Please enter a value for '{label}'.")
                return None
            try:
                results.append(float(val))
            except ValueError:
                messagebox.showerror("Invalid Input", f"'{label}' must be a number.")
                return None
        return results
