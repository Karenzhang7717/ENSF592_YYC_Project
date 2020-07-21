import read_db
from read_db import *
from Map import *
from tkinter import *
from tkinter import ttk
import pandas as pd


class CalgaryTrafficGUI:
    
    #Readjust method to accept frame
    #def __init__(self):
    def __init__(self, master):
        #move root to main
        #root = Tk()
        root = master

        self.left = Frame(root, width=300, height=1500, borderwidth=2, relief="solid", bg="#a6a6a6")
        self.right = Frame(root, width=800, height=1500, borderwidth=2, relief="solid")

        label1 = ttk.Label(self.left, text="Type")
        self.combobox1 = ttk.Combobox(self.left, text="type", width=15)
        self.combobox1['value'] = ("Traffic Volume", "Accident")

        label2 = ttk.Label(self.left, text="Year")
        #missing type call
        #self.combobox2 = ttk.Combobox(self.left, width=15)
        self.combobox2 = ttk.Combobox(self.left, text="year", width=15)
        self.combobox2['value'] = ("2016", "2017", "2018")

        #command is somehow being called before the button is pressed. command = ... may be wrong, rather than specifying what to do, its actually just doing it

        #btn1 = Button(self.left, text="Read", height=3, width=20, command=CalgaryTrafficGUI.read(self))
        btn1 = Button(self.left, text="Read", height=3, width=20)
        btn2 = Button(self.left, text="Sort", height=3, width=20)
        btn3 = Button(self.left, text="Analysis", height=3, width=20)
        #btn4 = Button(self.left, text="Map", height=3, width=20, command=CalgaryTrafficGUI.open_map(self))
        btn4 = Button(self.left, text="Map", height=3, width=20)

        label3 = ttk.Label(self.left, text="status:")

        #string var should maybe be initiated once but outside main loop

        
        self.status_txt = StringVar()
        self.status_txt.set('status messages')
  
        
        label4 = ttk.Label(self.left, textvariable=self.status_txt)
        #label4 = ttk.Label(self.left, text="testing")
        
        #change pack order
        """
        self.left.pack(side="left", expand=True, fill="both")
        self.right.pack(side="right", expand=True, fill="both")
        """

        label1.pack()
        self.combobox1.pack()
        label2.pack()
        self.combobox2.pack()

        btn1.pack(pady=20)
        btn2.pack(pady=20)
        btn3.pack(pady=20)
        btn4.pack(pady=20)
        label3.pack(pady=10)
        label4.pack()

        self.left.pack(side="left", expand=True, fill="both")
        self.right.pack(side="right", expand=True, fill="both")

        #move mainloop to main
        #root.mainloop()
    
    def read(self):
        type_ = self.combobox1.get()
        year = self.combobox2.get()
        
        if type_ is not "" and year is not "":
            df = read_data(type_, year)

            cols = list(df.columns)
            tree = ttk.Treeview(self.right)
            tree["columns"] = cols
            for i in cols:
                tree.column(i, anchor="w")
                tree.heading(i, text=i, anchor='w')

            for index, row in df.iterrows():
                tree.insert("", 0, text=index, values=list(row))

            tree.pack()

    def open_map(self):
        # Map Constructor Definition:
        #  Map(self, data_kind = 'Traffic_Incidents', data_year = '2017',
        #  marker_coordinates = [51.03706737,-114.1123288],
        #  location = "17 Avenue at Richmond Road SW",
        #   map_base_coordinates = [51.044270, -114.062019]):

        # Get the type and year user has selected
        map_type = self.combobox1.get()
        map_year = self.combobox2.get()

        print("map_type",map_type)
        print("map_year",map_year)

        if map_type is not "" and map_year is not "":

            # TODO: Get the coordinate and location of the street with the most traffic/accidents from the list specified by map_type and map_year

            map_object = Map(map_type, map_year)  # Map(map_type,map_year,map_coordinate, map_location)
            # Update status on GUI
            # self.update_deposit_label("" + map_object.get_File_Name() + "\ncreated")
            print("open_map making file")


        else:
            #self.update_deposit_label("Error: Select Type/Year")
            print("Error")
    
    """
    def update_deposit_label(self, status):
        print(status)
        #self.status_txt.set("successfully loaded database")
        self.status_txt.set(status)
        print("update_deposit_label")
        return self.status_txt
    """

"""
def main():
    CalgaryTrafficGUI()

"""
def main():
    root = Tk()
    CalgaryTrafficGUI(root)
    root.mainloop()



if __name__ == '__main__':
    main()
