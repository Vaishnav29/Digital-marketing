import pandas as pd
import numpy as np

lis_inv = {}
inv_mon_name = []
count = 1
temp = 'inventory_month'
for i in range(1,49):
       var=temp+str(count)
       lis_inv[var]={}
       inv_mon_name.append(var)
       count += 1
        
lis_inv_sold_per = {}
inv_monsoldper_name = []
count = 1
temp = 'inventory_soldmonth_per'
for i in range(1,49):
       var=temp+str(count)
       lis_inv_sold_per[var]={}
       inv_monsoldper_name.append(var)
       count += 1        

# loading dataset
dataset = pd.read_excel("store-dataset.xlsx")

# sorting from lowest to highest date
dataset1 = dataset.sort_values('Order Date')

# resetting index
dataset1 = dataset1.reset_index(drop=True)
#dataset1 = dataset1[['Order Date', 'Product ID', 'Product Name', 'Quantity']]


# setting inventory size    
l = list(dataset1['Product Name'].unique())
for i in l:
    lis_inv[inv_mon_name[0]][i] = 500
    
# selecting desired sales data for a given period of time
a = pd.DatetimeIndex(dataset1['Order Date']).year == 2014
b = pd.DatetimeIndex(dataset1['Order Date']).month == 1


# =============================================================================
# for i in range(len(dataset2)):
#     if(a[i]== True and b[i] == True):
#         count += 1
#     
# dataset2 = dataset1.iloc[int(count):,:]
# dataset2 = dataset2.reset_index(drop=True)
# =============================================================================

year = 2014 
month = 1
count = 0
while(year < 2018 and count <49):
    
    dataset2 = pd.DataFrame()
    for i in range(len(dataset1)):
        if(pd.DatetimeIndex(dataset1['Order Date']).year[i] == year and pd.DatetimeIndex(dataset1['Order Date']).month[i] == month):
            print(count)
            dataset2 = dataset2.append(dataset1.iloc[i,:])
        dataset2 = dataset2.reset_index(drop=True)
        
        
    for i in l:
        lis_inv[inv_mon_name[count+1]][i] = lis_inv[inv_mon_name[count]][i]
    for k in range(len(dataset2)):
        # updating inventory
        
        lis_inv[inv_mon_name[count+1]][dataset2['Product Name'].iloc[k]] = (lis_inv[inv_mon_name[count+1]][dataset2['Product Name'].iloc[k]]-int(dataset2['Quantity'].iloc[k]))
         # percentage of sales for each product
        
        lis_inv_sold_per[inv_monsoldper_name[count]][dataset2['Product Name'].iloc[k]] = (((((lis_inv[inv_mon_name[count+1]][dataset2['Product Name'].iloc[k]])-(lis_inv[inv_mon_name[count+1]][dataset2['Product Name'].iloc[k]]-int(dataset2['Quantity'].iloc[k])))/lis_inv[inv_mon_name[count+1]][dataset2['Product Name'].iloc[k]])*100), dataset2['Quantity'][k])
          # updating inventory for next month/quarter/year

    count += 1
    month += 1
    if(month == 13):        
        month = 1
        year += 1
