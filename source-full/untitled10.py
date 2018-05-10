from tkinter import *
from sqlite3 import dbapi2 as sqlite
import win32api
import win32print
import random
import time    

    global c, cur, flag, t, name, name1, add, billingsto, names, qty, sl, qtys,n, namee, lb1
    t=0
    
    names=[]
    qty=[]
    sl=[]
    n=[]
    qtys=['']*10
    
    flag='billingsto'
    billingsto=Tk()
    billingsto.title('BILLING')
    #billingsto.wm_iconbitmap('favicon.ico')
    Label(billingsto,text='-'*48+'Billing'+'-'*49).grid(row=0,column=0,columnspan=7,sticky='W')
    Label(billingsto,text='Enter Name: ').grid(row=1,column=0)
    name1=Entry(billingsto)
    name1.grid(row=1, column=1)
    Label(billingsto,text='Enter Address: ').grid(row=2,column=0)
    add=Entry(billingsto)
    add.grid(row=2, column=1)
    
    Label(billingsto,text='-'*115).grid(row=6, column=0,columnspan=7,sticky='W')
    Label(billingsto,text='Select Item',relief='ridge',width=15).grid(row=7,column=0)
    Label(billingsto,text='Qty_Remain',relief='ridge',width=10).grid(row=7,column=1)
    Label(billingsto,text='Cost',relief='ridge',width=4).grid(row=7,column=2)
    Label(billingsto,text='Expiry Date',width=10,relief='ridge').grid(row=7,column=3)
   
    Button(billingsto,text='Add to bill',width=15).grid(row=8, column=6)
    Label(billingsto,text='QUANTITY',width=20,relief='ridge').grid(row=7, column=5)
    qtys=Entry(billingsto)
    qtys.grid(row=8,column=5)
    #refresh()
    Button(billingsto,width=15,text='Main Menu').grid(row=1,column=6)
    Button(billingsto,width=15,text='Refresh Stock').grid(row=3,column=6)
    Button(billingsto,width=15,text='Reset Bill').grid(row=4,column=6)
    Button(billingsto,width=15,text='Print Bill').grid(row=5,column=6)
    Button(billingsto,width=15,text='Save Bill').grid(row=7,column=6)
    
    billingsto.mainloop()