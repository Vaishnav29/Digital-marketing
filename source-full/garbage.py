import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_excel('store-dataset.xlsx')

pd.unique(data['Sub-Category'])

office = data[data['Category'] == 'Office Supplies']
print(office.head())

tech = data[data['Category'] == 'Technology']
furniture = data[data['Category'] == 'Furniture']

pd.unique(office['Sub-Category'])
pd.unique(tech['Sub-Category'])
pd.unique(furniture['Sub-Category'])

office['Product Name'].value_counts()
tech['Product Name'].value_counts()
furniture['Product Name'].value_counts()

year_2014 = office[office['Order Date'].dt.year == 2014]
len(year_2014[year_2014['Order Date'].dt.month==11])

d = pd.DataFrame()
a = pd.DatetimeIndex(office['Order Date']).year == 2014
b = pd.DatetimeIndex(office['Order Date']).month == 4
for i in range(len(office)):
    if(a[i] == True and b[i]== True):
        office['Revenue'][i] = office['MRP per price'][i] * office['Quantity'][i]
        d = d.append(office.iloc[i,:])
        
