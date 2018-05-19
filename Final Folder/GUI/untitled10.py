import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel(r"C:\Users\user\Desktop\dashboard\store-dataset1.xlsx")

data.head()
# =============================================================================
# customers = pd.unique(data['Customer_Id'])
# 
# df = data.groupby('Customer_Id').count()
# 
# most_frequent = df.sort_values('Order_ID')[-5:]
# most_frequent = list(most_frequent.index)
# 
# freq_cust = pd.DataFrame(columns = data.columns)
# 
# for idx in most_frequent:
#     temp = data[data['Customer_Id'] == idx]
#     freq_cust = freq_cust.append(temp)
# 
# 
# =============================================================================

# =============================================================================
# 
# plt.figure(figsize=(15,10))
# plt.bar(range(49),list(values.values()),align='center')
# plt.xticks(range(49), list(values.keys()))
# plt.xticks(rotation=90)
# plt.show()
# 
# =============================================================================
female = data[data['Gender'] == 'Female']
male = data[data['Gender'] == 'Male']
plt.figure(figsize=(3,10))
count_female = len(pd.unique(female['Customer_Id']))
count_male = len(pd.unique(male['Customer_Id']))
plt.bar(range(2),[count_female,count_male],align='center')
plt.xticks(range(2), ["Female","Male"])

plt.show()


