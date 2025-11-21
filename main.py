import tkinter as tk
from graph_component import GraphComponent
from button_component import ButtonComponent
import numpy as np


class App:
    def __init__(self, root):
        root.title("Tkinter + Matplotlib Example")

        self.graph = GraphComponent(root)
        self.button = ButtonComponent(root, self.plot_random)

    def plot_random(self):
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        self.graph.plot_data(x, y)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()