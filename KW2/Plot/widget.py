# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 16:24:05 2020

@author: Adewole
"""
from ipywidgets import interact, interactive, fixed, interact_manual
from IPython.display import display
import ipywidgets as widgets


widgetSelection = widgets.Dropdown(
    options=['Mean', 'Median', 'Standard_Deviation','Frequency',],
    value='Mean',
    description='Selection:',
    disabled=False,
)
start = widgets.DatePicker(
    description='Start Date: ',
    disabled=False
)
end = widgets.DatePicker(
    description='End Date: ',
    disabled=False
)
widgetDataToPlot = widgets.Dropdown(
    options=['Temperature', 'Dew_Point', 'Humidity','Wind_Speed' ,'Wind_Gust','Pressure','Precipitation'],
    value='Temperature',
    description='Data To Plot:',
    disabled=False,
)

#display(widgetSelection,start,end,widgetDataToPlot)