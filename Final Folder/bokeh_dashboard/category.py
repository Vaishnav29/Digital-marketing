import pandas as pd
import numpy as np

from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import (CategoricalColorMapper,ColumnDataSource,Panel,FactorRange)
from bokeh.palettes import Viridis6 as palette
from bokeh.layouts import widgetbox,column,row
from bokeh.models.widgets import Select 

 
def category_bar(data):
    
   
    categories = pd.unique(data['Category'])
    years = [2014,2015,2016,2017]
    data_count = {'categories': categories}
    
    for x in years:
        count = []
        for y in categories:
            frame = data[(data['Category'] == y) & (data['year'] == x)]
            profit = frame['Profit'].agg(np.sum)
            count.append(profit)
        data_count[str(x)] = count
    
    
    temp = [ (category,str(year)) for category in categories for year in years]
    counts = sum(zip(data_count['2014'],data_count['2015'],data_count['2016'],data_count['2017']), ())
    
    source = ColumnDataSource(data=dict(x=temp,counts=counts))
    p = figure(x_range=FactorRange(*temp),title="Category Profits/Sales by Year",y_axis_label="Total Profit",plot_width=1000,toolbar_location=None,tools="")
    p.vbar(x='x',top='counts',width=0.9,source=source)
    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None
    
    menu = Select(title="Select",value="Profit",options=["Sales","Profit"])
    
    def callback(attr,old,new):
        value = menu.value
        categories = pd.unique(data['Category'])
        years = [2014,2015,2016,2017]
        data_count = {'categories': categories}
        for x in years:
            count = []
            for y in categories:
                frame = data[(data['Category'] == y) & (data['year'] == x)]
                profit = frame[value].agg(np.sum)
                count.append(profit)
            data_count[str(x)] = count
        temp = [ (category,str(year)) for category in categories for year in years]
        counts = sum(zip(data_count['2014'],data_count['2015'],data_count['2016'],data_count['2017']), ())
        
        source.data = dict(x=temp,counts=counts)
    
    menu.on_change('value',callback)
    layout = row(menu,p)
    tab = Panel(child=layout,title="Category Profits")
    return tab
