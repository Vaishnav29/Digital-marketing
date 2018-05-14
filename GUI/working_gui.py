# -*- coding: utf-8 -*-
"""
Created on Mon May  7 21:06:09 2018

@author: user
"""

from tkinter import *
import pandas as pd

data = pd.read_excel('C:\\Users\\user\\Desktop\\store-dataset.xlsx')

root = Tk()
root.geometry("900x600")
root.title("DM-Inventory Management")
Month = list(range(1,13))
Year = [2014,2015,2016,2017]
Category = ['Office Supplies','Furniture','Technology']

catLabel = Label(root,text='Select Category')
catLabel.place(relx = 0.05, rely = 0.05)

cat = StringVar(root)
cat.set('Furniture')
catDropdown = OptionMenu(root,cat,*Category)
catDropdown.place(relx = 0.05, rely = 0.09)

yearLabel = Label(root,text='Select Year')
yearLabel.place(relx = 0.2, rely = 0.05)

year = IntVar(root)
year.set(2014)
yearDropdown = OptionMenu(root,year,*Year)
yearDropdown.place(relx = 0.2, rely = 0.09)

monthLabel = Label(root,text='Select Month')
monthLabel.place(relx = 0.3, rely = 0.05)

month = IntVar(root)
month.set(1)
monthDropdown = OptionMenu(root,month,*Month)
monthDropdown.place(relx = 0.3, rely = 0.09)
#list_of_string=[]
global pLabel
global pnameDropDown
global pname
global s
def getYM():
    global s
    global pLabel
    global pnameDropDown
    pLabel.destroy()
    pnameDropDown.destroy()
   
    m = month.get()
    y = year.get()
    c = cat.get()
    
# =============================================================================
#     if str(m)+str(y)+str(c) in list_of_string:
#         return
#     else:
#         list_of_string.append(str(m)+str(y)+str(c))
# =============================================================================
    print(y,m,c)
    product_list = list(data[(data['Order Date'].dt.year==y) & (data['Order Date'].dt.month==m) & (data['Category']==c)]['Product Name'])
    
    pname = StringVar(root)
    pname.trace('w',callback)
    pname.set(product_list[0])
    
    pLabel = Label(root,text='Select Product')
    pLabel.place(relx = 0.2, rely = 0.18)
    
    pnameDropDown = OptionMenu(root, pname, *product_list)
    pnameDropDown.place(relx = 0.2, rely = 0.22)
    
    #print(product_list)
    
    print(len(product_list))
    #s = pnameDropDown.selection_get()
    #print(pname.get())
    
def callback(*args):
    print(pname.get())
btn = Button(root,text="Get Products",command=getYM)
btn.place(relx = 0.4, rely = 0.09)
pname = StringVar(root)
product_list = [0]
pnameDropDown = OptionMenu(root, pname, *product_list)
pLabel = Label(root,text='Select Product')
root.mainloop()