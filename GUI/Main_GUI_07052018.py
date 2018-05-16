from tkinter import *
import os
root = Tk()
root.title('Digital Marketing')
root.geometry("900x600")
root.config(background = '#7E85AB')
root.resizable(0,0)
label = Label(root, borderwidth= 10, background= '#7E85AB', text='Welcome to Digital Marketing Portal!', font=36)
label.place(relx=0.4,rely=0.05)

    
def inventoryManagement():
    os.system('python inventory_gui.py')
    print("hello")
    
    
def targetmarketing():
    os.system('python Targetfinal.py')
    
def personalised():
    os.system('python personalised_gui.py')

#style = ttk.Style()
#style.configure("BW.TLabel", foreground="black", background="white")

inventory = Button(root,foreground="black", text = "Inventory Managemnet", padx = 50, pady = 30, wraplength=80, command=inventoryManagement)
inventory.place(relx = 0.1,rely = 0.15)
pricing = Button(root,text = "Pricing Strategy", padx = 50, pady = 30, wraplength=80)
pricing.place(relx= 0.45,rely=0.15)
customer = Button(root, text = "Customer Segmentation", padx = 50, pady = 30, wraplength=80)
customer.place(relx= 0.75,rely=0.15)
target = Button(root, text = "Targert Marketing", padx = 50, pady = 30, wraplength=80, command = targetmarketing)
target.place(relx= 0.1,rely=0.455)
#smart = Button(root, background = '#759EBD',text = "Smart Advertising", padx = 50, pady = 30, wraplength=80)
#smart.place(relx= 0.45,rely=0.455)
personalized = Button(root, text = "Personalized Experience", padx = 50, pady = 30, wraplength=80, command = personalised)
personalized.place(relx= 0.45,rely=0.455)
def openBokeh():
    os.system('bokeh serve --show C:/Users/user/Desktop/dashboard')
visualization = Button(root, text = "Visualization", padx = 50, pady = 30, wraplength=80, command=openBokeh)
visualization.place(relx= 0.75,rely=0.455)

root.mainloop()
