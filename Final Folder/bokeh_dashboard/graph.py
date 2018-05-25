import numpy as np
import pandas as pd

from bokeh.plotting import figure
from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.us_states import data as states
from bokeh.models import (ColumnDataSource, HoverTool,LinearColorMapper,Panel)
from bokeh.layouts import widgetbox,row,column
from bokeh.models.widgets import Select

def stateWiseSales(data,most_sold):
    
    del states['HI']
    del states['AK']
   
    states_sort = sorted(states)
    state_xs = [states[code]['lons'] for code in states_sort]
    state_ys = [states[code]['lats'] for code in states_sort]
    state_names = [states[code]['name'] for code in states_sort]
    
    data_2017 = data[data['year']==2017].groupby('State')
    data_2016 = data[data['year']==2016].groupby('State')
    data_2015 = data[data['year']==2015].groupby('State')
    data_2014 = data[data['year']==2014].groupby('State')
    
   
    sales_by_state = data_2017['Sales'].agg(np.sum)
    sales_2017 = [round(sales,2) for sales in sales_by_state]
    
    most_profitable = [x for x in most_sold]
    source = ColumnDataSource(data=dict(x=state_xs,y=state_ys,name=state_names,state_sales=sales_2017,most_profit=most_profitable))
    
   
    #color_mapper = LogColorMapper(palette=palette)
    color_mapper = LinearColorMapper(palette='Magma256',low=min(sales_2017),high=max(sales_2017))
    TOOLS = "pan,wheel_zoom,reset,hover,save"

    p = figure(title="Sales by State", tools = TOOLS,x_axis_location=None,y_axis_location=None,toolbar_location="left",plot_width=1100,plot_height=700)
    p.title.align = 'center'
    p.title.text_font_size = '20pt'
    p.title.text_font = 'serif'

    p.patches('x','y',source=source,line_color="#000000",fill_color={'field':'state_sales','transform':color_mapper},fill_alpha=0.7,line_width=0.5)
    hover = p.select_one(HoverTool)
    hover.point_policy = "follow_mouse"
    hover.tooltips = [("Name","@name"),("Sales:","@state_sales{($ 0.00 a)}"),("(Long,Lat)","($x,$y)"),("Most Profitable:","@most_profit")]
    
    menu = Select(title="Year", value="2017", options=['2017','2016','2015','2014'])
    
    def callback(attr,old,new):
        
        value = menu.value
        if value == '2017':
            sales_by_state = data_2017['Sales'].agg(np.sum)
        if value == '2016':
            sales_by_state = data_2016['Sales'].agg(np.sum)
        if value == '2015':
            sales_by_state = data_2015['Sales'].agg(np.sum)
        if value == '2014':
            sales_by_state = data_2014['Sales'].agg(np.sum)
        
        
        source.data['state_sales'] = [round(sales,2) for sales in sales_by_state]
    
    menu.on_change('value',callback)
    layout = row(menu,p)
    tab = Panel(child=layout,title="Statewise Sales for US")
    return(tab)
