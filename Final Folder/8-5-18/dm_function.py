# importing libraries and pickle files
import pandas as pd
import numpy as np
import pickle
inv_mon_name = pickle.load(open("inv_mon_name.p", "rb"))
inv_monsoldper_name = pickle.load(open("inv_monsoldper_name.p", "rb"))
l = pickle.load(open("l.p", "rb"))
lis_inv = pickle.load(open("lis_inv.p", "rb"))
lis_inv_sold_per = pickle.load(open("lis_inv_sold_per.p", "rb"))

# function to create dataframe containing profit, quantity, price for every product for the given year and month
def sorted_profit(year,mon):
    firstyear= pickle.load(open("firstyear.p", "rb"))
    secondyear= pickle.load(open("secondyear.p", "rb"))
    thirdyear= pickle.load(open("thirdyear.p", "rb"))
    fourthyear= pickle.load(open("fourthyear.p", "rb"))
    thirdfourth= pickle.load(open("thirdfourth.p", "rb"))
    twothree4= pickle.load(open("twothree4.p", "rb"))
    twothree= pickle.load(open("twothree.p", "rb"))
    onetwo= pickle.load(open("onetwo.p", "rb"))
    onetwo3=pickle.load(open("onetwo3.p", "rb"))
    if(year == 2017):
        data = pd.read_excel("store-dataset1.xlsx")
    if(year == 2016):
        data = onetwo3  
    if(year == 2015):
        data = onetwo
    if(year == 2014):
        data = firstyear    
    
    
    d_product = []
    d_MRP = []
    d_inventory = []
    d_quantity = []
    d_profit = []
    year1 =0
    mon1 = 0
    if(mon == 1 or mon ==  2 or mon == 3):
        mon1= 10
        year1 = year-1
    else:
        mon1=mon-3
        year1=year
     
    data1 = pd.DataFrame()
    count=0

    while(count < 3): 
          
        a =  pd.DatetimeIndex(data['Order Date']).year == year1
        b =  pd.DatetimeIndex(data['Order Date']).month == mon1
    
        for i in range(len(data)):
            if(a[i]== True and b[i]==True):
        
                data1 = data1.append(data.iloc[i,:]) 
    
        mon1+=1
        count+=1        
            
        data1 = data1.reset_index(drop=True)
    
        
    
    for i in data1['Product Name'].unique():
        d_product.append(i)
        d_MRP.append(data1[data1['Product Name']==i]['MRP per price'].sum())
        d_inventory.append(data1[data1['Product Name']==i]['Factory Price per piece'].sum())
        d_quantity.append(data1[data1['Product Name']==i]['Quantity'].sum())
        d_profit.append(data1[data1['Product Name']==i]['Profit per piece'].sum())
    d_os1 = np.array([d_product,d_MRP,d_inventory,d_quantity,d_profit]).T
    d_os1 = pd.DataFrame(d_os1,columns = ['d_product','d_MRP','d_inventory','d_quantity','d_profit'])
    d_os1[['d_MRP','d_inventory','d_quantity','d_profit']] = d_os1[['d_MRP','d_inventory','d_quantity','d_profit']].apply(pd.to_numeric)
    d_os1 = d_os1.round(2)
    d_os1=d_os1.sort_values(['d_profit'],ascending=False)
    d_os1 = d_os1.reset_index()
    return d_os1

# function to get the sales for the given year and month
def predicted_sales(year,mon,pname):
    lis = [0,0,0]
   
    count = year - 2014
    diction = ((year-2014)*12+mon)-1
    
    for i in range(3):
        try:
            li = lis_inv_sold_per[inv_monsoldper_name[diction-1-i]][pname][1]
        except:
            li = 0
            pass
        lis[i] = li
    while(count!=0):
        for i in range(4):
            try:
                li = lis_inv_sold_per[inv_monsoldper_name[diction-12-i]][pname][1]
            except:
                li = 0
                pass
            lis.append(li)
                
        diction-=12
        count -=1
    return lis


