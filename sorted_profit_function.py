import pandas as pd
import numpy as np

def sorted_profit(year,mon):
    data = pd.read_excel("store-dataset.xlsx")
    data = data.sort_values(by='Order Date')
    #Converting the Date field from string to Date object
    data['Order Date'] = pd.to_datetime(data['Order Date'])
    data['Ship Date'] = pd.to_datetime(data['Ship Date'])
    
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
    
        
        
    
    for i in data['Product Name'].unique():
        d_product.append(i)
        d_MRP.append(data[data['Product Name']==i]['MRP per price'].sum())
        d_inventory.append(data[data['Product Name']==i]['Factory Price per piece'].sum())
        d_quantity.append(data[data['Product Name']==i]['Quantity'].sum())
        d_profit.append(data[data['Product Name']==i]['Profit per piece'].sum())
    d_os = np.array([d_product,d_MRP,d_inventory,d_quantity,d_profit]).T
    d_os = pd.DataFrame(d_os,columns = ['d_product','d_MRP','d_inventory','d_quantity','d_profit'])
    d_os[['d_MRP','d_inventory','d_quantity','d_profit']] = d_os[['d_MRP','d_inventory','d_quantity','d_profit']].apply(pd.to_numeric)
    d_os = d_os.round(2)
    d_os=d_os.sort_values(['d_profit'],ascending=False)
    d_os = d_os.reset_index()
    
        
        
    d_product = []
    d_MRP = []
    d_inventory = []
    d_quantity = []
    d_profit = []   
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
    return d_os,d_os1