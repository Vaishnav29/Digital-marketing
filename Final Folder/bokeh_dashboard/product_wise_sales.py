import numpy as np
import pandas as pd

from bokeh.plotting import figure
from bokeh.models import (CategoricalColorMapper,ColumnDataSource,Panel,FactorRange)
from bokeh.palettes import Viridis6 as palette
from bokeh.layouts import widgetbox,column,row
from bokeh.models.widgets import Select 

def product_wise_bar(lis_inv_sold_per):

    #lis_inv_sold_per = pickle.load(open("lis_inv_sold_per.p", "rb"))

    product_names = list(lis_inv_sold_per['inventory_soldmonth_per47'].keys())
    
    month_num = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    months_list = list(month_num.keys())
    years = ["2014","2015","2016","2017"]
    sales=[]
    source = ColumnDataSource(data=dict(months_list=months_list,sales=sales))
    p = figure(x_range=months_list,plot_height=500,plot_width=600,title="Month wise Sales of the given Product",toolbar_location=None,tools="",x_axis_label ="Months",y_axis_label="Quantity Sold")
    p.xaxis.axis_label_text_font_size = '14pt'
    p.xaxis.axis_label_text_font_style = 'bold'
    p.yaxis.axis_label_text_font_size = '14pt'
    p.yaxis.axis_label_text_font_style = 'bold'
    
    p.vbar(x='months_list',top='sales',width=0.9,source=source)
    p.xgrid.grid_line_color = None
    menu1 = Select(title="Select Year", value="2017",options=years)
    menu2 = Select(title="Select Product",value=None, options = product_names )
    
    
    def callback(attr,old,new):
        year_month = {2014:(1,13),2015:(13,25),2016:(25,37),2017:(37,49)}
        year = int(menu1.value)
        prod_name = menu2.value
        
        month_num = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
        sales=[]
        i,j = year_month[year]
        for x in range(i,j):
            try:
                sales_tuple = lis_inv_sold_per['inventory_soldmonth_per'+str(x)][prod_name]
                sales.append(sales_tuple[1])
            
            except KeyError:
                sales.append(0)
        
        source.data=dict(months_list=months_list,sales=sales)
                
    menu1.on_change('value',callback)
    menu2.on_change('value',callback)
    
    layout = row(menu1,menu2)
    layout2 = column(layout,p)
    tab = Panel(child=layout2,title="Month wise Sales")
    
    return tab
    
    