from tkinter import *
import pandas as pd
import pickle
from tkinter import messagebox
from tkinter import font

# loading dumped datafiles(pickles from managing_inventory.py)
data = pickle.load(open('pcat.p', 'rb'))
last3 = pickle.load(open('last3mon.p', 'rb'))
lis_inv = pickle.load(open("lis_inv.p", "rb"))
inv_mon_name = pickle.load(open("inv_mon_name.p", "rb"))
pred = pickle.load(open("predsales.p", "rb"))

# window configuration
root = Tk()
root.geometry("900x600")
root.configure(background='#7E85AB')
root.title("DM-Inventory Management")
root.resizable(0,0)
Month = list(range(1,13))
Year = [2014,2015,2016,2017]
Category = ['Office Supplies','Furniture','Technology']

pname = StringVar(root)
product_list = [0]
pnameDropDown = OptionMenu(root, pname, *product_list)
pLabel = Label(root,text='Select Product')

# function to get product summary on selecting a product
def getpname(*val):
    v = pname.get()
    print(v)
    h1=list(last3[:370]['d_product'])
    h2=list(last3[371:1500]['d_product'])
    h3=list(last3[1500:]['d_product'])
    val = 0
    z = 0
        
    if v in h1:
        for j in range(len(last3)):
            if last3['d_product'][j] == v:
                z=j
        ltq= last3['d_quantity'][z]   
        print("Quantity sold in last 3 months: ", ltq)
        val =  lis_inv[inv_mon_name[-1]][v]
        print("Remaining quantity in inventory", val)
        print('Best Product')
        pre = pred[v]
        print("Predicted sales:", pre)
        listi.delete(0, END)
        listi.insert(END, '                         Best Product')
        listi.itemconfig(END, foreground="green")
        listi.insert(END, 'Quantity sold in last 3 months     : {}'.format(ltq))
        listi.insert(END, 'Remaining quantity in inventory : {}'.format(val))
        listi.insert(END, 'Predicted sales                                : {}'.format(pre))
        if(val < 15):
            messagebox.showinfo("Add inventory alert", "This product quantity is running low. Increase the inventory for this product!!!")
        
            
    elif v in h2:
        for j in range(len(last3)):
            if last3['d_product'][j] == v:
                z=j
        ltq= last3['d_quantity'][z]   
        print("Quantity sold in last 3 months: ", ltq)
        val =  lis_inv[inv_mon_name[-1]][v]
        print("Remaining quantity in inventory", val)
        print('Moderate Product')
        pre = pred[v]
        print("Predicted sales:", pre)
        listi.delete(0, END)
        listi.insert(END, '                         Moderate Product')
        listi.itemconfig(END, foreground="blue")
        listi.insert(END, 'Quantity sold in last 3 months     : {}'.format(ltq))
        listi.insert(END, 'Remaining quantity in inventory : {}'.format(val))
        listi.insert(END, 'Predicted sales                                : {}'.format(pre))
        if(val < 15):
            messagebox.showinfo("Add inventory alert", "This product quantity is running low. Increase the inventory for this product!!!")
        
    elif v in h3:
        for j in range(len(last3)):
            if last3['d_product'][j] == v:
                z=j
        ltq= last3['d_quantity'][z]   
        print("Quantity sold in last 3 months: ", ltq)
        val =  lis_inv[inv_mon_name[-1]][v]
        print("Remaining quantity in inventory", val)
        print('Worst Product')
        pre = pred[v]
        print("Predicted sales:", pre)
        listi.delete(0, END)
        listi.insert(END, '                         Worst Product')
        listi.itemconfig(END, foreground="red")
        listi.insert(END, 'Quantity sold in last 3 months     : {}'.format(ltq))
        listi.insert(END, 'Remaining quantity in inventory : {}'.format(val))
        listi.insert(END, 'Predicted sales                                : {}'.format(pre))
        if(val < 15):
            messagebox.showinfo("Add inventory alert", "This product quantity is running low. Increase the inventory for this product!!!")

        
    else:
        val =  lis_inv[inv_mon_name[-1]][v]
        print("Remaining quantity in inventory", val)
        print('Not Sold in last THREE MONTHS!!!')
        pre = pred[v]
        print("Predicted sales:", pre)
        listi.delete(0, END)
        listi.insert(END, '                 Not Sold in last THREE MONTHS!!!')
        listi.itemconfig(END, foreground="purple")
        listi.insert(END, 'Remaining quantity in inventory     : {}'.format(val))
        listi.insert(END, 'Predicted sales                                : {}'.format(pre))
        if(val < 15):
            messagebox.showinfo("Add inventory alert", "This product quantity is running low. Increase the inventory for this product!!!")
       
# function to get a list of products on selecting category        
def getYM(val):
    global s
    global pLabel
    global pname
    global pnameDropDown
    pLabel.destroy()
    pnameDropDown.destroy()
   
    c = cat.get()
    product_list = []
    print(c)
    
    for key,val in data.items():
        if val == c:
            product_list.append(key) 
    product_list = sorted(product_list)    
    pname = StringVar(root)
    pname.set(product_list[0])
    
    pLabel = Label(root,text='Select Product : ', background='#7E85AB', fg = 'white')
    pLabel.place(relx = 0.1, rely = 0.32)
    pname.trace("w", getpname)  # calls getpname() when a product is chosen from the list
    pnameDropDown = OptionMenu(root, pname, *product_list)
    pnameDropDown.configure(width = 30, anchor = 'w')
    pnameDropDown.place(relx = 0.2, rely = 0.315)
    
    print(len(product_list))

catLabel = Label(root,text='Select Category : ', background='#7E85AB', fg = 'white')
catLabel.place(relx = 0.1, rely = 0.15)

cat = StringVar(root)
cat.set(Category[0])
catDropdown = OptionMenu(root,cat,*Category, command=getYM)
catDropdown.configure(width = 13, anchor = 'w')
catDropdown.place(relx = 0.21, rely = 0.15)

catLabel = Label(root,text='Product Summary : ', background='#7E85AB', fg = 'white')
catLabel.place(relx = 0.685, rely = 0.31)    
    
listi = Listbox(root, width = 45, height = 10)
listi.place(relx = 0.6, rely = 0.35)

root.mainloop()