import pandas as pd
import numpy as np

# loading dataset
dataset = pd.read_excel("store-dataset.xlsx")

# sorting from lowest to highest date
dataset1 = dataset.sort_values('Order Date')

# resetting index
dataset1 = dataset1.reset_index(drop=True)


# selecting desired sales data for a given period of time
a = pd.DatetimeIndex(dataset1['Order Date']).year == int(input("Enter year"))
b = pd.DatetimeIndex(dataset1['Order Date']).month == int(input("Enter month "))

dataset2 = pd.DataFrame()
for i in range(9994):
    if(a[i]== True and b[i]==True):
    
        dataset2 = dataset2.append(dataset1.iloc[i,:])    
        
dataset2 = dataset2.reset_index(drop=True)

# setting inventory size    
l = list(dataset2['Product Name'].unique())
inv_dict = {}
for i in l:
    inv_dict[i] = 50

# sold, remaining % sold, adding inventory
sold_percent = {}   
for i in range(len(dataset2)):
    # percentage of sales for each product
    sold_percent[dataset2['Product Name'][i]] = (((inv_dict[dataset2['Product Name'][i]])-(inv_dict[dataset2['Product Name'][i]]-int(dataset2['Quantity'][i])))/inv_dict[dataset2['Product Name'][i]])*100
    # updating inventory
    inv_dict[dataset2['Product Name'][i]] -= int(dataset2['Quantity'][i])
    # updating inventory for next month/quarter/year
    if(sold_percent[dataset2['Product Name'][i]] >= 10.0):
        print(dataset2['Product Name'][i])
        inv_dict[dataset2['Product Name'][i]] += 10