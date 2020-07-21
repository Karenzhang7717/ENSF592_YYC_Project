
"""
GUI_main.py
This file is a project delieverable for Phase I of the ENSF 592 Project Assignment. 
The file runs the GUI for the Calgary Traffic App.
@Author: J. XU, K. ZHANG, P. KWAN
@Since: July 19 2020
"""
import string
from tkinter import *
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

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
        print("GUI generated")

    # The read function reads data of selected type/year onto the right frame

    def read(self):
   
        self.update_type_year()

        df = read_data(self.type_, self.year_)

        self.output_table(df)

        self.status_.set("Read: " + self.type_ + " " + self.year_)

    # The sorts function sorts data of selected type/year

    def sort(self):
        
        self.update_type_year()

        df = read_data(self.type_, self.year_)
        
        df_sorted = sort_data(df, self.type_)

        self.output_table(df_sorted)

        self.status_.set("Sort: " + self.type_ + " " + self.year_)

    # The analyze function analyze data of selected type/year

    def analyze(self):

        self.update_type_year()

        self.status_.set("Analyze: " + self.type_)

        analyze_yearly(self.type_)


    # The open_map function creates a map with a marker denoting largest value of selected type/year

    def open_map(self):

        self.update_type_year()

        if self.type_ == "Vol":
            
            df = read_data(self.type_, self.year_)
            df_sorted = sort_data(df, self.type_)

            loc, coord = get_most_vol_coordinate(df_sorted)

            coord_list = list()

            for value in coord.split()[1:]:
                value = value.strip("(), ")
                coord_list.append(float(value))
            

            for i in range(1,len(coord_list)):
                temp = coord_list[i-1]
                coord_list[i-1] = coord_list[i]
                coord_list[i] = temp
            
            #print("For year", data_year,"and type",data_type,"the location", loc, "the coordinates",coord_list[0:2])

            map_object = Map(self.type_, self.year_,coord_list[:2], loc)
            map_object.create_Map()
               
        if self.type_ == "Accident":

            df = read_data(self.type_, self.year_)
            df_sorted = sort_data(df, self.type_)

            loc, coord = get_most_accident_coord(df, df_sorted)

            coord_list = list()

            for value in coord.split():
                value = value.strip("(), ")
                coord_list.append(float(value))
            
            print("For year", self.year_,"and type",self.type_,"the location", loc, "the coordinates",coord_list)

            map_object = Map(self.type_, self.year_,coord_list, loc)
            map_object.create_Map()

        self.status_.set("Mapping: " + self.type_ + " " + self.year_)

    # Update self.type_ and self.year_

    def update_type_year(self):
        data_type = self.combobox1_.get()
        data_year = self.combobox2_.get()

        if data_type == "Traffic Volume":
            self.type_ = "Vol"
        else:
            self.type_ = "Accident"
        
        self.year_ = data_year

    # The output_table function outputs the table for the read and sort functions. Receives the desired dataframe (df) to be outputted.

    def output_table(self, df):
        self.tree.destroy()

        cols = list(df.columns)

        self.tree = ttk.Treeview(self.right_)

        self.tree["columns"] = cols

        for i in cols:
            self.tree.column(i, anchor="w")
            self.tree.heading(i, text=i, anchor='w')

        for index, row in df.iterrows():
            self.tree.insert("", "end", text=index, values=list(row))

        self.tree.pack(fill="both", expand=True)


# The main function creates a tkinter object named root and passes root to a GUI object. The main function houses the mainloop for root

def main():
    root = Tk()
    GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
