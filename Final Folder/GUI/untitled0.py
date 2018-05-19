# -*- coding: utf-8 -*-
"""
Created on Sat May 19 09:32:30 2018

@author: user
"""

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

data=pd.read_excel(r"C:\Users\user\Desktop\store-dataset.xlsx")
dataset= data
data['Sub-Category'].unique()
data['Discount'].unique()
data['Sub-Category']=np.where((data['Sub-Category'] =='Accessories'), 0, data['Sub-Category'])
data['Sub-Category']=np.where((data['Sub-Category'] =='Art'), 0, data['Sub-Category'])
data['Sub-Category']=np.where((data['Sub-Category'] =='Envelopes'), 0, data['Sub-Category'])
data['Sub-Category']=np.where((data['Sub-Category'] =='Paper'), 0, data['Sub-Category'])
data['Sub-Category']=np.where((data['Sub-Category'] =='Binders'), 0, data['Sub-Category'])
data['Sub-Category']=np.where((data['Sub-Category'] =='Labels'), 0, data['Sub-Category'])
data['Sub-Category']=np.where((data['Sub-Category'] =='Phones'), 0, data['Sub-Category'])
data['Sub-Category']=np.where((data['Sub-Category'] =='Fasteners'), 0, data['Sub-Category'])

data['Sub-Category']=np.where((data['Sub-Category'] =='Chairs'), 1, data['Sub-Category'])
data['Sub-Category']=np.where((data['Sub-Category'] =='Machines'), 1, data['Sub-Category'])
data['Sub-Category']=np.where((data['Sub-Category'] =='Tables'), 1, data['Sub-Category'])
data['Sub-Category']=np.where((data['Sub-Category'] =='Bookcases'), 1, data['Sub-Category'])
data['Sub-Category']=np.where((data['Sub-Category'] =='Copiers'), 1, data['Sub-Category'])
data['Sub-Category']=np.where((data['Sub-Category'] =='Appliances'), 1, data['Sub-Category'])
data['Sub-Category']=np.where((data['Sub-Category'] =='Supplies'), 1, data['Sub-Category'])
data['Sub-Category']=np.where((data['Sub-Category'] =='Storage'), 1, data['Sub-Category'])
data['Sub-Category']=np.where((data['Sub-Category'] =='Furnishings'), 1, data['Sub-Category'])


data['Discount']=np.where((data['Discount'] <= 0.2), 0, data['Discount'])
data['Discount']=np.where((data['Discount'] > 0.2), 1, data['Discount'])

a = pd.DatetimeIndex(data['Order_Date']).year ==  2014

data= data.sort_values('Order_Date')
data=data.reset_index(drop=True)

data['Age']= np.nan
s=0
j=0
while(s<4):
    
    while(pd.DatetimeIndex(data['Order_Date']).year[j]== pd.DatetimeIndex(data['Order_Date']).year[j+1]):
        data['Age'][j]=s
        j+=1
    data['Age'][j]=s    
    s+=1
    if(j<len(data)):
        
        j+=1

        
# =============================================================================
# b = pd.DatetimeIndex(data['Order Date']).year ==  2015
# c= pd.DatetimeIndex(data['Order Date']).year ==  2016
# for i in range(0,len(data)):
#     
#     
#     if a[i]==True:
#         data['Order Date'][i]=3
#     
#     elif b[i]==True:
#         data['Order Date'][i]=2
#     
#     elif c[i]==True:
#         data['Order Date'][i]=1
#     
#     
#     else:
#         data['Order Date'][i]=0
# 
# 
# =============================================================================
for i in range(0,len(data)):
    if data['Discount'][i]== 1 :
        print(data['Product Name'][i])


data=data.dropna()
data['Product I']= np.nan

#Label Encoding
le = preprocessing.LabelEncoder()
le.fit(data['Customer ID'])
data['Customer ID']= le.transform(data['Customer ID'])

le.fit(data['Region'])
data['Region']= le.transform(data['Region'])

le.fit(data['Product ID'])
data['Product I']= le.transform(data['Product ID'])

dict1 ={}
for i in range(len(data)):
    dict1[data['Product I'][i]]= data['Product Name'][i]

test_data= data[:8315][['Customer ID','Region','Product ID','Sub-Category','Age','Profit','Quantity']]
discount_data = data[:8315]['Discount']
# =============================================================================
# le.fit(data['Sub-Category'])
# data['Sub-Category']= le.transform(data['Sub-Category'])
# 
# =============================================================================

#X_train, X_test, y_train, y_test = train_test_split(data[['Customer ID','Region','Product ID','Sub-Category','Order Date','Profit','Quantity']], data.Discount, test_size=0.05, random_state=42)

logreg = LogisticRegression()
logreg.fit(test_data, discount_data)



# =============================================================================
# rfe = RFE(logreg,7)
# rfe = rfe.fit(X_train,y_train)
# print(rfe.support_)
# print(rfe.ranking_)
# =============================================================================
y_pred=[]
#= y_test.reset_index(drop=True)
dataset= data[8316:][['Customer ID','Region','Product ID','Sub-Category','Age','Profit','Quantity']]
dataset = dataset.reset_index(drop = True)
y_pred= logreg.predict(dataset)


D =[]
for i in range(len(dataset)):
    if y_pred[i] == 1 :
        D.append(dataset['Product ID'][i])
        
D= list(set(D))
h=[]
for i in range(len(D)):
    h.append(dict1[D[i]])
        
# =============================================================================
# for i in range(0,len(data)):
#     S= data.iloc[i]
#     S= S.reshape(1,-1)
#     #S=np.array(dataset1['Customer ID'][i],dataset1['Region'][i],dataset1['Product ID'][i],dataset1['age'][i],dataset1['Profit'][i]]).reshape(1,-1)
# #S= np.array(['630','0','672','0','3','-3.0396','3'])
#     y_pred.append(logreg.predict(S))
# #print(logreg.score(np.array([[630],[0],[672],[0],[3],[-3.0396],[3]]).reshape(1,-1),y_test))
# =============================================================================

kfold = model_selection.KFold(n_splits=10, random_state=7)
modelCV = LogisticRegression()
scoring = 'accuracy'
results = model_selection.cross_val_score(modelCV, X_train, y_train, cv=kfold, scoring=scoring)
print("10-fold cross validation average accuracy: %.3f" % (results.mean()))

from sklearn.metrics import confusion_matrix
def plot_confusion_matrix(cm, classes,normalize=False,title='Confusion matrix',cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=0)
    plt.yticks(tick_marks, classes)

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    
cnf_matrix = confusion_matrix(y_test,y_pred)
np.set_printoptions(precision=2)
print("Recall metric in the testing dataset: ", cnf_matrix[1,1]/(cnf_matrix[1,0]+cnf_matrix[1,1]))

print("Confusion Metric in the testing dataset: \n", cnf_matrix)

# Plot non-normalized confusion matrix
class_names = ["<=20% discount", ">20% discount"]
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names, title='Confusion matrix')
plt.show()
