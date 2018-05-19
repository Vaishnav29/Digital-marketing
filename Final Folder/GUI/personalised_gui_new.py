"""
Created on Tue May 15 09:12:07 2018
@author: Karthik & Bhavana
"""

import tkinter as tk
root = tk.Tk()
# =============================================================================
# Importing necessary Libraries
# =============================================================================
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import KMeans
from collections import OrderedDict
import matplotlib.pyplot as plt

# =============================================================================
# Importing necessary Libraries
# =============================================================================

root.title('DM - Personalized Recommendation')
root.geometry('900x600')
root.configure(background="RoyalBlue3")
root.resizable(0,0)
quarterLabel = tk.Label(root,text = 'Select Quarter')
quarterLabel.place(relx = 0.11, rely = 0.05)
quarterLabel.configure(background='RoyalBlue3',fg = 'white')
noOfCustLabel = tk.Label(root,text = 'Select No. of Best Customers')
noOfCustLabel.place(relx = 0.32, rely = 0.05)
noOfCustLabel.configure(background='RoyalBlue3',fg = 'white')
noOfProdLabel = tk.Label(root,text = 'Select No. of Best Products')
noOfProdLabel.place(relx = 0.53, rely = 0.05)
noOfProdLabel.configure(background='RoyalBlue3',fg = 'white')
confidenceLabel = tk.Label(root,text = 'Select Confidence')
confidenceLabel.place(relx = 0.74, rely = 0.05)
confidenceLabel.configure(background='RoyalBlue3',fg = 'white')

Quarter = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16']
Customers = [25,50,75,100]
Products = [25,50,75,100,125,150,175,200]
Confidence = [0.25,0.5,0.75]
quarter = tk.StringVar(root)
quarter.set(Quarter[0])
customers = tk.StringVar(root)
customers.set(Customers[0])
products = tk.StringVar(root)
products.set(Products[0])
confidence = tk.StringVar(root)
confidence.set(Confidence[0])
quarterOM = tk.OptionMenu(root,quarter,*Quarter)
quarterOM.place(relx = 0.12, rely = 0.10)
customersOM = tk.OptionMenu(root,customers,*Customers)
customersOM.place(relx = 0.36, rely = 0.10)
productsOM = tk.OptionMenu(root,products,*Products)
productsOM.place(relx = 0.56, rely = 0.10)
confidenceOM = tk.OptionMenu(root,confidence,*Confidence)
confidenceOM.place(relx = 0.76, rely = 0.10)
global SelectCust
SelectCust = ['Select Customer']
global selectCust
selectCust = tk.StringVar(root)
selectCust.set('Select Customer')
global selectCustOM
selectCustOM = tk.OptionMenu(root,selectCust,*SelectCust)
selectCustOM.place(relx = 0.2, rely = 0.38)

# =============================================================================
# Start of Data Cleaning and Modification
# =============================================================================
def get_recommendations(quar, num_best_cust, num_best_prod, conf):
    import pandas as pd
    data = pd.read_excel('C:\\Users\\user\\Desktop\\store-dataset.xlsx')
    quater16 = pd.datetime(2017,12,31)
    quater15 = pd.datetime(2017,9,30)
    quater14 = pd.datetime(2017,6,30)
    quater13 = pd.datetime(2017,3,31)
    quater12 = pd.datetime(2016,12,31)
    quater11 = pd.datetime(2016,9,30)
    quater10 = pd.datetime(2016,6,30)
    quater09 = pd.datetime(2016,3,31)
    quater08 = pd.datetime(2015,12,31)
    quater07 = pd.datetime(2015,9,30)
    quater06 = pd.datetime(2015,6,30)
    quater05 = pd.datetime(2015,3,31)
    quater04 = pd.datetime(2014,12,31)
    quater03 = pd.datetime(2014,9,30)
    quater02 = pd.datetime(2014,6,30)
    quater01 = pd.datetime(2014,3,31)
    
    data_q16 = data.loc[(data['Order Date'] <= quater16) & (data['Order Date'] > quater12)]
    data_q15 = data.loc[(data['Order Date'] <= quater15) & (data['Order Date'] > quater12)]
    data_q14 = data.loc[(data['Order Date'] <= quater14) & (data['Order Date'] > quater12)]
    data_q13 = data.loc[(data['Order Date'] <= quater13) & (data['Order Date'] > quater12)]
    data_q12 = data.loc[(data['Order Date'] <= quater12) & (data['Order Date'] > quater11)]
    data_q11 = data.loc[(data['Order Date'] <= quater11) & (data['Order Date'] > quater10)]
    data_q10 = data.loc[(data['Order Date'] <= quater10) & (data['Order Date'] > quater09)]
    data_q09 = data.loc[(data['Order Date'] <= quater09) & (data['Order Date'] > quater08)]
    data_q08 = data.loc[(data['Order Date'] <= quater08) & (data['Order Date'] > quater07)]
    data_q07 = data.loc[(data['Order Date'] <= quater07) & (data['Order Date'] > quater06)]
    data_q06 = data.loc[(data['Order Date'] <= quater06) & (data['Order Date'] > quater05)]
    data_q05 = data.loc[(data['Order Date'] <= quater05) & (data['Order Date'] > quater04)]
    data_q04 = data.loc[(data['Order Date'] <= quater04) & (data['Order Date'] > quater03)]
    data_q03 = data.loc[(data['Order Date'] <= quater03) & (data['Order Date'] > quater02)]
    data_q02 = data.loc[(data['Order Date'] <= quater02) & (data['Order Date'] > quater01)]
    data_q01 = data.loc[data['Order Date'] <= quater01]
    
    quaterly_data = [data_q16, data_q15, data_q14, data_q13, data_q12, data_q11, data_q10, data_q09, data_q08, data_q07, data_q06, data_q05, data_q04, data_q03, data_q02, data_q01]
    
    for i in quaterly_data:
        i = i.drop(columns=['Row ID','Ship Date', 'Ship Mode','Country','State', 'Postal Code','Profit per piece', 'MRP', 'MRP per price','Factory Price per piece'],inplace=True)
    
    # =============================================================================
    # End of Data Cleaning and Modification
    # =============================================================================
    
    # =============================================================================
    # Start of similarity function
    # =============================================================================
        
    def pearson_cosine(x,y):
        if((sum(x) == 0) or (sum(y) == 0)):
            return(0,0)
        else:
            import math
            sum_x_i = 0
            sum_y_i = 0
            sum_yi_2 = 0
            sum_xi_2 = 0
            sumx = 0
            sumy = 0
            sum_x_y = 0
            sumx_2 = 0
            sumy_2 = 0
            sumxy = 0
            x_mean = np.mean(x)
            y_mean = np.mean(y)
            for i in range(len(x)):
                sum_x_i += x[i] - x_mean
                sum_y_i += y[i] - y_mean
                sum_x_y += (x[i] - x_mean)*(y[i] - y_mean)
                sum_xi_2 += (x[i] - x_mean)**2
                sum_yi_2 += (y[i] - y_mean)**2
                sumx += x[i]
                sumy += y[i]
                sumxy += x[i]*y[i]
                sumx_2 += x[i]*x[i]
                sumy_2 += y[i]*y[i]
            pearson_correlation = sum_x_y/(math.sqrt(sum_xi_2)*math.sqrt(sum_yi_2))
            cosine_similarity = sumxy/(math.sqrt(sumx_2)*math.sqrt(sumy_2))
            return(pearson_correlation,cosine_similarity)
    
    # =============================================================================
    # End of Similarity functions
    # =============================================================================
    
    # =============================================================================
    # Get Recommendations Algorithm
    # =============================================================================
    

    df = eval('data_q'+quar)
    unique_client = list(pd.unique(df['Customer Name']))
    unique_client_profit = {}
    for i in unique_client:
        unique_client_profit[i] = sum(df[df['Customer Name']==i]['Profit'])
    bes_cus = sorted(unique_client_profit, key=unique_client_profit.__getitem__, reverse=True)[0:num_best_cust]
    
    
    unique_product = list(pd.unique(df['Product Name']))
    unique_product_profit = {}
    for i in unique_product:
        unique_product_profit[i] = sum(df[df['Product Name']==i]['Profit'])
    bes_pro = sorted(unique_product_profit, key=unique_product_profit.__getitem__, reverse=True)[0:num_best_prod]
    
    p = {} 
    for i in range(len(bes_cus)):
        p[bes_cus[i]] = list(pd.unique(df[df['Customer Name']==bes_cus[i]]['Product Name']))  
        
    cli_pro_mat = []
    for i in range(len(bes_cus)):
        prod = p[bes_cus[i]]
        arr = []
        for j in range(len(bes_pro)):
            if(bes_pro[j] in prod):
                arr.append(1)
            else:
                arr.append(0)
        cli_pro_mat.append(arr)
    
    cos_pea = []
    for i in range(len(cli_pro_mat)):
        cos_pea_tem = []
        for j in range(i+1,len(cli_pro_mat)):
            cos_pea_tem.append(pearson_cosine(cli_pro_mat[i],cli_pro_mat[j]))
        cos_pea.append(cos_pea_tem)
        
    user1 = []
    user2 = []
    for i in range(len(cos_pea)):
        for j in range(len(cos_pea[i])):
            if(np.matrix(cos_pea[i][j][0])>conf and np.matrix(cos_pea[i][j][1])>conf):
                if(i==j):
                    pass
                else:
                    user1.append(i),user2.append(j)
    
    asdf = []
    for i in range(len(user1)):
        for k in range(len(cli_pro_mat)):
            if(cli_pro_mat[user1[i]][k] == 1 and cli_pro_mat[user2[i]][k] == 0):
                asdf.append([bes_cus[user2[i]], bes_pro[k]])
            elif((cli_pro_mat[user1[i]][k] == 0 and cli_pro_mat[user2[i]][k] == 1)):
                asdf.append([bes_cus[user2[i]], bes_pro[k]])
    recommendations = pd.DataFrame(asdf,columns=['Name', 'Product'])
    return(recommendations)

# =============================================================================
# End of Get Recommendations Algorithm
# =============================================================================
global a
def getCust():
    global SelectCust
    global selectCust
    global selectCustOM
    global a
    a = get_recommendations(quarter.get(),int(customers.get()),int(products.get()),float(confidence.get()))
    print(a)
    custNames = list(pd.unique(a.Name))
    SelectCust = custNames
    selectCustOM = tk.OptionMenu(root,selectCust,*SelectCust)
    selectCustOM.place(relx = 0.2, rely = 0.38)
getCustomers = tk.Button(root, text = 'Get Customers', command=getCust)
getCustomers.place(relx = 0.45, rely = 0.18)
lineLabel = tk.Label(root, text = '-'*160)
lineLabel.place(relx = 0.05, rely = 0.25)
lineLabel.configure(background='RoyalBlue3',fg = 'white')
lineLabel1 = tk.Label(root, text = '-'*160)
lineLabel1.place(relx = 0.05, rely = 0.70)
lineLabel1.configure(background='RoyalBlue3',fg = 'white')
selectCustLabel = tk.Label(root, text='Select Customers')
selectCustLabel.configure(background='RoyalBlue3',fg = 'white')
selectCustLabel.place(relx = 0.225, rely = 0.33)
dispProdLabel = tk.Label(root, text='Product Recommendation')
dispProdLabel.configure(background='RoyalBlue3',fg = 'white')
dispProdLabel.place(relx = 0.663, rely = 0.33)
def showProd():
    global a
    name = selectCust.get()
    pro = list(a[a['Name']==name]['Product'])
    listBoxProd.delete(0,listBoxProd.size())
    for i in range(len(pro)):
        listBoxProd.insert(i, pro[i][0:min(len(pro[i]),48)])
    print(name)
recommendProd = tk.Button(root,text='Recommend Product',command=showProd, wraplength=100)
recommendProd.place(relx = 0.40, rely = 0.50)
listBoxProd = tk.Listbox(root,width=50,height=10)
listBoxProd.place(relx=0.56,rely=0.38)

str1 = '''Personalized Recommendation is based on the Collaborative Filtering. \nWe are using Cosine Similarity and Pearson Correlation \nto suggest Product to best Customers of that quarter.'''
messLabel = tk.Label(root, text=str1)
messLabel.configure(background='RoyalBlue3',fg = 'white')
messLabel.place(relx=0.30,rely=0.78)
root.mainloop()