# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 12:55:07 2020

@author: Adewole
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
start_date = "2020-01-01 00:00:00"
end_date = "2020-01-01 23:00:00"
dataToPlot = 'Pressure'

df = pd.read_excel('Keffi_Weather_Combined2.xlsx')
p = pd.date_range(start='1/1/2014',periods=len(df),freq='1H' )
df.set_index(p,inplace=True)

rng = df[start_date:end_date].dropna(how='any')

temp = rng.Temperature
dewP = rng.Dew_Point
hum = rng.Humidity
wind = rng.Wind
wS = rng.Wind_Speed
wG = rng.Wind_Gust
press = rng.Pressure
precip = rng.Precipitation
c = rng.Condition
date = rng.Date_Time


# Temperature and Dew Point in Celsius
temp1 = (temp.astype('float') -32) * (5/9)
dewP1 = (dewP.astype('float') - 32) * (5/9)

hum1 = hum.astype('int')
w1 = wind

#Wind Speed and Wind Gust in kmh
wS1 = wS.astype('float') * 1.60934
wG1 = wG.astype('float') * 1.60934
press1 = press.astype('float')
precip1 = precip.astype('float')
c1 = c
date1 = date
print(len(press1))
print(len(date1))
print()
inliers= []

def detect_inliers(data):
    threshold = 3
    print(data.index)
    my_mean = np.mean(data)
    std = np.std(data)
    if(my_mean == 0):
        print("Dataset values only contain zeros")
        return inliers
    else:
        for i in data:
            z_score = (i - my_mean)/std
            z = np.abs(z_score)
            if np.less(z, threshold):
                 inliers.append(i)
                 print(inliers.index)
        return inliers
    
result = detect_inliers(press1)
print(result)

#df['Pressure'] = result









