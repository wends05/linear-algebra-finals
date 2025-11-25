import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class GraphComponent:
    def __init__(self, parent, labels):
        self.frame = tk.Frame(parent)
        self.frame.pack(side="bottom", fill="both", expand=True)

        self.labels = labels

        self.figure = Figure(figsize=(5, 4))
        self.ax = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill="both", expand=True)

        # ---- INITIAL EMPTY GRAPH ----
        self._init_empty_graph()

    def _init_empty_graph(self):
        """Draws the initial graph with labels, title, and zero bars."""
        zero_values = [0] * len(self.labels)
        self.plot_data("Time of Work Per Developer", "Developers", "Time", zero_values)

    def plot_data(self, title, xlabel, ylabel, values):
        """
        values: list/array of numerical values for y-axis
        """
        self.ax.clear()

        bars = self.ax.bar(self.labels, values)

        # ---- Add space above highest bar ----
        max_val = max(values) if len(values) > 0 else 0
        top_limit = max_val * 1.15 if max_val > 0 else 1
        self.ax.set_ylim(0, top_limit)

        # ---- Add value annotations ----
        for bar, val in zip(bars, values):
            self.ax.annotate(
                f"{round(val, 2)}",
                xy=(bar.get_x() + bar.get_width() / 2, val),
                xytext=(0, 3),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=9
            )

        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.ax.set_title(title)

        self.figure.tight_layout()
        self.canvas.draw()
