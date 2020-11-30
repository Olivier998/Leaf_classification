"""
Class to show the main interface to plot results
"""
import tkinter as tk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

OptionList = ["Choose a method", "Ridge"]




class Interface:
    """"""

    def __init__(self, master):
        self.root = master
        # frames
        self.left_frame = Frame(self.root, side="left", color="white")
        self.right_frame = Frame(self.root, side="right", color="blue")#tk.Frame(self.root)



class Frame:

    def __init__(self, master, side, color="red"):
        self.master = master
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
        self.fig = Figure(figsize=(3, 3))
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
            self.plot1.set_title("Method : " + self.method_choice.get())  # Reset title
            y = [(i / 100) ** 2-5 for i in range(95)]  # Get data

        # plot new data
        self.plot1.plot(y)
        self.canvas.draw()





if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(840, 400)
    al = Interface(root)
    root.mainloop()
