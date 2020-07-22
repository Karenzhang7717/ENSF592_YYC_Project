"""
GUI_main.py
This file is a project deliverable for Phase I of the ENSF 592 Project Assignment.
The file runs the GUI for the Calgary Traffic App.
@Author: J. XU, K. ZHANG, P. KWAN
@Since: July 19 2020
"""
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from read_db import *
from Map import *


# GUI class acts as an interface between the user and the traffic and mapping objects.

class GUI:

    # This is the constructor method for GUI. It receives the tkinter object from the main() function and adds all
    # the required labels, buttons, combo-boxes.

    def __init__(self, master):
        # Assign the master to root
        self.root = master

        # Create a left and right frame.
        # Left frame contains the combobox and buttons
        # Right frame contains field for the table

        self.left = Frame(self.root, width=300, height=1500, borderwidth=2, relief="solid", bg="#a6a6a6")
        self.right = Frame(self.root, width=800, height=1500, borderwidth=2, relief="solid")
        self.tree = ttk.Treeview(self.right)

        # Create a combobox and label for data type value

        self.label1 = ttk.Label(self.left, text="Type")
        self.combobox1 = ttk.Combobox(self.left, text="type", width=15)
        self.combobox1['values'] = ("Traffic Volume", "Traffic Accident")
        self.combobox1.set("Traffic Volume")

        # Create a combobox and label for year type value

        self.label2 = ttk.Label(self.left, text="Year")
        self.combobox2 = ttk.Combobox(self.left, text="year", width=15)
        self.combobox2['values'] = ("2016", "2017", "2018")
        self.combobox2.set("2016")

        # Create a series of buttons

        self.btn1 = Button(self.left, text="Read", height=3, width=20, command=self.read)
        self.btn2 = Button(self.left, text="Sort", height=3, width=20, command=self.sort)
        self.btn3 = Button(self.left, text="Analysis", height=3, width=20, command=self.analyze)
        self.btn4 = Button(self.left, text="Map", height=3, width=20, command=self.open_map)

        # Create a new label thats a String Var

        self.label3 = ttk.Label(self.left, text="status:")
        self.status = StringVar()
        self.status.set('status messages')
        self.label = ttk.Label(self.left, textvariable=self.status)

        # Pack everything together so we can see the GUI

        self.label1.pack()
        self.combobox1.pack()
        self.label2.pack()
        self.combobox2.pack()
        self.btn1.pack()
        self.btn2.pack()
        self.btn3.pack()
        self.btn4.pack()
        self.label3.pack()
        self.label.pack()
        self.left.pack(side="left", expand=True, fill="both")
        self.right.pack(side="right", expand=True, fill="both")


    def read(self):
        """
        Reads the data from user selected data type and year, outputs the table displaying all the data
        and updates the status message
        """

        self.update_type_year()

        df = read_data(self.type_, self.year)

        self.output_table(df)

        self.status.set("Successfully read: " + self.type_ + " \n" + self.year + " from database")



    def sort(self):
        """
        Sorts the data from user selected data type and year, outputs the table displaying all the sorted data
        and updates the status message
        """

        self.update_type_year()

        df = read_data(self.type_, self.year)

        df_sorted = sort_data(df, self.type_)

        self.output_table(df_sorted)

        self.status.set("Successfully sort: \n" + self.type_ + " " + self.year)




    def analyze(self):
        """
        Analyze the data from user selected data type and year, display the plot onto GUI
        and updates the status message
        """

        self.update_type_year()

        self.clear_frame();

        fig = Figure(tight_layout = True)
        
        y = [yearly_max(self.type_, year) for year in range(2016, 2019)]

        fig.add_subplot(111, xticks= range(2016, 2019), xlabel = 'Years', ylabel='Traffic ' + self.type_, \
                        title = 'Traffic ' + self.type_ + ' from 2016 - 2018').\
            plot(range(2016, 2019), y)

        canvas = FigureCanvasTkAgg(fig, master=self.right)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

        self.status.set("Sucessfully analyzed: " + self.type_)


    def open_map(self):
        """
         Creates a map with a marker denoting largest value of selected type/year. the map is saved in html file
         under the same folder once it's called
        """

        self.update_type_year()

        if self.type_ == "Vol":

            df = read_data(self.type_, self.year)
            df_sorted = sort_data(df, self.type_)

            loc, coord = get_most_vol_coordinate(df_sorted)

            coord_list = list()

            for value in coord.split()[1:]:
                value = value.strip("(), ")
                coord_list.append(float(value))

            for i in range(1, len(coord_list)):
                temp = coord_list[i - 1]
                coord_list[i - 1] = coord_list[i]
                coord_list[i] = temp

            map_object = Map(self.type_, self.year, coord_list[:2], loc)
            map_object.create_Map()

        if self.type_ == "Accident":

            df = read_data(self.type_, self.year)
            df_sorted = sort_data(df, self.type_)

            loc, coord = get_most_accident_coord(df, df_sorted)

            coord_list = list()

            for value in coord.split():
                value = value.strip("(), ")
                coord_list.append(float(value))

            map_object = Map(self.type_, self.year, coord_list, loc)
            map_object.create_Map()

        self.status.set("Successfully written to map: \n" + self.type_ + " " + self.year)




    def update_type_year(self):
        """
        Update self.type_ and self.year according to user selection from combobox
        """
        data_type = self.combobox1.get()
        data_year = self.combobox2.get()

        self.type_ = "Vol" if data_type == "Traffic Volume" else "Accident"

        self.year = data_year


    def clear_frame(self):
        """
        clears the right frame
        """
        for widget in self.right.winfo_children():
            widget.destroy()


    def output_table(self, df):
        """
        :param df: the desired dataframe to be outputted
        Outputs the table for the read and sort functions
        """
        self.clear_frame();

        cols = list(df.columns)

        self.tree = ttk.Treeview(self.right)

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
