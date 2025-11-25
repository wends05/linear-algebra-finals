import tkinter as tk
from graph_component import GraphComponent
from button_component import ButtonComponent
from input_component import InputComponent
from src.matrix import Matrix
from src.constants import five_by_five_matrix
import numpy as np


class App:
    CAT_LABELS = ["Senior\nDeveloper", "Mid-Level\nDeveloper", "Junior\nDeveloper", "QA\nEngineer"]

    def __init__(self, root):
        root.title("Developer Hour Estimation Prototype")

        # Main container frame for layout
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill="both", expand=True)

        # Left side frame (inputs + button)
        self.left_frame = tk.Frame(self.main_frame)
        self.left_frame.pack(side="left", fill="y", padx=10, pady=10)

        # Input panel inside left frame
        self.input_panel = InputComponent(self.left_frame)
        self.input_panel.frame.pack(side="top", fill="x", pady=(0, 10))  # pack the input panel from the top

        # Button below input panel
        self.button = ButtonComponent(self.left_frame, "Calculate Results", self.plot_values)
        self.button.button.pack(side="top", pady=10)  # pack button below input bars

        # Right side frame (graph)
        self.right_frame = tk.Frame(self.main_frame)
        self.right_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Graph panel inside right frame
        self.graph = GraphComponent(self.right_frame, self.CAT_LABELS)

    def plot_values(self):
        input_values = self.input_panel.get_values()
        if input_values is None:
            return
        res = Matrix.gaussian_elimination(five_by_five_matrix, np.array(input_values))
        self.graph.plot_data("Time of Work Per Developer", "Developers", "Time", res)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
