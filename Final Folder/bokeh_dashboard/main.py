#importing necessary packages

import numpy as np
import pandas as pd
import sys
import pickle
sys.path.insert(0,'C:\\Users\\user\\Desktop\\dashboard\\')

from bokeh.io import curdoc
from bokeh.models.widgets import Tabs
from bokeh.plotting import figure

from total_sales import graph_tab
from graph import stateWiseSales
from category import category_bar
from product_wise_sales import product_wise_bar
from trial import sub_cat_bar

#################################################################################

data = pd.read_excel(r'C:\Users\user\Desktop\dashboard\store-dataset1.xlsx')
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['year'],data['month'],data['day'] = data['Order Date'].dt.year, data['Order Date'].dt.month,data['Order Date'].dt.day

lis_inv_sold_per = pickle.load(open(r"C:\\Users\\user\\Desktop\\dashboard\\lis_inv_sold_per.p", "rb"))
category = pickle.load(open(r"C:\\Users\\user\\Desktop\\dashboard\\mostcategory.p",'rb'))
subcategory = pickle.load(open(r"C:\\Users\\user\\Desktop\\dashboard\\most_subcategory.p","rb"))

sub = list(subcategory.values())
most_sold = zip(category,sub)

tab1 = graph_tab(data)   # Month and year wise total sales
tab2 = stateWiseSales(data,most_sold) # US States Map
tab3 = category_bar(data)	# Category wise Sales
tab4 = product_wise_bar(lis_inv_sold_per) # Product and year sales
tab5 = sub_cat_bar(data)    # Subcategory sales
tabs = Tabs(tabs = [tab1, tab2, tab3, tab4, tab5])

curdoc().add_root(tabs)