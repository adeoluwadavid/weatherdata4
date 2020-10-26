# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 12:51:33 2020

@author: Adewole
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
start_date = "2014-01-01 00:00:00"
end_date = "2014-01-01 23:00:00"
dataToPlot = 'Pressure'

df = pd.read_excel('Keffi_Weather_Combined2.xlsx')
p = pd.date_range(start='1/1/2014',periods=len(df),freq='1H' )
df.set_index(p,inplace=True)

rng = df[start_date:end_date].dropna(how='any')

print(rng.Wind)