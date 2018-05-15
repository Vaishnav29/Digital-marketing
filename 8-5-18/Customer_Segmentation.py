import matplotlib.pyplot as plt



import pandas as pd
import numpy as np
#import  warnings
import  datetime as dt
#from datetime import date
#modules for predictive models
#import sklearn.cluster as cluster
from sklearn.cluster import KMeans
#from sklearn.decomposition import PCA
#from sklearn.mixture import GMM

from sklearn.metrics import silhouette_score

#visualizations
from pandas.plotting import scatter_matrix

import seaborn as sns

#warnings.filterwarnings("ignore")

retail_df = pd.read_excel(r'C:\Users\user.A713DCOK\Desktop\store-dataset.xlsx')
retail_df.head()

print("Summary..")
#exploring the unique values of each attribute
#print("Number of transactions: ", retail_df['Order ID'].nunique())
total = retail_df['Customer ID'].nunique()
print("Number of customers:", total )
#print("Percentage of customers NA: ", round(retail_df['Customer ID'].isnull().sum() * 100 / len(retail_df),2),"%" )

#try:
retail_df['Order Date'].max()
#except Valueerror as err:
#  pass
now = dt.date (2017,12,30)
print(now)

retail_df['Order Date'] = retail_df['Order Date'].dt.date

recency_df = retail_df.groupby(by='Customer ID', as_index=False)['Order Date'].max()
recency_df.columns = ['Customer ID','LastPurshaceDate']
recency_df.head()

recency_df['Recency'] = recency_df['LastPurshaceDate'].apply(lambda x: (now - x).days)
recency_df.head()
recency_df.drop('LastPurshaceDate',axis=1,inplace=True)

retail_df_copy = retail_df
retail_df_copy.drop_duplicates(subset=['Order Date', 'Customer ID'], keep="first", inplace=True)
#calculate frequency of purchases
frequency_df = retail_df_copy.groupby(by=['Customer ID'], as_index=False)['Order Date'].count()
frequency_df.columns = ['Customer ID','Frequency']
frequency_df.head()

retail_df['TotalCost'] = retail_df['Quantity'] * retail_df['Sales']
monetary_df = retail_df.groupby(by='Customer ID',as_index=False).agg({'TotalCost': 'sum'})
monetary_df.columns = ['Customer ID','Monetary']
monetary_df.head()

temp_df = recency_df.merge(frequency_df,on='Customer ID')
temp_df.head()

#merge with monetary dataframe to get a table with the 3 columns
rfm_df = temp_df.merge(monetary_df,on='Customer ID')
#use CustomerID as index
rfm_df.set_index('Customer ID',inplace=True)
#check the head
rfm_df.head()

#get the 80% of the revenue
pareto_cutoff = rfm_df['Monetary'].sum() * 0.8
print("The 80% of total revenue is: ",round(pareto_cutoff,2))

customers_rank = rfm_df
# Create a new column that is the rank of the value of coverage in ascending order
customers_rank['Rank'] = customers_rank['Monetary'].rank(ascending=0)
#customers_rank.drop('RevenueRank',axis=1,inplace=True)
customers_rank.head()

customers_rank.sort_values('Rank',ascending=True)
#get top 20% of the customers
top_20_cutoff = 793 *20 /100
top_20_cutoff

revenueByTop20 = customers_rank[customers_rank['Rank'] <= 158]['Monetary'].sum()
revenueByTop20

quantiles = rfm_df.quantile(q=[0.25,0.5,0.75])
quantiles
quantiles.to_dict()

def RScore(x,p,d):
    if x <= d[p][0.25]:
        return 4
    elif x <= d[p][0.50]:
        return 3
    elif x <= d[p][0.75]: 
        return 2
    else:
        return 1
# Arguments (x = value, p = recency, monetary_value, frequency, k = quartiles dict)
def FMScore(x,p,d):
    if x <= d[p][0.25]:
        return 1
    elif x <= d[p][0.50]:
        return 2
    elif x <= d[p][0.75]: 
        return 3
    else:
        return 4

rfm_segmentation = rfm_df
rfm_segmentation['R_Quartile'] = rfm_segmentation['Recency'].apply(RScore, args=('Recency',quantiles,))
rfm_segmentation['F_Quartile'] = rfm_segmentation['Frequency'].apply(FMScore, args=('Frequency',quantiles,))
rfm_segmentation['M_Quartile'] = rfm_segmentation['Monetary'].apply(FMScore, args=('Monetary',quantiles,))

rfm_segmentation.head()
rfm_segmentation['RFMScore'] = rfm_segmentation.R_Quartile.map(str) \
                            + rfm_segmentation.F_Quartile.map(str) \
                            + rfm_segmentation.M_Quartile.map(str)
rfm_segmentation.head()

#pickle files 
import pickle
pickle.dump(rfm_segmentation,open("Segmentation.p","wb"))



rfm_segmentation[rfm_segmentation['RFMScore']=='444'].sort_values('Monetary', ascending=False).head(10)
best = len(rfm_segmentation[rfm_segmentation['RFMScore']=='444']) 
print('Best Customers:',best) #recency , frequency and monetary is high
loyal = len(rfm_segmentation[rfm_segmentation['F_Quartile']==4])
print('Loyal Customers: ',loyal) #Spend good money with us often. Responsive to promotions.
potential = len(rfm_segmentation[rfm_segmentation['M_Quartile']==4])
print('Big Spenders:',potential) #Recent customers, but spent a good amount and bought more than once.
promising = len(rfm_segmentation[rfm_segmentation['R_Quartile']==4])
print('Promising Customers: ',promising) #Recent shoppers, but haven’t spent much.
attention = len(rfm_segmentation[rfm_segmentation['RFMScore']=='222']) + len(rfm_segmentation[rfm_segmentation['RFMScore']=='333'])
print('Customers Needing Attention : ',attention) #Above average recency, frequency and monetary values. May not have bought very recently though
at_risk = len(rfm_segmentation[rfm_segmentation['RFMScore']=='244'])
print('At Risk Customers: ',at_risk ) #Spent big money and purchased often. But long time ago. Need to bring them back!
cant_lose = len(rfm_segmentation[rfm_segmentation['RFMScore']=='114'])
print('Cannot lose these customers:',cant_lose)
lost = len(rfm_segmentation[rfm_segmentation['RFMScore']=='144'])
print('Lost Customers: ',lost) #Last purchase was long back, low spenders and low number of orders.
cheap = len(rfm_segmentation[rfm_segmentation['RFMScore']=='111'])
print('Lost Inconsequential Customers: ',cheap) #lowest receny, frequency, monetary.
#seasonal = (len(rfm_segmentation[rfm_segmentation['F_Quartile']=='1'] + len(rfm_segmentation[rfm_segmentation['M_Quartile']=='4']))
#print('Seasonal Customers:',seasonal)


#PIE-CHART
fracs = [best,loyal,potential,promising,attention,at_risk,cant_lose,lost,cheap]
labels = ['Best','Loyal', 'Potential','Promising', 'Attention', 'At_risk','Cant_lose','Lost','Cheap ']
#fracs =[best,loyal,potential,promising,attention,at_risk,cant_lose,lost,cheap]
explode = [0,0,0,0,0.2,0.2,0.2,0.2,0.2]
fig = plt.figure(figsize=[10, 10])
plt.pie(fracs,labels=labels,explode=explode,autopct='%1.1f%%')#startangle=90)
plt.title('Customer Segmentation')
plt.show()
seasonal = total - (best+loyal+potential+promising+attention+at_risk+cant_lose+lost+cheap)
print('Seasonal Customers:',seasonal)
rfm_data = rfm_df.drop(['R_Quartile','F_Quartile','M_Quartile','RFMScore'],axis=1)
rfm_data.head()
rfm_data.corr()

sns.heatmap(rfm_data.corr())
scatter_matrix(rfm_data, alpha = 0.3, figsize = (11,5), diagonal = 'hist');

#DATA NORMALIZATION
#log transformation
rfm_r_log = np.log(rfm_data['Recency']+0.1) #can't take log(0) and so add a small number
rfm_f_log = np.log(rfm_data['Frequency'])
rfm_m_log = np.log(rfm_data['Monetary']+0.1)

log_data = pd.DataFrame({'Monetary': rfm_m_log,'Recency': rfm_r_log,'Frequency': rfm_f_log})
log_data.head()

# Produce a scatter matrix for each pair of features in the data
scatter_matrix(log_data, alpha = 0.2, figsize = (11,5), diagonal = 'hist');
sns.heatmap(rfm_data.corr())
sns.heatmap(log_data.corr())
print(log_data.corr())

matrix = log_data.as_matrix()
for n_clusters in range(2,  10):
    kmeans = KMeans(init='k-means++', n_clusters = n_clusters, n_init=100)
    kmeans.fit(matrix)
    clusters = kmeans.predict(matrix)
    silhouette_avg = silhouette_score(matrix, clusters)
    print("For n_clusters =", n_clusters, "The average silhouette_score is :", silhouette_avg)

n_clusters = 2
kmeans = KMeans(init='k-means++', n_clusters = n_clusters, n_init=30)
kmeans.fit(matrix)
clusters_customers = kmeans.predict(matrix)
silhouette_avg = silhouette_score(matrix, clusters_customers)
print('score de silhouette: {:<.3f}'.format(silhouette_avg))

#VISUALIZATION
#create a scatter plot
plt.scatter(matrix[:, 0], matrix[:, 1], c=clusters_customers, s=50, cmap='viridis')
#select cluster centers
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='blue', s=200, alpha=0.5);

pd.DataFrame(pd.Series(clusters_customers).value_counts(), columns = ['NumberCustomers']).T       
                
