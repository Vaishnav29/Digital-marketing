import tkinter as tk
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from dm_function import sorted_profit1
from dm_function import predicted_sales
import pickle


root = tk.Tk()
root.geometry('900x600')
root.title('DM-Pricing')
root.resizable(0,0)
root.config(background='RoyalBlue3')
Year = [2014,2015,2016,2017]
Month = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
year = tk.IntVar(root)
month = tk.StringVar(root)
year.set(Year[0])
month.set(Month['Jan'])
yearLabel = tk.Label(root, text='Select Year and month')
yearLabel.place(relx = 0.32, rely = 0.05)
#monthLabel = tk.Label(root, text='Select Month')
yearOM = tk.OptionMenu(root, year, *Year)
yearOM.place(relx = 0.32, rely = 0.13)
monthOM = tk.OptionMenu(root, month, *Month.values())
#monthLabel.place(relx = 0.50, rely = 0.05)
monthOM.place(relx = 0.4, rely = 0.13)
Category = ['Best','Moderate','Worst High','Worst Low']
category = tk.StringVar(root)
category.set(Category[0])
categoryOM = tk.OptionMenu(root,category,*Category)
categoryLabel = tk.Label(root,text='Select Category')
categoryLabel.place(relx = 0.75, rely = 0.05)
categoryOM.place(relx = 0.75, rely = 0.13)
global new_data
global not_sold
global new_dict
global new_list
global l_best_new
global l_moderate_new
global l_worst_high_new
global l_worst_low_new
global profit_old_value
global profit_new_value
def showData():
    inv_mon_name = pickle.load(open("inv_mon_name.p", "rb"))
    inv_monsoldper_name = pickle.load(open("inv_monsoldper_name.p", "rb"))
    l = pickle.load(open("l.p", "rb"))
    lis_inv = pickle.load(open("lis_inv.p", "rb"))
    lis_inv_sold_per = pickle.load(open("lis_inv_sold_per.p", "rb"))
    data= pickle.load(open("4yrsBMW.p", "rb"))
    firstyear= pickle.load(open("firstyear.p", "rb"))
    secondyear= pickle.load(open("secondyear.p", "rb"))
    thirdyear= pickle.load(open("thirdyear.p", "rb"))
    fourthyear= pickle.load(open("fourthyear.p", "rb"))
    thirdfourth= pickle.load(open("thirdfourth.p", "rb"))
    twothree4= pickle.load(open("twothree4.p", "rb"))
    twothree= pickle.load(open("twothree.p", "rb"))
    onetwo= pickle.load(open("onetwo.p", "rb"))
    onetwo3=pickle.load(open("onetwo3.p", "rb"))
    lastdata1=pickle.load(open("last3mnthsBMW.p", "rb"))
    
    dataset1 = pd.DataFrame()
    m=[1,2,3]
    if(x==2017 and y in m):
        dataset1= thirdfourth
    elif(x==2017 and y not in m):
        dataset1=fourthyear  
    elif(x==2016 and y in m):
        dataset1=twothree    
    elif(x==2016 and  y not in m):
        dataset1= thirdyear
    elif(x==2015 and y in m):
        dataset1=onetwo
    elif(x==2015 and  y not in m):
        dataset1=secondyear
    
    else:
        dataset1=firstyear    
                
    dataset1 = dataset1.reset_index(drop=True)
    a = pd.DatetimeIndex(dataset1['Order Date']).year ==  x
    b = pd.DatetimeIndex(dataset1['Order Date']).month ==  y
    
    dataset2 = pd.DataFrame()
    for i in range(len(dataset1)):
        if(a[i]== True and b[i]==True):
        
            dataset2 = dataset2.append(dataset1.iloc[i,:])    
            
    dataset2 = dataset2.reset_index(drop=True)
    
    # setting inventory size    
    #l = list(dataset2['Product Name'].unique())
    inv_dict = {}
    inv_dict = lis_inv[inv_mon_name[((x - 2014)*12 + y)-1]]
    
    # sold, remaining % sold, adding inventory
    sold_percent = {} 
    if(x==2017):
        if(y==12):
            data1=lastdata1
        else:        
            data1= sorted_profit1(x,y)
    else:        
        data1= sorted_profit1(x,y)
    
                    
    #Code for Pricing according to best, worst and moderate product
    global new_data
    global not_sold
    global new_dict
    global new_list
    global l_best_new
    global l_moderate_new
    global l_worst_high_new
    global l_worst_low_new
    new_data= data1
    new_dict= {}
    new_list= list(dataset1['Product Name'].unique())
    l_best ={}
    l_best_new ={}
    l_moderate_new={}
    l_worst_high_new={}
    l_worst_low_new={}
    l_moderate={}
    l_worst_high={}
    l_worst_low ={}
    not_sold={}
    
    for i in range(0,len(new_data)):
        if (i<.2*len(new_data)):
            l_best[(new_data['d_product'][i])]= new_data['d_profit'][i]      
           
        elif (i>=.8*len(new_data)):
            if(new_data['d_quantity'][i] >= 5):
               l_worst_high[(new_data['d_product'][i])]= new_data['d_profit'][i]  
               
            else:
                    
                l_worst_low[(new_data['d_product'][i])]= new_data['d_profit'][i] 
                
        else:
            
            l_moderate[(new_data['d_product'][i])]= new_data['d_profit'][i]
    global profit_old_value
    if(category.get()=='Best'):
        a = []
        l_best_keys = list(l_best.keys())
        l_best_values = list(l_best.values())
        a = [str(i+1)+'. '+str(l_best_keys[i])[0:min(len(str(l_best_keys[i])),35)]+'    :'+str(l_best_values[i]) for i in range(len(l_best))]
        profit_old_value = sum(l_best_values)
    elif(category.get()=='Moderate'):
        a = []
        l_moderate_keys = list(l_moderate.keys())
        l_moderate_values = list(l_moderate.values())
        a = [str(i+1)+'. '+str(l_moderate_keys[i])[0:min(len(str(l_moderate_keys[i])),35)]+'    :'+str(l_moderate_values[i]) for i in range(len(l_moderate))]
        profit_old_value = sum(l_moderate_values)
    elif(category.get()=='Worst High'):
        a = []
        l_worst_high_keys = list(l_worst_high.keys())
        l_worst_high_values = list(l_worst_high.values())
        a = [str(i+1)+'. '+str(l_worst_high_keys[i])[0:min(len(str(l_worst_high_keys[i])),35)]+'    :'+str(l_worst_high_values[i]) for i in range(len(l_worst_high))]
        profit_old_value = sum(l_worst_high_values)
    elif(category.get()=='Worst Low'): 
        a = []
        l_worst_low_keys = list(l_worst_low.keys())
        l_worst_low_values = list(l_worst_low.values())
        a = [str(i+1)+'. '+str(l_worst_low_keys[i])[0:min(len(str(l_worst_low_keys[i])),35)]+'    :'+str(l_worst_low_values[i]) for i in range(len(l_worst_low))]
        profit_old_value = sum(l_worst_low_values)
    listbox_old.delete(0,max(len(l_best),len(l_moderate),len(l_worst_high),len(l_worst_low)))
    for i in range(len(a)):
        listbox_old.insert(i, a[i])
    profit_old_value = round(profit_old_value,2)
    profit_old = tk.Label(root,text=str(profit_old_value))
    profit_old.place(relx = 0.25, rely = 0.85)
         
global discount
def dispNew():
        global discount
        discount = int(discount_text.get('1.0'))  #int(input('Enter the Discount in % '))
        print(discount)
        for i in range(0,len(new_data)):
            if (i<.2*len(new_data) and category.get() == "Best" ):   
                new_data['d_MRP'][i]= new_data['d_MRP'][i]*(100-discount)/100
                new_data['d_profit'][i]= (new_data['d_MRP'][i]-new_data['d_inventory'][i])
                l_best_new[new_data['d_product'][i]]= new_data['d_profit'][i]
            elif (i>=.8*len(new_data)):
                if(new_data['d_quantity'][i] >= 5 and category.get() == "Worst High"):
                    
                   new_data['d_MRP'][i]= new_data['d_'][i]*(100-discount)/100
                   new_data['d_profit'][i]= (new_data['d_MRP'][i]-new_data['d_inventory'][i])
                   l_worst_high_new[new_data['d_product'][i]]= new_data['d_profit'][i]
                elif(new_data['d_quantity'][i] < 5 and category.get() == "Worst Low"):
                        
                    
                    new_data['d_MRP'][i]= new_data['d_MRP'][i]*(100-discount)/100
                    new_data['d_profit'][i]= (new_data['d_MRP'][i]-new_data['d_inventory'][i])
                    l_worst_low_new[new_data['d_product'][i]]= new_data['d_profit'][i]
            else:
                if (category.get() == "Moderate"):
                
                    new_data['d_MRP'][i]= new_data['d_MRP'][i]*(100-discount)/100
                    new_data['d_profit'][i]= (new_data['d_MRP'][i]-new_data['d_inventory'][i])
                    l_moderate_new[new_data['d_product'][i]]= new_data['d_profit'][i]
        for i in range(0,len(new_list)):
            flag=0
            for j in range(0,len(new_data)):
                if new_list[i]==new_data['d_product'][j]:
                    flag=1
                    break
            if flag==0:
                not_sold[(new_list[i])]= "Not Sold"
        global profit_new_value
        if(category.get()=='Best'):
            a = []
            l_best_new_keys = list(l_best_new.keys())
            l_best_new_values = list(l_best_new.values())
            l_best_new_values = [round(i,2) for i in l_best_new_values]
            a = [str(i+1)+'. '+str(l_best_new_keys[i])[0:min(len(str(l_best_new_keys[i])),35)]+'    :'+str(l_best_new_values[i]) for i in range(len(l_best_new))]
            profit_new_value = sum(l_best_new_values)
        elif(category.get()=='Moderate'):
            a = []
            l_moderate_new_keys = list(l_moderate_new.keys())
            l_moderate_new_values = list(l_moderate_new.values())
            l_moderate_new_values = [round(i,2) for i in l_moderate_new_values]
            a = [str(i+1)+'. '+str(l_moderate_new_keys[i])[0:min(len(str(l_moderate_new_keys[i])),35)]+'    :'+str(l_moderate_new_values[i]) for i in range(len(l_moderate_new))]
            profit_new_value = sum(l_moderate_new_values)
        elif(category.get()=='Worst High'):
            a = []
            l_worst_high_new_keys = list(l_worst_high_new.keys())
            l_worst_high_new_values = list(l_worst_high_new.values())
            l_worst_high_new_values = [round(i,2) for i in l_worst_high_new_values]
            a = [str(i+1)+'. '+str(l_worst_high_new_keys[i])[0:min(len(str(l_worst_high_new_keys[i])),35)]+'    :'+str(l_worst_high_new_values[i]) for i in range(len(l_worst_high_new))]
            profit_new_value = sum(l_worst_high_new_values)
        elif(category.get()=='Worst Low'): 
            a = []
            l_worst_low_new_keys = list(l_worst_low_new.keys())
            l_worst_low_new_values = list(l_worst_low_new.values())
            l_worst_low_new_values = [round(i,2) for i in l_worst_low_new_values]
            a = [str(i+1)+'. '+str(l_worst_low_new_keys[i])[0:min(len(str(l_worst_low_new_keys[i])),35)]+'    :'+str(l_worst_low_new_values[i]) for i in range(len(l_worst_low_new))]
            profit_new_value = sum(l_worst_low_new_values)
        listbox_new.delete(0,max(len(l_best_new),len(l_moderate_new),len(l_worst_high_new),len(l_worst_low_new)))
        for i in range(len(a)):
            listbox_new.insert(i, a[i])
        profit_new_value = round(profit_new_value,2)
        profit_new = tk.Label(root,text=str(profit_new_value))
        profit_new.place(relx = 0.79, rely = 0.85)
        
global x
global y
def showSelection():
    global x
    global y
    x = int(year.get())
    y = int(month.get())
    z = category.get()
    print(x,y,z)
    showData()

showButton = tk.Button(root, text='Show Data', command=showSelection)
showButton.place(relx = 0.50, rely = 0.21)

list_old_label = tk.Label(root,text='List of products with old profit')
list_old_label.place(relx = 0.12, rely = 0.32)
list_new_label = tk.Label(root,text='List of products with new profit')
list_new_label.place(relx = 0.68, rely = 0.32)
listbox_old = tk.Listbox(root,width=50,height=15)
listbox_old.place(relx = 0.05, rely = 0.4)
listbox_new = tk.Listbox(root,width=50,height=15)
listbox_new.place(relx = 0.60, rely = 0.4)
new_discount_label = tk.Label(root,text='New Discount')
new_discount_label.place(relx = 0.45, rely = 0.5)
discount_text = tk.Text(root,height=1,width=10)
discount_text.place(relx = 0.45, rely = 0.55)
apply_discount_btn = tk.Button(root,text='Apply Discount',command=dispNew)
apply_discount_btn.place(relx = 0.45, rely = 0.60)
old_profit_label = tk.Label(root, text='Total Profit')
old_profit_label.place(relx = 0.18, rely = 0.85)
new_profit_label = tk.Label(root, text='Total Profit')
new_profit_label.place(relx = 0.72, rely = 0.85)
root.mainloop()