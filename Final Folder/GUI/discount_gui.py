# -*- coding: utf-8 -*-
"""
Created on Fri May 25 10:11:11 2018

@author: user
"""

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

Label(root, text = 'Products eligible for giving discounts', font =('Helvetica', 15, 'bold', 'underline')).place(relx = 0.3, rely = 0)

def getprod():
    print(sub.get(),sub1.get())
    print(int(sub1.get())-3)
    
    #Setting year and month values
    global year 
    year= int(sub.get())
    global month 
    month=int(sub1.get())
    print(year,month)
    
    #Cases for Jan, Feb and March
    if month==3:
        month= 12
        year-=1
    elif month==2:
        month= 11
        year-=1
    elif month==1:
        month=10
        year-=1
    print(year,month)
    
    #Loading Data from Pickle file
    global data
    global dict1    
    data= pickle.load(open('logdata.p','rb'))  
    dict1= pickle.load(open('logdict.p','rb'))  
    
    #Assigning year and month value for the test dataset
    if sub1.get()==1 or sub1.get()==2 or sub1.get()==3:
        
        y = pd.DatetimeIndex(data['Order Date']).year == int(year)
        m = pd.DatetimeIndex(data['Order Date']).month== int(month)
    
    else:
        y = pd.DatetimeIndex(data['Order Date']).year == int(year)
        m = pd.DatetimeIndex(data['Order Date']).month== int(month)-3
    
    #Get the index of the last row of the train dataset
    i=0
    limit=0  
    for i in range(len(data)):
        if(y[i]== True):
            if(m[i]==True):
                limit=i
                break
                  
            
            
    #Get train data features and Target
    train_data= data[:limit][['Customer ID','Region','Product I','Sub-Category','Age','Profit','Quantity']]
    discount_data = data[:limit]['Discount']
    
    #Implementing Logistic Regression on the train dataset
    logreg = LogisticRegression()
    logreg.fit(train_data, discount_data)
    
    
    #Predicting values for the Discount (Using test dataset)
    global y_pred
    y_pred=[]
    global dataset
    dataset= data[limit:][['Customer ID','Region','Product I','Sub-Category','Age','Profit','Quantity']]
    print(dataset)
    dataset = dataset.reset_index(drop = True)
    print(dataset)
    y_pred= logreg.predict(dataset)
    print(y_pred)
    i=0
    j=0
    global D
    D = []

    #Get all product id's that are eligible for discounts
    for i in range(len(dataset)):
        if(y_pred[i] == 1):
            
            D.append(dataset['Product I'][i])
    print(D)       
    D= list(set(D))
    h=[]
    
    #get all product names that ar eligible for discounts
    for i in range(len(D)):
        h.append(dict1[D[i]]) #gets product name based on the product id and then is stored into a list
            
    
    j = 1
    lis.delete(0, END)
    for i in range(len(h)):
        lis.insert(END,'{}. {}'.format(j, h[i]))
        j +=1
        
    #Testing accuracy of the model using Cross-Validation
    kfold = model_selection.KFold(n_splits=10, random_state=7)
    modelCV = LogisticRegression()
    scoring = 'accuracy'
    X_train = data[:limit][['Customer ID','Region','Product I','Sub-Category','Age','Profit','Quantity']]
    y_train = data[:limit]['Discount']
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



#The Party Starts Here 










root.mainloop()
