
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 15:14:00 3018

@author: user
"""

from tkinter import *
import os
root = Tk()
root.title('Digital Marketing')
root.geometry("900x600")
root.config(background = '#EEC774')
label = Label(root, borderwidth= 10, background= '#B0E5B9', text='Welcome to Digital Marketing Portal!', font=36)
label.place(relx=0.4,rely=0.05)
def inventoryManagement():
    os.system('python C:/Users/user/Desktop/working_gui.py')
inventory = Button(root, background = '#759EBD',text = "Inventory Managemnet", padx = 50, pady = 30, wraplength=80, command=inventoryManagement)
inventory.place(relx = 0.1,rely = 0.15)
pricing = Button(root, background = '#759EBD',text = "Pricing Strategy", padx = 50, pady = 30, wraplength=80)
pricing.place(relx= 0.45,rely=0.15)
customer = Button(root, background = '#759EBD',text = "Customer Segmentation", padx = 50, pady = 30, wraplength=80)
customer.place(relx= 0.75,rely=0.15)
target = Button(root, background = '#759EBD',text = "Targert Marketing", padx = 50, pady = 30, wraplength=80)
target.place(relx= 0.1,rely=0.455)
smart = Button(root, background = '#759EBD',text = "Smart Advertising", padx = 50, pady = 30, wraplength=80)
smart.place(relx= 0.45,rely=0.455)
personalized = Button(root, background = '#759EBD',text = "Personalized Experience", padx = 50, pady = 30, wraplength=80)
personalized.place(relx= 0.75,rely=0.455)
def openBokeh():
    os.system('bokeh serve --show C:/Users/user/Desktop/dashboard')
visualization = Button(root, background = '#759EBD',text = "Visualization", padx = 50, pady = 30, wraplength=80, command=openBokeh)
visualization.place(relx= 0.45,rely=0.76)

root.mainloop()