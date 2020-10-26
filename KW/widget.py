# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:39:58 2020

@author: Adewole
"""
from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
from IPython.display import display
import ipywidgets as widgets

widgetDataToPlot = widgets.Dropdown(
    options=['Temperature', 'Dew Point', 'Humidity','Wind', 'Wind Speed' ,'Wind Gust','Pressure','Precip','Condition'],
    value='Temperature',
    description='Data To Plot:',
    disabled=False,
)

start_date = widgets.DatePicker(
    description='Start Date: ',
    disabled=False
)
end_date = widgets.DatePicker(
    description='End Date: ',
    disabled=False
)