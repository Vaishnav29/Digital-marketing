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
off = pickle.load(open('pcat.p', 'rb'))
off_prod = pickle.load(open("off_prod.p", "rb"))
fur_prod = pickle.load(open("fur_prod.p", "rb"))
tec_prod = pickle.load(open("tec_prod.p", "rb"))

# window configuration
root = Tk()
root.geometry("900x600")
root.configure(background='RoyalBlue3')
root.title("DM-Inventory Management")
root.resizable(0,0)
Month = list(range(1,13))
Year = [2014,2015,2016,2017]
Category = ['Office Supplies','Furniture','Technology']
BMW = ['Best', 'Moderate', 'Worst']
offsub = ['Binders', 'Storage', 'Appliances', 'Paper', 'Art', 'Envelopes', 'Fasteners', 'Labels', 'Supplies']
fursub = ['Chairs', 'Bookcases', 'Furnishings', 'Tables']
tecsub = ['Copiers', 'Accessories', 'Machines', 'Phones']
sub = [offsub, fursub, tecsub]

rate = StringVar(root)
rate.set('a')
rateDrop = OptionMenu(root, rate, *BMW)

subname = StringVar(root)
sub_sel = ['a']
subname.set('a')
scnameDropDown = OptionMenu(root, subname, *sub_sel)

p = StringVar(root)
product_list = [0]
pDropDown = OptionMenu(root, p, *product_list)


def gsummary(*ar):
    v = p.get()
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
        listi.insert(END, 'Name of the product :')
        listi.insert(END, v)
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
        listi.insert(END, 'Name of the product :')
        listi.insert(END, v)
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
        listi.insert(END, 'Name of the product :')
        listi.insert(END, v)
        listi.insert(END, 'Quantity sold in last 3 months     : {}'.format(ltq))
        listi.insert(END, 'Remaining quantity in inventory : {}'.format(val))
        listi.insert(END, 'Predicted sales                                : {}'.format(pre))
        if(val < 15):
            messagebox.showinfo("Add inventory alert", "This product quantity is running low. Increase the inventory for this product!!!")

    elif v == 'Nothing to select':
        listi.delete(0, END)
        listi.insert(END, "*Nothing to display*")
    
    else:
        val =  lis_inv[inv_mon_name[-1]][v]
        print("Remaining quantity in inventory", val)
        print('Not Sold in last THREE MONTHS!!!')
        pre = pred[v]
        print("Predicted sales:", pre)
        listi.delete(0, END)
        listi.insert(END, '                 Not Sold in last THREE MONTHS!!!')
        listi.itemconfig(END, foreground="purple")
        listi.insert(END, 'Name of the product :')
        listi.insert(END, v)
        listi.insert(END, 'Remaining quantity in inventory     : {}'.format(val))
        listi.insert(END, 'Predicted sales                                : {}'.format(pre))
        if(val < 15):
            messagebox.showinfo("Add inventory alert", "This product quantity is running low. Increase the inventory for this product!!!")
     
    
# function to get product summary on selecting a product
def getpname(*val):
    c = cat.get()
    v = subname.get()
    r = rate.get()
    global p
    global pDropDown
    pDropDown.destroy()
    print(c, v, r)
    p = StringVar(root)
    if c == 'Office Supplies':
        if r == 'Best':
            for i in range(len(sub[0])):
               if v == sub[0][i]:
                product_list = off_prod[0][i]
                if len(product_list) > 0:
                    p.set(product_list[0])
                else:
                    product_list = ['Nothing to select']
                    p.set(product_list[0])
                    listi.delete(0, END)
                    listi.insert(END, "*Nothing to display*")
                p.trace("w", gsummary)
                pDropDown = OptionMenu(root, p, *product_list)
                pDropDown.configure(width = 30, anchor = 'w')
                pDropDown.place(relx = 0.21, rely = 0.41)
        elif r == 'Moderate':
            for i in range(len(sub[0])):
               if v == sub[0][i]:
                product_list = off_prod[1][i]
                if len(product_list)> 0:
                    p.set(product_list[0])
                else:
                    product_list = ['Nothing to select']
                    p.set(product_list[0])
                    listi.delete(0, END)
                    listi.insert(END, "*Nothing to display*")
                p.trace("w", gsummary)
                pDropDown = OptionMenu(root, p, *product_list)
                pDropDown.configure(width = 30, anchor = 'w')
                pDropDown.place(relx = 0.21, rely = 0.41)
        else:
            for i in range(len(sub[0])):
               if v == sub[0][i]:
                product_list = off_prod[2][i]
                if len(product_list)> 0:
                    p.set(product_list[0])
                else:
                    product_list = ['Nothing to select']
                    p.set(product_list[0])
                    listi.delete(0, END)
                    listi.insert(END, "*Nothing to display*")
                p.trace("w", gsummary)
                pDropDown = OptionMenu(root, p, *product_list)
                pDropDown.configure(width = 30, anchor = 'w')
                pDropDown.place(relx = 0.21, rely = 0.41)
                
    elif c == 'Furniture':
        if r == 'Best':
            for i in range(len(sub[1])):
               if v == sub[1][i]:
                product_list = fur_prod[0][i]
                if len(product_list) > 0:
                    p.set(product_list[0])
                else:
                    product_list = ['Nothing to select']
                    p.set(product_list[0])
                    listi.delete(0, END)
                    listi.insert(END, "*Nothing to display*")
                p.trace("w", gsummary)
                pDropDown = OptionMenu(root, p, *product_list)
                pDropDown.configure(width = 30, anchor = 'w')
                pDropDown.place(relx = 0.21, rely = 0.41)
        elif r == 'Moderate':
            for i in range(len(sub[1])):
               if v == sub[1][i]:
                product_list = fur_prod[1][i]
                if len(product_list)> 0:
                    p.set(product_list[0])
                else:
                    product_list = ['Nothing to select']
                    p.set(product_list[0])
                    listi.delete(0, END)
                    listi.insert(END, "*Nothing to display*")
                p.trace("w", gsummary)
                pDropDown = OptionMenu(root, p, *product_list)
                pDropDown.configure(width = 30, anchor = 'w')
                pDropDown.place(relx = 0.21, rely = 0.41)
        else:
            for i in range(len(sub[1])):
               if v == sub[1][i]:
                product_list = fur_prod[2][i]
                if len(product_list)> 0:
                    p.set(product_list[0])
                else:
                    product_list = ['Nothing to select']
                    p.set(product_list[0])
                    listi.delete(0, END)
                    listi.insert(END, "*Nothing to display*")
                p.trace("w", gsummary)
                pDropDown = OptionMenu(root, p, *product_list)
                pDropDown.configure(width = 30, anchor = 'w')
                pDropDown.place(relx = 0.21, rely = 0.41)
                
    else:
        if r == 'Best':
            for i in range(len(sub[2])):
               if v == sub[2][i]:
                product_list = tec_prod[0][i]
                if len(product_list) > 0:
                    p.set(product_list[0])
                else:
                    product_list = ['Nothing to select']
                    p.set(product_list[0])
                    listi.delete(0, END)
                    listi.insert(END, "*Nothing to display*")
                p.trace("w", gsummary)
                pDropDown = OptionMenu(root, p, *product_list)
                pDropDown.configure(width = 30, anchor = 'w')
                pDropDown.place(relx = 0.21, rely = 0.41)
        elif r == 'Moderate':
            for i in range(len(sub[2])):
               if v == sub[2][i]:
                product_list = tec_prod[1][i]
                if len(product_list)> 0:
                    p.set(product_list[0])
                else:
                    product_list = ['Nothing to select']
                    p.set(product_list[0])
                    listi.delete(0, END)
                    listi.insert(END, "*Nothing to display*")
                p.trace("w", gsummary)
                pDropDown = OptionMenu(root, p, *product_list)
                pDropDown.configure(width = 30, anchor = 'w')
                pDropDown.place(relx = 0.21, rely = 0.41)
        else:
            for i in range(len(sub[2])):
               if v == sub[2][i]:
                product_list = tec_prod[2][i]
                if len(product_list)> 0:
                    p.set(product_list[0])
                else:
                    product_list = ['Nothing to select']
                    p.set(product_list[0])
                    listi.delete(0, END)
                    listi.insert(END, "*Nothing to display*")
                p.trace("w", gsummary)
                pDropDown = OptionMenu(root, p, *product_list)
                pDropDown.configure(width = 30, anchor = 'w')
                pDropDown.place(relx = 0.21, rely = 0.41)
    lisdis.delete(0, END)
    j = 1   
    if product_list[0] == 'Nothing to select':
        lisdis.insert(END, "*Nothing to display*")
    else:
        for i in product_list:
            lisdis.insert(END, '{}. {}'.format(j, i))
            j +=1
                

def getrate(*val):
    print(subname.get())
    global rate
    global rateDrop
    rateDrop.destroy()
    rate = StringVar(root)
    rate.set(BMW[0])
    rate.trace("w", getpname)
    rateDrop = OptionMenu(root, rate, *BMW)
    rateDrop.configure(width = 10, anchor = 'w')
    rateDrop.place(relx = 0.21, rely = 0.285)
        
# function to get a list of products on selecting category        
def getYM(val):
    global s
    global subname
    global sub_sel
    global scnameDropDown
    scnameDropDown.destroy()
   
    c = cat.get()
    if c == 'Office Supplies':
        sub_sel = sub[0]
    elif c == 'Furniture':
        sub_sel = sub[1]
    else:
        sub_sel = sub[2]
    print(c)
    subname = StringVar(root)
    subname.set(sub_sel[0])
    subname.trace("w", getrate)  # calls getpname() when a product is chosen from the list
    scnameDropDown = OptionMenu(root, subname, *sub_sel)
    scnameDropDown.configure(width = 10, anchor = 'w')
    scnameDropDown.place(relx = 0.21, rely = 0.165)

catLabel = Label(root,text='Select Category : ', background='RoyalBlue3', fg = 'white')
catLabel.place(relx = 0.05, rely = 0.05)

pLabel = Label(root,text='Select Sub-Category : ', background='RoyalBlue3', fg = 'white')
pLabel.place(relx = 0.05, rely = 0.17)

proL = Label(root,text='Select Rating : ', background='RoyalBlue3', fg = 'white')
proL.place(relx = 0.05, rely = 0.295)

Label(root, text = 'Select Product : ', background='RoyalBlue3', fg = 'white').place(relx = 0.05, rely = 0.415)
             
cat = StringVar(root)
cat.set(Category[0])
catDropdown = OptionMenu(root,cat,*Category, command=getYM)
catDropdown.configure(width = 13, anchor = 'w')
catDropdown.place(relx = 0.21, rely = 0.05)

catLabel = Label(root,text='Summary of selected product : ', background='RoyalBlue3', fg = 'white')
catLabel.place(relx = 0.62, rely = 0.55)   

Label(root, text = 'List of products : ', background='RoyalBlue3', fg = 'white').place(relx = 0.62, rely = 0.06)

lisdis = Listbox(root, width = 60, height = 15)
lisdis.place(relx = 0.545, rely = 0.1)

listi = Listbox(root, width = 45, height = 7)
listi.place(relx = 0.6, rely = 0.59)


root.mainloop()