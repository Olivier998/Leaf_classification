"""
Class to show the main interface to plot results
"""
import tkinter as tk
OptionList = ["", "Ridge"]


class Interface:
    """"""

    def __init__(self, master):
        self.root = master
        # frames
        self.left_frame = Frame(self.root, side="left")
        self.right_frame = Frame(self.root, side="right")#tk.Frame(self.root)



class Frame:

    def __init__(self, master, side):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack(side=side, fill="both", expand=True)

        global OptionList
        method_choice = tk.StringVar(self.frame)
        method_choice.set(OptionList[0])

        opt = tk.OptionMenu(master, method_choice, *OptionList)
        opt.pack()




def test():
    print("hey")

if __name__ == "__main__":
    root = tk.Tk()
    al = Interface(root)
    root.mainloop()
