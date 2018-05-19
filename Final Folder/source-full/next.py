#importing pandas library to implement DataFrame on Store Dataset
import pandas as pd
import numpy as np
data = pd.read_excel("store-dataset.xlsx")
a = pd.DatetimeIndex(data['Order Date']).year == int(input("Enter year"))
b = pd.DatetimeIndex(data['Order Date']).month == int(input("Enter month "))

#Converting the Date field from string to Date object
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Ship Date'] = pd.to_datetime(data['Ship Date'])

#Sorting the database chronologically
data = data.sort_values(by='Order Date')

#Dividing the database with respect to Segment and then further dividing it 
#based on product categories
data_consumer = data[data['Segment']=='Consumer']
data_consumer_officeSupplies = data_consumer[data_consumer['Category']=='Office Supplies']
data_consumer_furniture = data_consumer[data_consumer['Category']=='Furniture']
data_consumer_technology = data_consumer[data_consumer['Category']=='Technology']

data_corporate = data[data['Segment']=='Corporate']
data_corporate_officeSupplies = data_corporate[data_corporate['Category']=='Office Supplies']
data_corporate_furniture = data_corporate[data_corporate['Category']=='Furniture']
data_corporate_technology = data_corporate[data_corporate['Category']=='Technology']

data_homeOffice = data[data['Segment']=='Home Office']
data_homeOffice_officeSupplies = data_homeOffice[data_homeOffice['Category']=='Office Supplies']
data_homeOffice_furniture = data_homeOffice[data_homeOffice['Category']=='Furniture']
data_homeOffice_technology = data_homeOffice[data_homeOffice['Category']=='Technology']

d_cons_os_product = []
d_cons_os_MRP = []
d_cons_os_inventory = []
d_cons_os_quantity = []
d_cons_os_profit = []

data_consumer_officeSupplies=data_consumer_officeSupplies[data_consumer_officeSupplies['Order Date'].dt.year == 2014]
data_consumer_officeSupplies=data_consumer_officeSupplies[data_consumer_officeSupplies['Order Date'].dt.month == 4]

for i in data_consumer_officeSupplies['Product Name'].unique():
    data_consumer_officeSupplies=data_consumer_officeSupplies[data_consumer_officeSupplies['Order Date'].dt.year == a[i]]
    data_consumer_officeSupplies=data_consumer_officeSupplies[data_consumer_officeSupplies['Order Date'].dt.month == b[i]]
    d_cons_os_product.append(i)
    d_cons_os_MRP.append(data_consumer_officeSupplies[data_consumer_officeSupplies['Product Name']==i]['MRP per price'].sum())
    d_cons_os_inventory.append(data_consumer_officeSupplies[data_consumer_officeSupplies['Product Name']==i]['Factory Price per piece'].sum())
    d_cons_os_quantity.append(data_consumer_officeSupplies[data_consumer_officeSupplies['Product Name']==i]['Quantity'].sum())
    d_cons_os_profit.append(data_consumer_officeSupplies[data_consumer_officeSupplies['Product Name']==i]['Profit per piece'].sum())
d_cons_os = np.array([d_cons_os_product,d_cons_os_MRP,d_cons_os_inventory,d_cons_os_quantity,d_cons_os_profit]).T
d_cons_os = pd.DataFrame(d_cons_os,columns = ['d_cons_os_product','d_cons_os_MRP','d_cons_os_inventory','d_cons_os_quantity','d_cons_os_profit'])
d_cons_os[['d_cons_os_MRP','d_cons_os_inventory','d_cons_os_quantity','d_cons_os_profit']] = d_cons_os[['d_cons_os_MRP','d_cons_os_inventory','d_cons_os_quantity','d_cons_os_profit']].apply(pd.to_numeric)
d_cons_os = d_cons_os.round(2)
d_cons_os=d_cons_os.sort_values(['d_cons_os_profit'],ascending=False)

d_cons_fur_product = []
d_cons_fur_MRP = []
d_cons_fur_inventory = []
d_cons_fur_quantity = []
d_cons_fur_profit = []
data_consumer_furniture=data_consumer_furniture[data_consumer_furniture['Order Date'].dt.year == 2014]
data_consumer_furniture=data_consumer_furniture[data_consumer_furniture['Order Date'].dt.month == 4]
for i in data_consumer_furniture['Product Name'].unique():
    d_cons_fur_product.append(i)
    d_cons_fur_MRP.append(data_consumer_furniture[data_consumer_furniture['Product Name']==i]['MRP per piece'].sum())
    d_cons_fur_inventory.append(data_consumer_furniture[data_consumer_furniture['Product Name']==i]['Factory Price per piece'].sum())
    d_cons_fur_quantity.append(data_consumer_furniture[data_consumer_furniture['Product Name']==i]['Quantity'].sum())
    d_cons_fur_profit.append(data_consumer_furniture[data_consumer_furniture['Product Name']==i]['Profit per piece'].sum())
d_cons_fur = np.array([d_cons_fur_product,d_cons_fur_MRP,d_cons_fur_inventory,d_cons_fur_quantity,d_cons_fur_profit]).T
d_cons_fur = pd.DataFrame(d_cons_fur,columns = ['d_cons_fur_product','d_cons_fur_MRP','d_cons_fur_inventory','d_cons_fur_quantity','d_cons_fur_profit'])
d_cons_fur[['d_cons_fur_MRP','d_cons_fur_inventory','d_cons_fur_quantity','d_cons_fur_profit']] = d_cons_fur[['d_cons_fur_MRP','d_cons_fur_inventory','d_cons_fur_quantity','d_cons_fur_profit']].apply(pd.to_numeric)
d_cons_fur = d_cons_fur.round(2)
d_cons_fur=d_cons_fur.sort_values(['d_cons_fur_profit'],ascending=False)

d_cons_tech_product = []
d_cons_tech_MRP = []
d_cons_tech_inventory = []
d_cons_tech_quantity = []
d_cons_tech_profit = []
data_consumer_technology=data_consumer_technology[data_consumer_technology['Order Date'].dt.year == 2014]
data_consumer_technology=data_consumer_technology[data_consumer_technology['Order Date'].dt.month == 4]

for i in data_consumer_technology['Product Name'].unique():
    d_cons_tech_product.append(i)
    d_cons_tech_MRP.append(data_consumer_technology[data_consumer_technology['Product Name']==i]['MRP per piece'].sum())
    d_cons_tech_inventory.append(data_consumer_technology[data_consumer_technology['Product Name']==i]['Factory Price per piece'].sum())
    d_cons_tech_quantity.append(data_consumer_technology[data_consumer_technology['Product Name']==i]['Quantity'].sum())
    d_cons_tech_profit.append(data_consumer_technology[data_consumer_technology['Product Name']==i]['Profit per piece'].sum())
d_cons_tech = np.array([d_cons_tech_product,d_cons_tech_MRP,d_cons_tech_inventory,d_cons_tech_quantity,d_cons_tech_profit]).T
d_cons_tech = pd.DataFrame(d_cons_tech,columns = ['d_cons_tech_product','d_cons_tech_MRP','d_cons_tech_inventory','d_cons_tech_quantity','d_cons_tech_profit'])
d_cons_tech[['d_cons_tech_MRP','d_cons_tech_inventory','d_cons_tech_quantity','d_cons_tech_profit']] = d_cons_tech[['d_cons_tech_MRP','d_cons_tech_inventory','d_cons_tech_quantity','d_cons_tech_profit']].apply(pd.to_numeric)
d_cons_tech = d_cons_tech.round(2)
d_cons_tech=d_cons_tech.sort_values(['d_cons_tech_profit'],ascending=False)

d_cor_os_product = []
d_cor_os_MRP = []
d_cor_os_inventory = []
d_cor_os_quantity = []
d_cor_os_profit = []
data_corporate_officeSupplies=data_corporate_officeSupplies[data_corporate_officeSupplies['Order Date'].dt.year == 2014]
data_corporate_officeSupplies=data_corporate_officeSupplies[data_corporate_officeSupplies['Order Date'].dt.month == 4]
for i in data_corporate_officeSupplies['Product Name'].unique():
    d_cor_os_product.append(i)
    d_cor_os_MRP.append(data_corporate_officeSupplies[data_corporate_officeSupplies['Product Name']==i]['MRP per piece'].sum())
    d_cor_os_inventory.append(data_corporate_officeSupplies[data_corporate_officeSupplies['Product Name']==i]['Factory Price per piece'].sum())
    d_cor_os_quantity.append(data_corporate_officeSupplies[data_corporate_officeSupplies['Product Name']==i]['Quantity'].sum())
    d_cor_os_profit.append(data_corporate_officeSupplies[data_corporate_officeSupplies['Product Name']==i]['Profit per piece'].sum())
d_cor_os = np.array([d_cor_os_product,d_cor_os_MRP,d_cor_os_inventory,d_cor_os_quantity,d_cor_os_profit]).T
d_cor_os = pd.DataFrame(d_cor_os,columns = ['d_cor_os_product','d_cor_os_MRP','d_cor_os_inventory','d_cor_os_quantity','d_cor_os_profit'])
d_cor_os[['d_cor_os_MRP','d_cor_os_inventory','d_cor_os_quantity','d_cor_os_profit']] = d_cor_os[['d_cor_os_MRP','d_cor_os_inventory','d_cor_os_quantity','d_cor_os_profit']].apply(pd.to_numeric)
d_cor_os = d_cor_os.round(2)
d_cor_os=d_cor_os.sort_values(['d_cor_os_profit'],ascending=False)

d_cor_fur_product = []
d_cor_fur_MRP = []
d_cor_fur_inventory = []
d_cor_fur_quantity = []
d_cor_fur_profit = []
data_corporate_furniture=data_corporate_furniture[data_corporate_furniture['Order Date'].dt.year == 2014]
data_corporate_furniture=data_corporate_furniture[data_corporate_furniture['Order Date'].dt.month == 4]
for i in data_corporate_furniture['Product Name'].unique():
    d_cor_fur_product.append(i)
    d_cor_fur_MRP.append(data_corporate_furniture[data_corporate_furniture['Product Name']==i]['MRP per piece'].sum())
    d_cor_fur_inventory.append(data_corporate_furniture[data_corporate_furniture['Product Name']==i]['Factory Price per piece'].sum())
    d_cor_fur_quantity.append(data_corporate_furniture[data_corporate_furniture['Product Name']==i]['Quantity'].sum())
    d_cor_fur_profit.append(data_corporate_furniture[data_corporate_furniture['Product Name']==i]['Profit per piece'].sum())
d_cor_fur = np.array([d_cor_fur_product,d_cor_fur_MRP,d_cor_fur_inventory,d_cor_fur_quantity,d_cor_fur_profit]).T
d_cor_fur = pd.DataFrame(d_cor_fur,columns = ['d_cor_fur_product','d_cor_fur_MRP','d_cor_fur_inventory','d_cor_fur_quantity','d_cor_fur_profit'])
d_cor_fur[['d_cor_fur_MRP','d_cor_fur_inventory','d_cor_fur_quantity','d_cor_fur_profit']] = d_cor_fur[['d_cor_fur_MRP','d_cor_fur_inventory','d_cor_fur_quantity','d_cor_fur_profit']].apply(pd.to_numeric)
d_cor_fur = d_cor_fur.round(2)
d_cor_fur=d_cor_fur.sort_values(['d_cor_fur_profit'],ascending=False)


d_cor_tech_product = []
d_cor_tech_MRP = []
d_cor_tech_inventory = []
d_cor_tech_quantity = []
d_cor_tech_profit = []
data_corporate_technology=data_corporate_technology[data_corporate_technology['Order Date'].dt.year == 2014]
data_corporate_technology=data_corporate_technology[data_corporate_technology['Order Date'].dt.month == 4]

for i in data_corporate_technology['Product Name'].unique():
    d_cor_tech_product.append(i)
    d_cor_tech_MRP.append(data_corporate_technology[data_corporate_technology['Product Name']==i]['MRP per piece'].sum())
    d_cor_tech_inventory.append(data_corporate_technology[data_corporate_technology['Product Name']==i]['Factory Price per piece'].sum())
    d_cor_tech_quantity.append(data_corporate_technology[data_corporate_technology['Product Name']==i]['Quantity'].sum())
    d_cor_tech_profit.append(data_corporate_technology[data_corporate_technology['Product Name']==i]['Profit per piece'].sum())
d_cor_tech = np.array([d_cor_tech_product,d_cor_tech_MRP,d_cor_tech_inventory,d_cor_tech_quantity,d_cor_tech_profit]).T
d_cor_tech = pd.DataFrame(d_cor_tech,columns = ['d_cor_tech_product','d_cor_tech_MRP','d_cor_tech_inventory','d_cor_tech_quantity','d_cor_tech_profit'])
d_cor_tech[['d_cor_tech_MRP','d_cor_tech_inventory','d_cor_tech_quantity','d_cor_tech_profit']] = d_cor_tech[['d_cor_tech_MRP','d_cor_tech_inventory','d_cor_tech_quantity','d_cor_tech_profit']].apply(pd.to_numeric)
d_cor_tech = d_cor_tech.round(2)
d_cor_tech=d_cor_tech.sort_values(['d_cor_tech_profit'],ascending=False)

d_hof_os_product = []
d_hof_os_MRP = []
d_hof_os_inventory = []
d_hof_os_quantity = []
d_hof_os_profit = []
data_homeOffice_officeSupplies=data_homeOffice_officeSupplies[data_homeOffice_officeSupplies['Order Date'].dt.year == 2014]
data_homeOffice_officeSupplies=data_homeOffice_officeSupplies[data_homeOffice_officeSupplies['Order Date'].dt.month == 4]
for i in data_homeOffice_officeSupplies['Product Name'].unique():
    d_hof_os_product.append(i)
    d_hof_os_MRP.append(data_homeOffice_officeSupplies[data_homeOffice_officeSupplies['Product Name']==i]['MRP per piece'].sum())
    d_hof_os_inventory.append(data_homeOffice_officeSupplies[data_homeOffice_officeSupplies['Product Name']==i]['Factory Price per piece'].sum())
    d_hof_os_quantity.append(data_homeOffice_officeSupplies[data_homeOffice_officeSupplies['Product Name']==i]['Quantity'].sum())
    d_hof_os_profit.append(data_homeOffice_officeSupplies[data_homeOffice_officeSupplies['Product Name']==i]['Profit per piece'].sum())
d_hof_os = np.array([d_hof_os_product,d_hof_os_MRP,d_hof_os_inventory,d_hof_os_quantity,d_hof_os_profit]).T
d_hof_os = pd.DataFrame(d_hof_os,columns = ['d_hof_os_product','d_hof_os_MRP','d_hof_os_inventory','d_hof_os_quantity','d_hof_os_profit'])
d_hof_os[['d_hof_os_MRP','d_hof_os_inventory','d_hof_os_quantity','d_hof_os_profit']] = d_hof_os[['d_hof_os_MRP','d_hof_os_inventory','d_hof_os_quantity','d_hof_os_profit']].apply(pd.to_numeric)
d_hof_os = d_hof_os.round(2)
d_hof_os=d_hof_os.sort_values(['d_hof_os_profit'],ascending=False)

d_hof_fur_product = []
d_hof_fur_MRP = []
d_hof_fur_inventory = []
d_hof_fur_quantity = []
d_hof_fur_profit = []
data_homeOffice_furniture=data_homeOffice_furniture[data_homeOffice_furniture['Order Date'].dt.year == 2014]
data_homeOffice_furniture=data_homeOffice_furniture[data_homeOffice_furniture['Order Date'].dt.month == 4]
for i in data_homeOffice_furniture['Product Name'].unique():
    d_hof_fur_product.append(i)
    d_hof_fur_MRP.append(data_homeOffice_furniture[data_homeOffice_furniture['Product Name']==i]['MRP per piece'].sum())
    d_hof_fur_inventory.append(data_homeOffice_furniture[data_homeOffice_furniture['Product Name']==i]['Factory Price per piece'].sum())
    d_hof_fur_quantity.append(data_homeOffice_furniture[data_homeOffice_furniture['Product Name']==i]['Quantity'].sum())
    d_hof_fur_profit.append(data_homeOffice_furniture[data_homeOffice_furniture['Product Name']==i]['Profit per piece'].sum())
d_hof_fur = np.array([d_hof_fur_product,d_hof_fur_MRP,d_hof_fur_inventory,d_hof_fur_quantity,d_hof_fur_profit]).T
d_hof_fur = pd.DataFrame(d_hof_fur,columns = ['d_hof_fur_product','d_hof_fur_MRP','d_hof_fur_inventory','d_hof_fur_quantity','d_hof_fur_profit'])
d_hof_fur[['d_hof_fur_MRP','d_hof_fur_inventory','d_hof_fur_quantity','d_hof_fur_profit']] = d_hof_fur[['d_hof_fur_MRP','d_hof_fur_inventory','d_hof_fur_quantity','d_hof_fur_profit']].apply(pd.to_numeric)
d_hof_fur = d_hof_fur.round(2)
d_hof_fur=d_hof_fur.sort_values(['d_hof_fur_profit'],ascending=False)

d_hof_tech_product = []
d_hof_tech_MRP = []
d_hof_tech_inventory = []
d_hof_tech_quantity = []
d_hof_tech_profit = []
data_homeOffice_technology=data_homeOffice_technology[data_homeOffice_technology['Order Date'].dt.year == 2014]
data_homeOffice_technology=data_homeOffice_technology[data_homeOffice_technology['Order Date'].dt.month == 4]

for i in data_homeOffice_technology['Product Name'].unique():
    d_hof_tech_product.append(i)
    d_hof_tech_MRP.append(data_homeOffice_technology[data_homeOffice_technology['Product Name']==i]['MRP per piece'].sum())
    d_hof_tech_inventory.append(data_homeOffice_technology[data_homeOffice_technology['Product Name']==i]['Factory Price per piece'].sum())
    d_hof_tech_quantity.append(data_homeOffice_technology[data_homeOffice_technology['Product Name']==i]['Quantity'].sum())
    d_hof_tech_profit.append(data_homeOffice_technology[data_homeOffice_technology['Product Name']==i]['Profit per piece'].sum())
d_hof_tech = np.array([d_hof_tech_product,d_hof_tech_MRP,d_hof_tech_inventory,d_hof_tech_quantity,d_hof_tech_profit]).T
d_hof_tech = pd.DataFrame(d_hof_tech,columns = ['d_hof_tech_product','d_hof_tech_MRP','d_hof_tech_inventory','d_hof_tech_quantity','d_hof_tech_profit'])
d_hof_tech[['d_hof_tech_MRP','d_hof_tech_inventory','d_hof_tech_quantity','d_hof_tech_profit']] = d_hof_tech[['d_hof_tech_MRP','d_hof_tech_inventory','d_hof_tech_quantity','d_hof_tech_profit']].apply(pd.to_numeric)
d_hof_tech = d_hof_tech.round(2)
d_hof_tech=d_hof_tech.sort_values(['d_hof_tech_profit'],ascending=False)