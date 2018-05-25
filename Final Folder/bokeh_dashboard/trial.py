import pandas as pd
import numpy as np
from math import pi

from bokeh.io import curdoc
from bokeh.models.widgets import Select 
from bokeh.plotting import figure
from bokeh.models import (ColumnDataSource,LogColorMapper,Panel)
from bokeh.layouts import column,row

def sub_cat_bar(data):
    
    years = ["2014","2015","2016","2017"]
    sub_cat = list(pd.unique(data['Sub-Category']))
    
    sales = []
    for x in years:
        data_new = data[(data['year'] == int(x)) & (data['Sub-Category'] == 'Binders')]
        sales.append(data_new['Sales'].agg(np.mean))
            
        
    source = ColumnDataSource(data=dict(years=years,sales=sales))
    
    p = figure(x_range=years,plot_height=500,plot_width=600,title="Year wise Sales of the Subcategories",toolbar_location=None,tools="",x_axis_label ="Years",y_axis_label="Average Sales")
    #p.xaxis.major_label_orientation = pi/2
    p.xaxis.axis_label_text_font_size = '14pt'
    p.xaxis.axis_label_text_font_style = 'bold'
    p.yaxis.axis_label_text_font_size = '14pt'
    p.yaxis.axis_label_text_font_style = 'bold'
    
    p.vbar(x='years',top='sales',width=0.5,source=source,color='navy')
    
    #menu = Select(title="Year", value="2017", options=['2017','2016','2015','2014'])
    menu1 = Select(title="Sub Category", value="Binders", options=sub_cat)
    
    
    def callback(attr,old,new):
       
        sub = menu1.value
        sales = []
        data_sub = data[data['Sub-Category'] == sub]
        for x in years:
            data_new = data_sub[(data_sub['year'] == int(x))]
            sales.append(data_new['Sales'].agg(np.mean))
            
        source.data['sales'] = sales
        
    #menu.on_change('value',callback)
    menu1.on_change('value',callback)
    l1 = row(menu1)
    layout = column(l1,p)
    tab = Panel(child=layout,title='SubCategory Sales')
    return tab    