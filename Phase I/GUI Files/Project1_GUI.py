#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:23:41 2020

@author: kailunzhang
"""

import tkinter as tk
from tkinter import ttk
 
 
window = tk.Tk()
window.minsize(600, 400)

window.title("YYC Traffic")
window.wm_iconbitmap('icon.ico')
 
#def chosingTypes():
  #  label1.configure(text = "You Have Choosed "
 
#create first label, Type and combobox
label1 = ttk.Label(window, text = "Type")
label1.grid(column = 0, row = 0)
 


#combobox1 = ttk.Combobox(window, width = 15 , textvariable = mytype)
combobox1 = ttk.Combobox(window, width = 15)
combobox1['value'] = ("Traffic Volume","Accident")
combobox1.grid(column = 1, row = 0)
 
#create second label, Year and combobox
label2 = ttk.Label(window, text = "Year")
label2.grid(column = 0, row = 1)
combobox2 = ttk.Combobox(window, width = 15 )
combobox2['value'] = ("2016","2017","2018")
combobox2.grid(column = 1, row = 1)



#button = ttk.Button(window, text = "Click Me", command = chosingTypes)
#button.grid(column = 1, row = 5)
 
 
 
window.mainloop()