# -*- coding: utf-8 -*-
"""
Created on Fri May 11 11:08:22 2018

@author: user
"""

import tkinter as tk

root = tk.Tk()
root.title('DM-Pricing Management')
root.geometry("900x600")

year = tk.StringVar(root)
month = tk.StringVar(root)

year.set('Select Year')
month.set('Select Month')

yearLabel = tk.Label(text='Select Year')
monthLabel = tk.Label(text='Select Month')

Year = ['Select Year', '2014', '2015', '2016', '2017']
yearOM = tk.OptionMenu(root,year,*Year)
Month = ['Select Month', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
monthOM = tk.OptionMenu(root,month,*Month)

yearLabel.place(relx=0.05,rely=0.05)
yearOM.place(relx=0.05,rely=0.08)
monthLabel.place(relx=0.2,rely=0.05)
monthOM.place(relx=0.2,rely=0.08)

global x
global y
x = 2014
y = 1

def printYM():
    print(x,y)

    import pandas as pd
    import numpy as np
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from dm_function import sorted_profit 
    from dm_function import predicted_sales
    import pickle
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
    dataset = pd.read_excel(r"C:\Users\user\Desktop\dashboard\store-dataset1.xlsx")
    dataset1 = dataset.sort_values('Order Date')
    dataset1 = dataset1.reset_index(drop=True)
    #x=int(input("Enter year"))
    #y=int(input("Enter month "))
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
    l = list(dataset2['Product Name'].unique())
    inv_dict = {}
    inv_dict = lis_inv[inv_mon_name[((x - 2014)*12 + y)-1]]
    sold_percent = {} 
    if(x==2017):
        if(y==12):
            data1=lastdata1
    else:        
        data1= sorted_profit(x,y)
    m = list(dataset1['Product Name'].unique())
    import operator
    new_l=[]
    dic ={}
    for i in range(len(m)):
        dic[m[i]]=0
    for i in range(0,len(m)):
        new_l=[]
        new_l = predicted_sales(x, y, m[i] )
        #new_l= np.array(new_l).reshape(1, -1)
        h=np.array(range(0,len(new_l))) 
        new_l= np.array(new_l).reshape(-1,1)
        h= np.array(h).reshape(-1,1)
        reg =LinearRegression()
        reg.fit(h,new_l)
        y_predict= int(abs(reg.predict(len(h))))
        dic[m[i]]= y_predict
        dic1=sorted(dic.items(),key=lambda x:x[1])
    for i in range(len(dataset2)):
        sold_percent[dataset2['Product Name'][i]] = (((((inv_dict[dataset2['Product Name'][i]])-(inv_dict[dataset2['Product Name'][i]]-int(dataset2['Quantity'][i])))/inv_dict[dataset2['Product Name'][i]])*100),dataset2['Quantity'][i])
        temp= int(dataset2['Quantity'][i])
        inv_dict[dataset2['Product Name'][i]] -= int(dataset2['Quantity'][i])
        if(sold_percent[dataset2['Product Name'][i]][1] >= 5.0):
            try:
                count=0     
                dfb = data[data1['d_product']==dataset2['Product Name'][i]].index.values.astype(int)[0]   
            except:
                count =1
                pass
            if(count==1):
                dfb = data[data['d_product']==dataset2['Product Name'][i]].index.values.astype(int)[0]
                if(dfb < 0.2*(len(data))):
                    print('HB')
                    inv_dict[dataset2['Product Name'][i]] += (80*temp)//100             
                if(dfb >= 0.2*(len(data))):
                    print('HMW')
                    inv_dict[dataset2['Product Name'][i]] += (50*temp)//100
            else:
                if(dfb < 0.2*(len(data1))):
                    print('HB1')
                    inv_dict[dataset2['Product Name'][i]] += (80*temp)//100
                if(dfb >= 0.2*(len(data1))):
                    print('HMW1')
                    inv_dict[dataset2['Product Name'][i]] += (50*temp)//100
        if(sold_percent[dataset2['Product Name'][i]][1] <= 5.0 and sold_percent[dataset2['Product Name'][i]][1] >= 3.0  ):
            try:
                count=0     
                dfb = data[data1['d_product']==dataset2['Product Name'][i]].index.values.astype(int)[0]   
            except:
                count =1
                pass 
            if(count==1):
                dfb = data[data['d_product']==dataset2['Product Name'][i]].index.values.astype(int)[0]
                if(dfb < 0.2*(len(data))):
                    print('MB')
                    inv_dict[dataset2['Product Name'][i]] += (80*temp)//100
                if(dfb > 0.2*(len(data)and dfb < 0.8*(len(data)))):
                    print('MM')
                    inv_dict[dataset2['Product Name'][i]] += (50*temp)//100   
                if(dfb >= 0.8*(len(data))):
                    print('MW')
                    inv_dict[dataset2['Product Name'][i]] += (20*temp)//100
            else:
                if(dfb < 0.2*(len(data1))):
                    print('MB1')
                    inv_dict[dataset2['Product Name'][i]] += (80*temp)//100
                if(dfb > 0.2*(len(data1)and dfb < 0.8*(len(data1)))):
                    print('MM1')
                    inv_dict[dataset2['Product Name'][i]] += (50*temp)//100   
                if(dfb >= 0.8*(len(data1))):
                    print('MW1')
                    inv_dict[dataset2['Product Name'][i]] += (20*temp)//100
        if(sold_percent[dataset2['Product Name'][i]][1] <= 3.0  ):
            try:
                count=0     
                dfb = data[data1['d_product']==dataset2['Product Name'][i]].index.values.astype(int)[0]   
            except:
                count =1
                pass 
            if(count==1):
                dfb = data[data['d_product']==dataset2['Product Name'][i]].index.values.astype(int)[0]
                if(dfb < 0.2*(len(data))):
                    print('WB')
                    inv_dict[dataset2['Product Name'][i]] += (50*temp)//100
                if(dfb > 0.2*(len(data)and dfb < 0.8*(len(data)))):
                    print('WM')
                    inv_dict[dataset2['Product Name'][i]] += (50*temp)//100   
                if(dfb >= 0.8*(len(data))):
                    print('WW')
                    inv_dict[dataset2['Product Name'][i]] += (0*temp)//100
            else:
                if(dfb < 0.2*(len(data1))):
                    print('WB1')
                    inv_dict[dataset2['Product Name'][i]] += (50*temp)//100
                if(dfb > 0.2*(len(data1)and dfb < 0.8*(len(data1)))):
                    print('WM1')
                    inv_dict[dataset2['Product Name'][i]] += (50*temp)//100
                if(dfb >= 0.8*(len(data1))):
                    print('WW1')
                    inv_dict[dataset2['Product Name'][i]] += (0*temp)//100
    new_data= data1
    new_dict= {}
    new_list= list(dataset['Product Name'].unique())
    l_best ={}
    l_moderate={}
    l_worst_high={}
    l_worst_low ={}
    not_sold={}
    discount = int(input('Enter the Discount in % '))
    for i in range(0,len(new_data)):
        if (i<.2*len(new_data)):
            #new_dict[new_data['d_product'][i]]= 'B'
            #new_data['d_MRP'][i]=new_data['d_inventory'][i]+new_data['d_inventory'][i]*discount
            #new_data['d_profit'][i]=(new_data['d_MRP'][i]-new_data['d_inventory'][i])*new_data['d_quantity'][i]
            l_best[(new_data['d_product'][i])]= new_data['d_profit'][i]   
        elif (i>=.8*len(new_data)):
            #new_dict[new_data['d_product'][i]]= 'W'
            if(new_data['d_quantity'][i] >= 5):
            #new_data['d_MRP'][i]= new_data['d_MRP'][i]+new_data['d_MRP'][i]*0.2
                #new_data['d_MRP'][i]=new_data['d_inventory'][i]+new_data['d_inventory'][i]*discount
                #print(new_data['d_product'][i])
                #new_data['d_profit'][i]=(new_data['d_MRP'][i]-new_data['d_inventory'][i])*new_data['d_quantity'][i]
                l_worst_high[(new_data['d_product'][i])]= new_data['d_profit'][i]   
            else:
                
                #new_data['d_MRP'][i]=new_data['d_inventory'][i]-new_data['d_inventory'][i]*discount
    
                #new_data['d_profit'][i]=(new_data['d_MRP'][i]-new_data['d_inventory'][i])*new_data['d_quantity'][i]
                l_worst_low[(new_data['d_product'][i])]= new_data['d_profit'][i] 
        else:
            #new_dict[new_data['d_product'][i]]= 'M'
            
            #new_data['d_MRP'][i]=new_data['d_inventory'][i]+new_data['d_inventory'][i]*discount
            #new_data['d_profit'][i]=(new_data['d_MRP'][i]-new_data['d_inventory'][i])*new_data['d_quantity'][i]        
            l_moderate[(new_data['d_product'][i])]= new_data['d_profit'][i] 
    
    string= "best"
    string2= "l_"+string
    final=eval(string2)
    final_list = list(final.values())
    for i in range(0,len(final)):
        final_list[i] *= discount
        
    for i in range(0,len(new_list)):
        flag=0
        for j in range(0,len(new_data)):
            if new_list[i]==new_data['d_product'][j]:
                flag=1
                break
        if flag==0:
            not_sold[(new_list[i])]= "Not Sold" 

    
    import pickle    
    pickle_out = open("Pricing_data.p","wb")
    pickle.dump(new_list,pickle_out)
    pickle_out.close()
    s=pickle.load(open("Pricing_data.p", "rb"))   
    
    pickle_out = open("Pricing_BestProduct.p","wb")
    pickle.dump(l_best,pickle_out)
    pickle_out.close()
    t=pickle.load(open("Pricing_BestProduct.p", "rb")) 
      
    pickle_out = open("Pricing_ModerateProduct.p","wb")
    pickle.dump(l_moderate,pickle_out)
    pickle_out.close()
    u=pickle.load(open("Pricing_ModerateProduct.p", "rb")) 
    
    pickle_out = open("Pricing_WorstHighProduct.p","wb")
    pickle.dump(l_worst_high,pickle_out)
    pickle_out.close()
    v=pickle.load(open("Pricing_WorstHighProduct.p", "rb")) 
    
    pickle_out = open("Pricing_WorstLowProduct.p","wb")
    pickle.dump(l_worst_low,pickle_out)
    pickle_out.close()
    v=pickle.load(open("Pricing_WorstLowProduct.p", "rb")) 
    
    pickle_out = open("not_sold_Product.p","wb")
    pickle.dump(not_sold,pickle_out)
    pickle_out.close()
    w=pickle.load(open("not_sold_Product.p", "rb")) 
    
    category = tk.StringVar(root)
    category.set('Select Category')
    Category = ['Select Category', 'Best', 'Moderate', 'Worst Low', 'Worst High', 'Not Sold']
    categoryOM = tk.OptionMenu(root,category,*Category)
    categoryLabel = tk.Label(root,text='Choose Category')
    categoryLabel.pack()
    categoryOM.pack()
    
    def showData():
        #productList = tk.Listbox(root,width = 60, height = 10)
        #profitList = tk.Listbox(root,width = 60, height = 10)
        if(category.get()=='Best'):
            a = []
            #b = []
            l_best_keys = list(l_best.keys())
            l_best_values = list(l_best.values())
            a = [str(i)+str(l_best_keys[i])+':'+str(l_best_values[i]) for i in range(len(l_best))]
            #b = [i for i in list(l_best.values())]
        elif(category.get()=='Moderate'):
            a = []
            #b = []
            l_moderate_keys = list(l_moderate.keys())
            l_moderate_values = list(l_moderate.values())
            a = [str(i)+str(l_moderate_keys[i])+':'+str(l_moderate_values[i]) for i in range(len(l_moderate))]
            #b = [i for i in list(l_best.values())]
        elif(category.get()=='Worst High'):
            a = []
            #b = []
            l_worst_high_keys = list(l_worst_high.keys())
            l_worst_high_values = list(l_worst_high.values())
            a = [str(i)+str(l_worst_high_keys[i])+':'+str(l_worst_high_values[i]) for i in range(len(l_worst_high))]
            #b = [i for i in list(l_best.values())]
        elif(category.get()=='Worst Low'): 
            a = []
            #b = []
            l_worst_low_keys = list(l_worst_low.keys())
            l_worst_low_values = list(l_worst_low.values())
            a = [str(i)+str(l_worst_low_keys[i])+':'+str(l_worst_low_values[i]) for i in range(len(l_worst_low))]
            #b = [i for i in list(l_best.values())]
        elif(category.get()=='Not Sold'):
            a = []
            #b = []
            l_not_sold_keys = list(l_not_sold.keys())
            l_not_sold_values = list(l_not_sold.values())
            a = [str(i)+str(l_not_sold_keys[i])+':'+str(l_not_sold_values[i]) for i in range(len(l_not_sold))]
            #b = [i for i in list(l_best.values())]
        productList.delete(0,max(len(l_best),len(l_moderate),len(l_worst_high),len(l_worst_low),len(not_sold)))
        for i in range(len(a)):
            productList.insert(i, a[i])
            #profitList.insert(i, b[i])
        
# =============================================================================
#         scrollbar = tk.Scrollbar(productList, orient="vertical")         
#         scrollbar.pack(side="right", fill="y") 
# =============================================================================
        
    productList = tk.Listbox(root,width = 60, height = 10)
    #profitList = tk.Listbox(root,width = 60, height = 10)
    productList.place(relx=0.05,rely=0.28)
    #profitList.pack()
    getData = tk.Button(root, text='Get Data', command=showData)                           
    getData.pack()
    
def populateData():
    global x
    global y
    x = int(year.get())
    y = int(month.get())
    printYM()

loadButton = tk.Button(root, text='Load Data', command=populateData)
loadButton.place(relx=0.35,rely=0.08)
root.mainloop()