import pandas as pd
import numpy as np

from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import (CategoricalColorMapper,ColumnDataSource, HoverTool, LogColorMapper,Panel)
from bokeh.palettes import Viridis6 as palette
from bokeh.layouts import widgetbox,column,row
from bokeh.models.widgets import Select 

#########################################################################################################
#Total sales graph. Takes year and month as arguments and returns total sales of that month in that year.
#########################################################################################################

def graph_tab(data):
    def f(data,year,month):
        recent = data[(data['year']==year) & (data['month']==month)]
        recent_by_day = recent.groupby('day')
        sales_by_year = recent_by_day['Sales'].agg(np.sum)
        sales = [sales for sales in sales_by_year]
        return sales


    recent = data[(data['year'] == 2017) & (data['month'] == 12)] 

    group_by_day = recent.groupby('day')
    x=group_by_day['Sales'].agg(np.sum)
    sales = [sale for sale in x]

    source = ColumnDataSource(data={'days':[x for x in range(len(sales))],'sales':sales})
    p = figure(plot_width = 800, plot_height = 600,title="Day wise Total Sales for a given Year and Month",x_axis_label ="Days of Month",y_axis_label="Total Sales")
    p.title.align = 'center'
    p.title.text_font_size = '20pt'
    p.title.text_font = 'serif'

		# Axis titles
    p.xaxis.axis_label_text_font_size = '14pt'
    p.xaxis.axis_label_text_font_style = 'bold'
    p.yaxis.axis_label_text_font_size = '14pt'
    p.yaxis.axis_label_text_font_style = 'bold'
    

		# Tick labels
    p.xaxis.major_label_text_font_size = '12pt'
    p.yaxis.major_label_text_font_size = '12pt'
    p.line(x='days', y='sales', source=source,line_width=1.5)
    p.circle(x='days',y='sales',source=source)

    menu1 = Select(title="Year", value="2017", options=['2017','2016','2015','2014'])
    menu2 = Select(title="Month", value="Dec",options=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])

    # calls this function when the dropdown values are changed.
    def callback(attr,old,new):
        month_num = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
        year = int(menu1.value)
        month = month_num[menu2.value]
        source.data = {'days':[x for x in range(1,31)],'sales':f(data,year,month)}

    menu1.on_change('value',callback)
    menu2.on_change('value',callback)

    controls = widgetbox(menu1,menu2)
    layout = row(controls,p)

    tab = Panel(child=layout,title='Total Sales')
    
    return tab
#curdoc().add_root(layout)
