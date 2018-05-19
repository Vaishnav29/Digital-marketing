from tkinter import *
import pandas as pd
from math import sqrt
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFE
from sklearn.model_selection import cross_val_score
from sklearn import model_selection
import numpy as np
import pickle

global dataset
global D
global y_pred
#D = np.zeros(len(y_pred))
discount = pickle.load(open('dicount.p','rb'))
root = Tk()
root.title('Pricing strategies')
root.geometry('900x600')
root.configure(background='RoyalBlue3')

Label(root, text = 'Products eligible for giving discounts', font =('Helvetica', 15, 'bold', 'underline')).place(relx = 0.25, rely = 0.04)

def getprod():
    print(sub.get(),sub1.get())
    print(int(sub1.get())-3)
    
    #The Party Starts Here 
    
    f=sub.get()
    
    g= sub1.get()
    global a 
    a= int(f)
    global b 
    b=int(g)
    print(a,b)
    if b==3:
        b= 12
        a-=1
    elif b==2:
        b= 11
        a-=1
    elif b==1:
        b=10
        a-=1
    print(a,b)
    global data
    global dict1    
    data= pickle.load(open('logdata.p','rb'))  
    dict1= pickle.load(open('logdict.p','rb'))  
    if sub1.get()==1 or sub1.get()==2 or sub1.get()==3:
        
        y = pd.DatetimeIndex(data['Order Date']).year == int(a)
        m = pd.DatetimeIndex(data['Order Date']).month== int(b)
    
    else:
        y = pd.DatetimeIndex(data['Order Date']).year == int(a)
        m = pd.DatetimeIndex(data['Order Date']).month== int(b)-3
    i=0
    p=0
    for i in range(len(data)):
        if(y[i]== True):
            if(m[i]==True):
                p=i
                break
                  
            
            
    
    test_data= data[:p][['Customer ID','Region','Product I','Sub-Category','Age','Profit','Quantity']]
    discount_data = data[:p]['Discount']
    
    
    logreg = LogisticRegression()
    logreg.fit(test_data, discount_data)
    
    
    
    global y_pred
    y_pred=[]
    #= y_test.reset_index(drop=True)
    global dataset
    dataset= data[p:][['Customer ID','Region','Product I','Sub-Category','Age','Profit','Quantity']]
    print(dataset)
    dataset = dataset.reset_index(drop = True)
    print(dataset)
    y_pred= logreg.predict(dataset)
    
    print(y_pred)
    
    i=0
    j=0
    global D
    D = []

# =============================================================================
#     while(i< len(y_pred)):
#          if(y_pred[i] == 1):
#              D[j] = data['Product I'][i]
#              
#              j+=1
#          i+=1    
#              
#     print(D)   
#     
# =============================================================================
    for i in range(len(dataset)):
        if(y_pred[i] == 1):
            
            D.append(dataset['Product I'][i])
            #print(dataset['Product I'][i],data['Product I'][i])
    print(D)       
    D= list(set(D))
    h=[]
    for i in range(len(D)):
        h.append(dict1[D[i]])
            
    
    j = 1
    lis.delete(0, END)
    for i in range(len(h)):
        lis.insert(END,'{}. {}'.format(j, h[i]))
        j +=1
        
        
    kfold = model_selection.KFold(n_splits=10, random_state=7)
    modelCV = LogisticRegression()
    scoring = 'accuracy'
    X_train = data[:p][['Customer ID','Region','Product I','Sub-Category','Age','Profit','Quantity']]
    y_train = data[:p]['Discount']
    results = model_selection.cross_val_score(modelCV, X_train, y_train, cv=kfold, scoring=scoring)
    print("10-fold cross validation average accuracy: %.3f" % (results.mean()))


lis = Listbox(root, width = 60, height = 25)
lis.place(relx = 0.4, rely = 0.2)
    
bu = Button(root, text = 'Get Products for discount', command = getprod)
bu.place(relx = 0.1, rely = 0.2)

Years =[2017,2016,2015,2014]
month =[1,2,3,4,5,6,7,8,9,10,11,12]
sub = StringVar(root)
sub.set(Years[0])
subDropdown = OptionMenu(root,sub,*Years)
#subDropdown.configure(fg = 'black')
subDropdown.place(relx = 0.68, rely = 0.08)

sub1 = StringVar(root)
sub1.set(month[0])
sub1Dropdown = OptionMenu(root,sub1,*month)
#subDropdown.configure(fg = 'black')
sub1Dropdown.place(relx = 0.745, rely = 0.08)

root.mainloop()