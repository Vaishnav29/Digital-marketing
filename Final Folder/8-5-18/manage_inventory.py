# Importing libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from dm_function import sorted_profit 
from dm_function import predicted_sales
import pickle

# loading pickle files (created/taken from inventory_history.py)
inv_mon_name = pickle.load(open("inv_mon_name.p", "rb"))
inv_monsoldper_name = pickle.load(open("inv_monsoldper_name.p", "rb"))
l = pickle.load(open("l.p", "rb"))
lis_inv = pickle.load(open("lis_inv.p", "rb"))
lis_inv_sold_per = pickle.load(open("lis_inv_sold_per.p", "rb"))
data = pickle.load(open("4yrsBMW.p", "rb"))
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

# best, moderate, worst, top 20 products, bottom 20 products and quantities
best = 80
moderate = 50
worst = 20
top_20 = 0.2
last_20 = 0.8
quantity_best = 5.0
quantity_worst = 3.0
first_year = 2014

# selecting desired sales data for a given period of time
year_enter=int(input("Enter year"))
mon_enter=int(input("Enter month "))
dataset1 = pd.DataFrame()
mon_quarter=[1,2,3]
if(year_enter==2017 and mon_enter in mon_quarter):
    dataset1= thirdfourth
elif(year_enter==2017 and mon_enter not in mon_quarter):
    dataset1=fourthyear  
elif(year_enter==2016 and mon_enter in mon_quarter):
    dataset1=twothree    
elif(year_enter==2016 and  mon_enter not in mon_quarter):
    dataset1= thirdyear
elif(year_enter==2015 and mon_enter in mon_quarter):
    dataset1=onetwo
elif(year_enter==2015 and  mon_enter not in mon_quarter):
    dataset1=secondyear

else:
    dataset1=firstyear    
            
dataset1 = dataset1.reset_index(drop=True)
a = pd.DatetimeIndex(dataset1['Order Date']).year ==  year_enter
b = pd.DatetimeIndex(dataset1['Order Date']).month ==  mon_enter

dataset2 = pd.DataFrame()
for i in range(len(dataset1)):
    if(a[i]== True and b[i]==True):
    
        dataset2 = dataset2.append(dataset1.iloc[i,:])    
        
dataset2 = dataset2.reset_index(drop=True)

# setting inventory size    
l = list(dataset2['Product Name'].unique())
inv_dict = {}
inv_dict = lis_inv[inv_mon_name[((year_enter - first_year)*12 + mon_enter)-1]]

# sold, remaining % sold, adding inventory
sold_percent = {} 
if(year_enter==2017):
    if(mon_enter==12):
        data1=lastdata1
else:        
    data1= sorted_profit(year_enter,mon_enter)
    
#full data is dataset1
list_unique_products = list(dataset1['Product Name'].unique())

#Predicting Sales
list_prev_sales=[]
list_predicted_sales ={}
for i in range(len(list_unique_products)):
    list_predicted_sales[list_unique_products[i]]=0
    
for i in range(0,len(list_unique_products)):
    list_prev_sales=[]
    list_prev_sales = predicted_sales(year_enter, mon_enter, list_unique_products[i] )
    h=np.array(range(0,len(list_prev_sales)))
    
    list_prev_sales= np.array(list_prev_sales).reshape(-1,1)
    h= np.array(h).reshape(-1,1)
    
    reg =LinearRegression()
    reg.fit(h,list_prev_sales)
    y_predict= int(abs(reg.predict(len(h))))
    list_predicted_sales[list_unique_products[i]]= y_predict

# Upadtes the inventory with rating and demand
for i in range(len(dataset2)):
    # percentage of sales for each product
    sold_percent[dataset2['Product Name'][i]] = (((((inv_dict[dataset2['Product Name'][i]])-(inv_dict[dataset2['Product Name'][i]]-int(dataset2['Quantity'][i])))/inv_dict[dataset2['Product Name'][i]])*100),dataset2['Quantity'][i])
    # updating inventory
    temp= int(dataset2['Quantity'][i])
    inv_dict[dataset2['Product Name'][i]] -= int(dataset2['Quantity'][i])
    # updating inventory for next month/quarter/year
    if(sold_percent[dataset2['Product Name'][i]][1] >= quantity_best):
        try: 
            count=0     
            dfb = data[data1['d_product']==dataset2['Product Name'][i]].index.values.astype(int)[0]   
        except:
            count =1
            pass 

        if(count==1):
            dfb = data[data['d_product']==dataset2['Product Name'][i]].index.values.astype(int)[0]                
            if(dfb < top_20*(len(data))):
                inv_dict[dataset2['Product Name'][i]] += (best*temp)//100
            
            if(dfb >= top_20*(len(data))):
                inv_dict[dataset2['Product Name'][i]] += (moderate*temp)//100
        else:
            if(dfb < top_20*(len(data1))):
                inv_dict[dataset2['Product Name'][i]] += (best*temp)//100
            
            if(dfb >= top_20*(len(data1))):
                inv_dict[dataset2['Product Name'][i]] += (moderate*temp)//100
        
        
    if(sold_percent[dataset2['Product Name'][i]][1] <= quantity_best and sold_percent[dataset2['Product Name'][i]][1] >= quantity_worst  ):       
        try:            
            count=0     
            dfb = data[data1['d_product']==dataset2['Product Name'][i]].index.values.astype(int)[0]   
        except:            
            count =1
            pass 
        if(count==1):
            dfb = data[data['d_product']==dataset2['Product Name'][i]].index.values.astype(int)[0]

            if(dfb < top_20*(len(data))):
                inv_dict[dataset2['Product Name'][i]] += (best*temp)//100
            
            if(dfb > top_20*(len(data)and dfb < last_20*(len(data)))):
                inv_dict[dataset2['Product Name'][i]] += (moderate*temp)//100   
            
            if(dfb >= last_20*(len(data))):
                inv_dict[dataset2['Product Name'][i]] += (worst*temp)//100

        else:
            if(dfb < top_20*(len(data1))):
                inv_dict[dataset2['Product Name'][i]] += (best*temp)//100
            
            if(dfb > top_20*(len(data1)and dfb < last_20*(len(data1)))):
                inv_dict[dataset2['Product Name'][i]] += (moderate*temp)//100   
            
            if(dfb >= last_20*(len(data1))):
                inv_dict[dataset2['Product Name'][i]] += (worst*temp)//100
 
    if(sold_percent[dataset2['Product Name'][i]][1] <= quantity_worst  ): 
        try:
            count=0     
            dfb = data[data1['d_product']==dataset2['Product Name'][i]].index.values.astype(int)[0]   
        except:
            count =1
            pass 
        
        if(count==1):
            dfb = data[data['d_product']==dataset2['Product Name'][i]].index.values.astype(int)[0]
            if(dfb < top_20*(len(data))):
                inv_dict[dataset2['Product Name'][i]] += (moderate*temp)//100
            
            if(dfb > top_20*(len(data)and dfb < last_20*(len(data)))):  
                inv_dict[dataset2['Product Name'][i]] += (moderate*temp)//100   
            
            if(dfb >= last_20*(len(data))):
                inv_dict[dataset2['Product Name'][i]] += (0*temp)//100

        else:
              if(dfb < top_20*(len(data1))):
                inv_dict[dataset2['Product Name'][i]] += (moderate*temp)//100
            
              if(dfb > top_20*(len(data1)and dfb < last_20*(len(data1)))):
                inv_dict[dataset2['Product Name'][i]] += (moderate*temp)//100    
            
              if(dfb >= last_20*(len(data1))):
                inv_dict[dataset2['Product Name'][i]] += (0*temp)//100               