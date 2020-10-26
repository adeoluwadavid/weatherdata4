# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 14:04:08 2020

@author: Adewole
"""


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
start_date = "2019-01-01 00:00:00"
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



if (dataToPlot == 'Temperature'):
    print('Mean: ',np.mean(temp1))
    print('Median: ', np.median(temp1))
    print('STD: ',np.std(temp1))
    print("Max value",np.max(temp1))
    print('Min value', np.min(temp1))
    
    plt.plot(temp1,"-o")
    plt.xlabel("Date")
    plt.ylabel("Temperature(C)") 
elif (dataToPlot == 'Dew_Point'):
    print('Mean: ',np.mean(dewP1))
    print('Median: ', np.median(dewP1))
    print('STD: ',np.std(dewP1))
    print("Max value",np.max(dewP1))
    print('Min value', np.min(dewP1))
    
    plt.plot(dewP1,"-o")
    plt.xlabel("Date")
    plt.ylabel("Dew Point(C)") 
elif (dataToPlot == 'Humidity'):
    print('Mean: ',np.mean(hum1))
    print('Median: ', np.median(hum1))
    print('STD: ',np.std(hum1))
    print("Max value",np.max(hum1))
    print('Min value', np.min(hum1))
    
    plt.plot(hum1,"-o")
    plt.xlabel("Date")
    plt.ylabel("Dew Point(C)")
elif (dataToPlot == 'Wind'):
    print('Wind Does Not Contain Numerics')
    plt.plot(w1,"-o")
    plt.xlabel("Date")
    plt.ylabel("Wind(C)")
elif (dataToPlot == 'Wind_Speed'):
    print('Mean: ',np.mean(wS1))
    print('Median: ', np.median(wS1))
    print('STD: ',np.std(wS1))
    print("Max value",np.max(wS1))
    print('Min value', np.min(wS1))
    
    plt.plot(wS1,"-o")
    plt.xlabel("Date")
    plt.ylabel("Wind Speed(C)")
elif (dataToPlot == 'Wind_Gust'):
    print('Mean: ',np.mean(wG1))
    print('Median: ', np.median(wG1))
    print('STD: ',np.std(wG1))
    print("Max value",np.max(wG1))
    print('Min value', np.min(wG1))
    
    plt.plot(wG1,"-o")
    plt.xlabel("Date")
    plt.ylabel("Wind Gust(C)")
elif (dataToPlot == 'Pressure'):
    print('Mean: ',np.mean(press1))
    print('Median: ', np.median(press1))
    print('STD: ',np.std(press1))
    print("Max value",np.max(press1))
    print('Min value', np.min(press1))
    
    plt.plot(press1,"-o")
    plt.xlabel("Date")
    plt.ylabel("Wind Speed(C)")
elif (dataToPlot == 'Precipitation'):
    print('Mean: ',np.mean(precip1))
    print('Median: ', np.median(precip1))
    print('STD: ',np.std(precip1))
    print("Max value",np.max(precip1))
    print('Min value', np.min(precip1))
    
    plt.plot(precip1,"-o")
    plt.xlabel("Date")
    plt.ylabel("Wind Speed(C)")
elif (dataToPlot == 'Condition'):
    print('Condition Does Not Contain Numerics')
    
    plt.plot(c1,"-o")
    plt.xlabel("Date")
    plt.ylabel("Wind Speed(C)")
else:
    print("Enter the correct value")










