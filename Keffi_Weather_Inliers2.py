# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:54:11 2020

@author: Adewole
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
start_date = "2014-01-01 00:00:00"
end_date = "2020-09-30 23:00:00"
dataToPlot = 'Pressure'

df = pd.read_excel('Keffi_Weather_Combined_Updated.xlsx')
#p = pd.date_range(start='1/1/2014',periods=len(df),freq='1H' )
#df.set_index(p,inplace=True)


date = df['Date_Time']
temp = df['Temperature']
dewP = df['Dew_Point']
hum = df['Humidity']
wind = df['Wind']
wS = df['Wind_Speed']
wG = df['Wind_Gust']
press = df['Pressure']
preC = df['Precipitation']
c = df['Condition']

temp1 = temp.astype('str')
dewP1 = dewP.astype('str')
hum1 = hum.astype('str')
wind1 = wind.astype('str')
windSpeed1 = wS.astype('str')
windGust1 = wG.astype('str')
pressure1 = press.astype('str')
precip1 = preC.astype('str')
condition1 = c.astype('str')
date_time1 = date.astype('str')

temp2 = temp1.str.extract(r'([0-9]+)')
dewP2 = dewP1.str.extract(r'([0-9]+)')
humidity2 = hum1.str.extract(r'([0-9]+)')
wind2 = wind1.str.extract(r'([0-9]+)')
windSpeed2 = windSpeed1.str.extract(r'([0-9]+)')
windGust2 = windGust1.str.extract(r'([0-9]+)')
pressure2 = pressure1.str.extract(r'([\d\.\d]+)')
precip2 = precip1.str.extract(r'([\d\.\d]+)')
condition2 = condition1
date_time2 = date_time1.str.extract(r'(^.{0,16})')

df['Date_Time'] = date_time2
df['Temperature'] = temp2
df['Dew_Point'] = dewP2
df['Humidity'] = humidity2
df['Wind'] = wind2
df['Wind_Speed'] = windSpeed2
df['Wind_Gust'] = windGust2
df['Pressure'] = pressure2
df['Precipitation'] = precip2
df['Condition'] = condition2



df.to_excel(r'C:\Users\Adewole\Documents\Astra_Agric\Keffi_Weather4\Keffi_Weather_Combined2.xlsx', index = False, header=True)
#rng = df[start_date:end_date].dropna(how='any')

#temperature = rng.Temperature
#dewPoint = rng.Dew_Point
#humidity = rng.Humidity
#wind = rng.Wind
#windSpeed = rng.Wind_Speed
#windGust = rng.Wind_Gust
#pressure = rng.Pressure
#precip = rng.Precip
#condition = rng.Condition
#date_time = rng.Date_Time

#data = {'Date_Time':[date_time], 'Pressure':[pressure]}
#a = pd.DataFrame(data)
#print(a)
#print(rng)
#print(pressure)
#pressure2 = pressure.str.extract(r'([\d\.\d]+)')
#print(type(pressure2))
#print(pressure2)