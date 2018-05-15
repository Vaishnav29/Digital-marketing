from tkinter import *
import pandas as pd
import pickle
from tkinter import messagebox

data = pickle.load(open('pcat.p', 'rb'))
last3 = pickle.load(open('last3mon.p', 'rb'))
lis_inv = pickle.load(open("lis_inv.p", "rb"))
inv_mon_name = pickle.load(open("inv_mon_name.p", "rb"))
pred = pickle.load(open("predsales.p", "rb"))

root = Tk()
root.geometry("900x600")
root.title("DM-Inventory Management")
root.resizable(0,0)
Month = list(range(1,13))
Year = [2014,2015,2016,2017]
Category = ['Office Supplies','Furniture','Technology']

catLabel = Label(root,text='Select Category : ')
catLabel.place(relx = 0.1, rely = 0.15)

cat = StringVar(root)
cat.set(Category[0])
catDropdown = OptionMenu(root,cat,*Category)
catDropdown.configure(width = 13, anchor = 'w')
catDropdown.place(relx = 0.21, rely = 0.15)

pname = StringVar(root)
product_list = [0]
pnameDropDown = OptionMenu(root, pname, *product_list)
pLabel = Label(root,text='Select Product')


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
        listi.insert(END, 'Quantity sold in last 3 months: {}'.format(ltq))
        listi.insert(END, 'Remaining quantity in inventory: {}'.format(val))
        listi.insert(END, 'Best Product')
        listi.insert(END, 'Predicted sales: {}'.format(pre))
        if(val < 15):
            messagebox.showinfo("Add inventory alert", "This product quantity is running low. Increse the inventory for this product!!!")
        else:
            messagebox.showinfo("Inventory alert", "Enough inventory. No need to increse inventory for this product!!!")
            
            
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
        listi.insert(END, 'Quantity sold in last 3 months: {}'.format(ltq))
        listi.insert(END, 'Remaining quantity in inventory: {}'.format(val))
        listi.insert(END, 'Moderate Product')
        listi.insert(END, 'Predicted sales: {}'.format(pre))
        if(val < 15):
            messagebox.showinfo("Add inventory alert", "This product quantity is running low. Increse the inventory for this product!!!")
        else:
            messagebox.showinfo("Inventory alert", "Enough inventory. No need to increse inventory for this product!!!")
            
        
    elif v in h3:
        for j in range(len(last3)):
            if last3['d_product'][j] == v:
                z=j
        ltq= last3['d_quantity'][z]   
        print("Quantity sold in last 3 months: ", ltq)
        val =  lis_inv[inv_mon_name[-1]][v]
        print("Remaining quantity in inventory", val)
        #count+=1  
        print('Worst Product')
        pre = pred[v]
        print("Predicted sales:", pre)
        listi.delete(0, END)
        listi.insert(END, 'Quantity sold in last 3 months: {}'.format(ltq))
        listi.insert(END, 'Remaining quantity in inventory: {}'.format(val))
        listi.insert(END, 'Worst Product')
        listi.insert(END, 'Predicted sales: {}'.format(pre))
        if(val < 15):
            messagebox.showinfo("Add inventory alert", "This product quantity is running low. Increse the inventory for this product!!!")
        else:
            messagebox.showinfo("Inventory alert", "Enough inventory. No need to increse inventory for this product!!!")
            
        
    else:
        val =  lis_inv[inv_mon_name[-1]][v]
        print("Remaining quantity in inventory", val)
        #count+=1
        print('Not Sold in last THREE MONTHS!!!')
        pre = pred[v]
        print("Predicted sales:", pre)
        listi.delete(0, END)
        listi.insert(END, 'Remaining quantity in inventory: {}'.format(val))
        listi.insert(END, 'Not Sold in last THREE MONTHS!!!')
        listi.insert(END, 'Predicted sales: {}'.format(pre))
        if(val < 15):
            messagebox.showinfo("Add inventory alert", "This product quantity is running low. Increse the inventory for this product!!!")
        else:
            messagebox.showinfo("Inventory alert", "Enough inventory. No need to increse inventory for this product!!!")
            
        
def getYM():
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
    
    pLabel = Label(root,text='Select Product : ')
    pLabel.place(relx = 0.1, rely = 0.32)
    pname.trace("w", getpname)
    pnameDropDown = OptionMenu(root, pname, *product_list)
    pnameDropDown.configure(width = 30, anchor = 'w')
    pnameDropDown.place(relx = 0.2, rely = 0.315)
    
    print(len(product_list))

catLabel = Label(root,text='Product Summary : ')
catLabel.place(relx = 0.685, rely = 0.31)    
    
listi = Listbox(root, width = 45, height = 10)
listi.place(relx = 0.6, rely = 0.35)

btn = Button(root,text="Get Products",command=getYM)
btn.place(relx = 0.36, rely = 0.155)

root.mainloop()