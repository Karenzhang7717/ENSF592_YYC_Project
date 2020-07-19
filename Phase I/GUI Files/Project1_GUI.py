from Read_db import *
from Map import *
from tkinter import *
from tkinter import ttk
import pandas as pd
from pymongo import MongoClient


class CalgaryTrafficGUI:

    def __init__(self):
        root = Tk()

        left = Frame(root, width=300, height=1500, borderwidth=2, relief="solid", bg="#a6a6a6")
        self.right = Frame(root, width=800, height=1500, borderwidth=2, relief="solid")

        label1 = ttk.Label(left, text="Type")
        self.combobox1 = ttk.Combobox(left, text="type", width=15)
        self.combobox1['value'] = ("Traffic Volume", "Accident")

        label2 = ttk.Label(left, text="Year")
        self.combobox2 = ttk.Combobox(left, width=15)
        self.combobox2['value'] = ("2016", "2017", "2018")

        btn1 = Button(left, text="Read", height=3, width=20, command=read_2016)
        btn2 = Button(left, text="Sort", height=3, width=20)
        btn3 = Button(left, text="Analysis", height=3, width=20)
        btn4 = Button(left, text="Map", height=3, width=20, command=open_map)

        label3 = ttk.Label(left, text="status:")

        self.status_txt = StringVar()
        self.status_txt.set('status messages')
        label4 = ttk.Label(left, textvariable=self.status_txt)

        left.pack(side="left", expand=True, fill="both")
        self.right.pack(side="right", expand=True, fill="both")

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

        root.mainloop()


    def read_data(type_, year):
        """
        Return traffic record for the specified type and year
        :param type_: a string of either 'Vol' for traffic volume or 'Accident' for traffic accidents
        :param year: a string for year '2016', '2017' or '2018'
        :return: traffic records stored in a dataframe
        """
        client = MongoClient()
        db = client['CalgaryTraffic' + type_ + year]
        df = pd.DataFrame(list(db[type_ + year].find())).drop(columns = '_id')
        return df


    def read_2016(self):
        df_volume2016 = read_data('Vol', '2016')

        df = pd.DataFrame(df_volume2016)
        cols = list(df.columns)

        tree = ttk.Treeview(self.right)
        tree.pack()
        tree["columns"] = cols
        for i in cols:
            tree.column(i, anchor="w")
            tree.heading(i, text=i, anchor='w')

        for index, row in df.iterrows():
            tree.insert("",0,text=index,values=list(row))


        tree.pack()


    def open_map(self):
        # Map Constructor Definition:
        #  Map(self, data_kind = 'Traffic_Incidents', data_year = '2017',
        #  marker_coordinates = [51.03706737,-114.1123288],
        #  location = "17 Avenue at Richmond Road SW",
        #   map_base_coordinates = [51.044270, -114.062019]):

        #Get the type and year user has selected
        map_type = self.combobox1.get()
        map_year = self.combobox2.get()

        if(map_type is not "" and map_year is not ""):

            #TODO: Get the coordinate and location of the street with the most trafiic/accidents from the list specified by map_type and map_year

            map_object = Map(map_type, map_year) # Map(map_type,map_year,map_coordinate, map_location)
            # Update status on GUI
            self.updateDepositLabel(""+map_object.get_File_Name()+"\ncreated")

        else:
            self.updateDepositLabel("Error: Select Type/Year")


    def updateDepositLabel(self, status) :
        #status_txt.set("successfully loaded database")
        self.status_txt.set(status)
        return self.status_txt


def main():
    CalgaryTrafficGUI()


if __name__ == '__main__':
    main()