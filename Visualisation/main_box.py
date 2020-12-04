"""
Class to show the main interface to plot results
"""
import tkinter as tk
import numpy as np
import Classification.methodsTester
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

OptionList = ["Choose a method", "Ridge", "Logistic Regression", "SGD", "Perceptron", "SVM", "Random forest", "ML Perceptron"]


class Interface:
    """ Creates an interface to compare performance of different classification methods on leafs data """

    def __init__(self, master, data_holder):
        self.root = master
        # frames
        self.left_frame = Frame(self.root, data_holder=data_holder, side="left", color="white")
        self.right_frame = Frame(self.root, data_holder=data_holder, side="right", color="white")


class Frame:

    def __init__(self, master, data_holder, side, color="red"):
        self.master = master
        self.data_holder = data_holder
        # Set Frame
        self.frame = tk.Frame(master, bg=color)
        self.frame.pack(side=side, fill="both", expand=True)

        # Set dropdown
        global OptionList
        self.method_choice = tk.StringVar(self.frame)
        self.method_choice.set(OptionList[0])
        opt = tk.OptionMenu(self.frame, self.method_choice, *OptionList)
        opt.pack()

        # Initialise graph
        self.fig = Figure(figsize=(5, 4))
        # adding the subplot
        self.plot1 = self.fig.add_subplot(111)
        self.plot1.plot()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.draw()
        # placing the canvas on the Tkinter window
        self.canvas.get_tk_widget().pack()
        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(self.canvas, self.frame)
        toolbar.update()
        # placing the toolbar on the Tkinter window
        self.canvas.get_tk_widget().pack()

        # Set the refresh graph button
        self.b1 = tk.Button(self.frame, text="Refresh", command=self.refresh_plot, pady=8, padx=30)
        self.b1.pack()

    def refresh_plot(self):
        """ Reset plot in frame with new data from chosen method
        :param window:
        :return:
        """
        self.plot1.clear()  # Clears current graph

        if self.method_choice.get() == "Choose a method":
            y = []
        else:
            self.plot1.set_title("Method : " + self.method_choice.get())  # Reset titles
            self.plot1.set_ylabel("Accuracy")
            self.plot1.set_xlabel("n value (10^n) for regularization term")

            # Get iterative Data
            data_frame = Classification.methodsTester.find_parameters_list(self.method_choice.get(),
                                                                           self.data_holder)
            data_frame["lambd"] = np.log10(data_frame["lambd"])  # we want the exponent
            groups = data_frame.groupby('M')
            for name, group in groups:
                self.plot1.plot(group.lambd, group.score, marker='o', label=name)
            self.plot1.legend(title="M values (for projection)")

        # refresh canvas with new plot
        self.canvas.draw()


def show_interface(data_holder):
    """ Creates the interface """
    root = tk.Tk()
    root.title("Methods comparator")
    root.minsize(1000, 500)
    Interface(root, data_holder)
    root.mainloop()
