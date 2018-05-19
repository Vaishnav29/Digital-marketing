from tkinter import *
import os
import tkinter.font as tkFont


root = Tk()
root.title('Digital Marketing')
root.geometry("900x600")
root.resizable(0,0)
root.config(background = 'RoyalBlue3')
#customfont = tkFont.Font(family="Verdana",weight='bold',size=20)
#label = Label(root, borderwidth= 10, background= '#ffffff', text='Smart Store', font=customfont)
label = Label(root,  text='Digital Marketing Assistant', background='#ffffff', fg = 'black', font=("Verdana", 20,'bold', 'italic'))  
label.place(relx=0.28,rely=0.09)
def inventoryManagement():
    os.system('start python in_gui.py')
    
def targetmarketing():
    os.system('start python Targetfinal.py')
    
def personalised():
    os.system('start python personalised_gui.py')
    
def customer():
    os.system('start python customer_seg_gui.py')
    
def pricing():
    os.system('start python pricing_gui1.py')    


def cust_recommendation():
    os.system('start python personalised_gui_new.py')

def discount():
    os.system('start python discount_gui.py')


customer = Button(root, background = '#E4F1FE',text = "Customer       Segmentation", padx = 50, pady = 30, wraplength=90, command=customer)
customer.place(relx=0.11,rely=0.25)

target = Button(root, background = '#E4F1FE',text = "Targeted         Marketing", padx = 60, pady = 35, wraplength=90, command = targetmarketing)
target.place(relx= 0.41,rely=0.25)

visualization = Button(root, background = '#E4F1FE',text = "Customer Recommendation", padx = 40, pady = 35, wraplength=95, command=cust_recommendation)
visualization.place(relx= 0.71,rely=0.25)

personalized = Button(root, background = '#E4F1FE',text = "Personalized   Experience", padx = 50, pady = 35, wraplength=90, command = personalised)
personalized.place(relx= 0.11,rely=0.5)

pricing = Button(root, background = '#E4F1FE',text = "Pricing        Strategy", padx = 60, pady = 30, wraplength=90, command=pricing)
pricing.place(relx= 0.41,rely=0.5)

discount = Button(root, background= '#E4F1FE',text='Discount',padx = 60, pady = 35, wraplength=95, command=discount)
discount.place(relx=0.71,rely=0.5)

inventory = Button(root, background = '#E4F1FE',text = "Inventory      Management", padx = 50, pady = 30, wraplength=90, command=inventoryManagement)
inventory.place(relx = 0.41, rely=0.75)


root.mainloop()
