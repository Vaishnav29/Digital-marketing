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

data=pd.read_excel(r"C:\Users\user\Downloads\store-dataset.xlsx")
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

a = pd.DatetimeIndex(data['Order Date']).year ==  2014

data= data.sort_values('Order Date')
data=data.reset_index(drop=True)

data['Age']= np.nan
s=0
j=0
while(s<4):
    
    while(pd.DatetimeIndex(data['Order Date']).year[j]== pd.DatetimeIndex(data['Order Date']).year[j+1]):
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
    
    
pickle.dump(data,open('logdata.p','wb'))
pickle.dump(dict1,open('logdict.p','wb'))








#The Party Starts Here 


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
    
data= pickle.load(open('logdata.p','rb'))  
dict1= pickle.load(open('logdict.p','rb'))  
a=0
b=0
y = pd.DatetimeIndex(data['Order Date']).year == 2017
m = pd.DatetimeIndex(data['Order Date']).month== 10
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



y_pred=[]
#= y_test.reset_index(drop=True)
dataset= data[p:][['Customer ID','Region','Product I','Sub-Category','Age','Profit','Quantity']]
dataset = dataset.reset_index(drop = True)
y_pred= logreg.predict(dataset)


D =[]
for i in range(len(dataset)):
    if y_pred[i] == 1 :
        D.append(data['Product I'][i])
        
D= list(set(D))
h=[]
for i in range(len(D)):
    h.append(dict1[D[i]])
        


kfold = model_selection.KFold(n_splits=10, random_state=7)
modelCV = LogisticRegression()
scoring = 'accuracy'
X_train = data[:p][['Customer ID','Region','Product I','Sub-Category','Age','Profit','Quantity']]
y_train = data[:p]['Discount']
results = model_selection.cross_val_score(modelCV, X_train, y_train, cv=kfold, scoring=scoring)
print("10-fold cross validation average accuracy: %.3f" % (results.mean()))


