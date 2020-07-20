""" 
GUI_main.py
This file is a project delieverable for Phase I of the ENSF 592 Project Assignment. 
The file runs the GUI for the Calgary Traffic App.

@Author: J. XU, K. ZHANG, P. KWAN
@Since: July 19 2020
"""

from tkinter import *
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from read_db import *
from Map import *


# GUI class acts as an interface between the user and the traffic and mapping objects.

class GUI:

    # This is the constructor method for GUI. It receives the tkinter object from the main() function and adds all the required labels, buttons, comboboxes.

    def __init__(self, master):
        # Assign the master to root_
        self.root_ = master

        # Create a left and right frame.
        # Left frame contains combobox and the read button
        # Right frame contains field for the table

        self.left_ = Frame(self.root_, width=300, height=1500, borderwidth=2, relief="solid", bg="#a6a6a6")
        self.right_ = Frame(self.root_, width=800, height=1500, borderwidth=2, relief="solid")
        self.tree = ttk.Treeview(self.right_)

        # Create a combobox and label for data type value

        self.label1_ = ttk.Label(self.left_, text="Type")
        self.combobox1_ = ttk.Combobox(self.left_, text="type", width=15)
        self.combobox1_['values'] = ("Traffic Volume", "Traffic Accident")
        self.combobox1_.set("Traffic Volume")

        # Create a combobox and label for year type value

        self.label2_ = ttk.Label(self.left_, text="Year")
        self.combobox2_ = ttk.Combobox(self.left_, text="year", width=15)
        self.combobox2_['values'] = ("2016", "2017", "2018")
        self.combobox2_.set("2016")

        # Create a series of buttons

        self.btn1_ = Button(self.left_, text="Read", height=3, width=20, command=self.read)
        self.btn2_ = Button(self.left_, text="Sort", height=3, width=20, command=self.sort)
        self.btn3_ = Button(self.left_, text="Analysis", height=3, width=20, command=self.analyze)
        self.btn4_ = Button(self.left_, text="Map", height=3, width=20, command=self.open_map)

        # Create a new label thats a String Var

        self.label3_ = ttk.Label(self.left_, text="status:")
        self.status_ = StringVar()
        self.status_.set('status messages')
        self.label_ = ttk.Label(self.left_, textvariable=self.status_)

        # Pack everything together so we can see the GUI

        self.label1_.pack()
        self.combobox1_.pack()
        self.label2_.pack()
        self.combobox2_.pack()
        self.btn1_.pack()
        self.btn2_.pack()
        self.btn3_.pack()
        self.btn4_.pack()
        self.label3_.pack()
        self.label_.pack()
        self.left_.pack(side="left", expand=True, fill="both")
        self.right_.pack(side="right", expand=True, fill="both")

        # Say its completed
        print("completed")

    # The read function reads data of selected type/year onto the right frame

    def read(self):

        self.tree.destroy()

        data_type, data_year = self.get_Combobox_value()
        self.status_.set("Read: " + data_type + " " + data_year)

        # TODO add read operation

        if data_type == "Traffic Volume":
            type_ = "Vol"
        if data_type == "Traffic Accident":
            type_ = "Accident"

        df = read_data(type_, data_year)

        cols = list(df.columns)
        self.tree = ttk.Treeview(self.right_)
        self.tree["columns"] = cols
        for i in cols:
            self.tree.column(i, anchor="w")
            self.tree.heading(i, text=i, anchor='w')

        for index, row in df.iterrows():
            self.tree.insert("", "end", text=index, values=list(row))

        self.tree.pack(fill="both", expand=True)

    # The sorts function sorts data of selected type/year

    def sort(self):

        self.tree.destroy()

        data_type, data_year = self.get_Combobox_value()
        self.status_.set("Sort: " + data_type + " " + data_year)

        if data_type == "Traffic Volume":
            type_ = "Vol"
        if data_type == "Traffic Accident":
            type_ = "Accident"

        df = read_data(type_, data_year)

        df_sorted = sort_data(df, type_)

        cols = list(df_sorted.columns)
        self.tree = ttk.Treeview(self.right_)
        self.tree["columns"] = cols
        for i in cols:
            self.tree.column(i, anchor="w")
            self.tree.heading(i, text=i, anchor='w')

        for index, row in df_sorted.iterrows():
            self.tree.insert("", "end", text=index, values=list(row))

        self.tree.pack(fill="both", expand=1)

    # The analyze function analyze data of selected type/year

    def analyze(self):

        data_type, data_year = self.get_Combobox_value()
        self.status_.set("Analyze: " + data_type + " \n" + data_year)

        canvas = FigureCanvasTkAgg(analyze_yearly(data_type), self.root_)
        canvas.show()
        canvas.get_tkwidget().pack(self.right_, expand=True)

        # TODO add analyze operation

    # The open_map function creates a map with a marker denoting largest value of selected type/year

    def open_map(self):

        data_type, data_year = self.get_Combobox_value()
        self.status_.set("Map: " + data_type + " " + data_year)

        # TODO add open map operation

    # This is a getter function for the combobox1_ and combobox2_
    # Returns a tuple with the format (data_type, data_year)

    def get_Combobox_value(self):
        data_type = self.combobox1_.get()
        data_year = self.combobox2_.get()

        self.status_.set(data_type + " " + data_year)
        return data_type, data_year


# The main function creates a tkinter object named root and passes root to a GUI object. The main function houses the mainloop for root

def main():
    root = Tk()
    GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
