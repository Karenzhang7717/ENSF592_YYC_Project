#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 15:49:16 2020

@author: kailunzhang
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:00:03 2020

@author: kailunzhang
"""


from tkinter import *
from tkinter import ttk

root = Tk()


left = Frame(root, width=300,height=1500,borderwidth=2, relief="solid",bg = "#a6a6a6")
right = Frame(root, width=800,height=1500,borderwidth=2, relief="solid")


label1 = ttk.Label(left, text = "Type")
combobox1 = ttk.Combobox(left,text="type",width = 15)
combobox1['value'] = ("Traffic Volume","Accident")


label2 = ttk.Label(left,text = "Year")
combobox2 = ttk.Combobox(left,width = 15 )
combobox2['value'] = ("2016","2017","2018")

# =============================================================================
# btn1 = Button(left,text="Read",height=3,width=20,command = read_data) 
# btn2 = Button(left,text="Sort",height=3,width=20,command = sort_data)   
# btn3 = Button(left,text="Analysis",height=3,width=20,command = analyze_data)  
# btn4 = Button(left,text="Map",height=3,width=20,command = open_map) 
# =============================================================================


btn1 = Button(left,text="Read",height=3,width=20) 
btn2 = Button(left,text="Sort",height=3,width=20)   
btn3 = Button(left,text="Analysis",height=3,width=20)  
btn4 = Button(left,text="Map",height=3,width=20) 

label3=ttk.Label(left, text = "status:")

status_txt = StringVar()
status_txt.set('status messages')
label4 = ttk.Label(left,textvariable=status_txt)

def updateDepositLabel() :
    status_txt.set("successfully loaded database")
    return status_txt

left.pack(side="left", expand=True, fill="both")
right.pack(side="right", expand=True, fill="both")

label1.pack()
combobox1.pack()
label2.pack()
combobox2.pack()

btn1.pack(pady=20)
btn2.pack(pady=20)
btn3.pack(pady=20)
btn4.pack(pady=20)
label3.pack(pady=10)
label4.pack()


root.mainloop()


def read_data(file):
    pass

def sort_data(file):
    pass


def analyze_data(file):
    pass


def open_map():
    pass
