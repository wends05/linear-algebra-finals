import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class GraphComponent:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.frame.pack(fill="both", expand=True)


        self.figure = Figure(figsize=(5, 4))
        self.ax = self.figure.add_subplot(111)
        self.ax.plot([], [])


        self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill="both", expand=True)


    def plot_data(self, x, y):
        self.ax.clear()
        self.ax.plot(x, y)
        self.canvas.draw()