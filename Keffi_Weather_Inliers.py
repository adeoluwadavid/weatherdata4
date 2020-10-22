# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:20:13 2020

@author: Adewole
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

start_date = "2020-01-01 00:00:00"
end_date = "2020-01-02 23:00:00"
dataToPlot = 'Wind_Speed'

df = pd.read_excel('Keffi_Weather_Combined_Updated.xlsx')
p = pd.date_range(start='1/1/2014',periods=len(df),freq='1H' )
df.set_index(p,inplace=True)

rng = df[start_date:end_date]

temperature = rng.Temperature
dewPoint = rng.Dew_Point
humidity = rng.Humidity
wind = rng.Wind
windSpeed = rng.Wind_Speed
windGust = rng.Wind_Gust
pressure = rng.Pressure
precip = rng.Precip
condition = rng.Condition
date_time = rng.Date_Time

#print(temperature)
df['Temperature'] = temperature
df['Dew_Point'] = dewPoint
df['Humidity'] = humidity
df['Wind'] = wind
df['Wind_Speed'] = windSpeed
df['Wind_Gust'] = windGust
df['Pressure'] = pressure
df['Precipitation'] = precip
df['Condition'] = condition
df['Date_Time'] = date_time 

temp1 = temperature.dropna(how='any').astype('str')
dewP1 = dewPoint.dropna(how='any').astype('str')
humidity1 = humidity.dropna(how='any').astype('str')
wind1 = wind.dropna(how='any').astype('str')
windSpeed1 = windSpeed.dropna(how='any').astype('str')
windGust1 = windGust.dropna(how='any').astype('str')
pressure1 = pressure.dropna(how='any').astype('str')
precip1 = precip.dropna(how='any').astype('str')
condition1 = condition.dropna(how='any').astype('str')
date_time1 = date_time.dropna(how='any').astype('str')

temp2 = temp1.str.extract(r'([0-9]+)')
dewP2 = dewP1.str.extract(r'([0-9]+)')
humidity2 = humidity1.str.extract(r'([0-9]+)')
wind2 = wind1
windSpeed2 = windSpeed1.str.extract(r'([0-9]+)')
windGust2 = windGust1.str.extract(r'([0-9]+)')
pressure2 = pressure1.str.extract(r'([\d\.\d]+)')
precip2 = precip1.str.extract(r'([\d\.\d]+)')
condition2 = condition1
date_time2 = date_time1

df['Temperature'] = temp2
df['Dew_Point'] = dewP2
df['Humidity'] = humidity2
df['Wind'] = wind2
df['Wind_Speed'] = windSpeed2
df['Wind_Gust'] = windGust2
df['Pressure'] = pressure2
df['Precipitation'] = precip2
df['Condition'] = condition2
df['Date_Time'] = date_time2

temp3 = df['Temperature'].dropna(how='any').astype('str')
dewP3 = df['Dew_Point'].dropna(how='any').astype('str')
humidity3 = df['Humidity'].dropna(how='any').astype('str')
wind3 = df['Wind'].dropna(how='any').astype('str')
windSpeed3 = df['Wind_Speed'].dropna(how='any').astype('str')
windGust3 = df['Wind_Gust'].dropna(how='any').astype('str')
pressure3 = df['Pressure'].dropna(how='any').astype('str')
precip3 = df['Precipitation'].dropna(how='any').astype('str')
condition3 = df['Condition'].dropna(how='any').astype('str')
date_time3 = df['Date_Time'].dropna(how='any').astype('str')
#print(date_time3)
# Temperature and Dew Point in Celsius
temp = (temp3.astype('float') -32) * (5/9)
dewP = (dewP3.astype('float') - 32) * (5/9)
#print(temp)
#print(len(temp))
hum = humidity3.astype('int')
w = wind3

#Wind Speed and Wind Gust in kmh
wS = windSpeed3.astype('float') * 1.60934
wG = windGust3.astype('float') * 1.60934
press = pressure3.astype('float')
preC = precip3.astype('float')
c = condition3

inliers= []
#
def detect_inliers(data):
    threshold = 3
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
        return inliers

if(dataToPlot == 'Temperature'):
    result = detect_inliers(temp)
    if result ==[]:
        print('Mean is: 0 ')
        print('S.D is: 0')
        print('Median is: 0')
        print('Max value is: 0')
        print('Min value is: 0')
    else:
        print('Mean is: ', np.mean(result).round(2))
        print('S.D is:',np.std(result).round(2))
        print('Median is: ',np.median(result).round(2))
        print('Max value is:',np.max(result).round(2))
        print('Min value is:',np.min(result).round(2))
elif(dataToPlot == 'Dew_Point'):
    result = detect_inliers(dewP)
    if result ==[]:
        print('Mean is: 0 ')
        print('S.D is: 0')
        print('Median is: 0')
        print('Max value is: 0')
        print('Min value is: 0')
    else:
        print('Mean is: ', np.mean(result).round(2))
        print('S.D is:',np.std(result).round(2))
        print('Median is: ',np.median(result).round(2))
        print('Max value is:',np.max(result).round(2))
        print('Min value is:',np.min(result).round(2))
elif(dataToPlot == 'Humidity'):
    result = detect_inliers(hum)
    if result ==[]:
        print('Mean is: 0 ')
        print('S.D is: 0')
        print('Median is: 0')
        print('Max value is: 0')
        print('Min value is: 0')
    else:
        print('Mean is: ', np.mean(result).round(2))
        print('S.D is:',np.std(result).round(2))
        print('Median is: ',np.median(result).round(2))
        print('Max value is:',np.max(result).round(2))
        print('Min value is:',np.min(result).round(2))
elif(dataToPlot == 'Wind_Speed'):
    result = detect_inliers(wS)
    if result ==[]:
        print('Mean is: 0 ')
        print('S.D is: 0')
        print('Median is: 0')
        print('Max value is: 0')
        print('Min value is: 0')
    else:
        print('Mean is: ', np.mean(result).round(2))
        print('S.D is:',np.std(result).round(2))
        print('Median is: ',np.median(result).round(2))
        print('Max value is:',np.max(result).round(2))
        print('Min value is:',np.min(result).round(2))
elif(dataToPlot == 'Wind_Gust'):
    result = detect_inliers(wG)
    if result ==[]:
        print('Mean is: 0 ')
        print('S.D is: 0')
        print('Median is: 0')
        print('Max value is: 0')
        print('Min value is: 0')
    else:
        print('Mean is: ', np.mean(result).round(2))
        print('S.D is:',np.std(result).round(2))
        print('Median is: ',np.median(result).round(2))
        print('Max value is:',np.max(result).round(2))
        print('Min value is:',np.min(result).round(2))
elif(dataToPlot == 'Pressure'):
    result = detect_inliers(press)
    if result ==[]:
        print('Mean is: 0 ')
        print('S.D is: 0')
        print('Median is: 0')
        print('Max value is: 0')
        print('Min value is: 0')
    else:
        print('Mean is: ', np.mean(result).round(2))
        print('S.D is:',np.std(result).round(2))
        print('Median is: ',np.median(result).round(2))
        print('Max value is:',np.max(result).round(2))
        print('Min value is:',np.min(result).round(2))
elif(dataToPlot == 'Precipitation'):
    result = detect_inliers(preC)
    if result ==[]:
        print('Mean is: 0 ')
        print('S.D is: 0')
        print('Median is: 0')
        print('Max value is: 0')
        print('Min value is: 0')
    else:
        print('Mean is: ', np.mean(result).round(2))
        print('S.D is:',np.std(result).round(2))
        print('Median is: ',np.median(result).round(2))
        print('Max value is:',np.max(result).round(2))
        print('Min value is:',np.min(result).round(2))
elif(dataToPlot == 'Condition'):
    print()
elif(dataToPlot == 'Wind'):
    print()
else:
    print("Enter a correct data to process")
    

if(dataToPlot == 'Temperature'):
    plt.plot(result,"-o")
    plt.xlabel("Date")
    plt.ylabel("Temperature(C)")
    
elif(dataToPlot == 'Dew_Point'):
    plt.plot(result,"-o")
    plt.xlabel("Date")
    plt.ylabel("Dew Point(C)")
elif(dataToPlot == 'Humidity'):
    plt.plot(result,"-o")
    plt.xlabel("Date")
    plt.ylabel("Humidity(%)")
elif(dataToPlot == 'Wind'):
    plt.plot(w,"-o")
    plt.xlabel("Date")
    plt.ylabel("Wind")
elif(dataToPlot == 'Wind_Speed'):
    plt.plot(result,"-o")
    plt.xlabel("Date")
    plt.ylabel("Wind Speed(kmh)")
elif(dataToPlot == 'Wind_Gust'):
    plt.plot(result,"-o")
    plt.xlabel("Date")
    plt.ylabel("Wind Gust(kmh)")
elif(dataToPlot == 'Pressure'):
    plt.plot(result,"-o")
    plt.xlabel("Date")
    plt.ylabel("Pressure(in)")
elif(dataToPlot == 'Precipitation'):
    plt.plot(result,"-o")
    plt.xlabel("Date")
    plt.ylabel("Precipitation(in)")
elif(dataToPlot == 'Condition'):
    plt.plot(c,"-o")
    plt.xlabel("Date")
    plt.ylabel("Condition")    
else:
    print("Enter a correct data to plot")