# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 11:00:30 2020

@author: Adewole
"""

import pandas as pd
import matplotlib.pyplot as plt



#selection = 'Frequency'
#
#start_date = '2020-01'
#end_date = '2020-06'
#dataToPlot = 'Humidity'

def weatherData(a,b,c,d):
    
    df_mean = pd.read_excel('Keffi_Weather_Mean.xlsx')
    df_median = pd.read_excel('Keffi_Weather_Median.xlsx')
    df_std = pd.read_excel('Keffi_Weather_Std.xlsx')
    df_freq = pd.read_excel('Keffi_Weather_Frequency.xlsx')
    
    selection = a
    start_date = b
    end_date = c
    dataToPlot = d
    
    if(selection == 'Mean'):
      index_range = pd.date_range(start='2014-01', periods= len(df_mean), freq='MS')
      df_mean.set_index(index_range,inplace=True)
      rng = df_mean[start_date:end_date].dropna(how='any')
      date = rng.Date
      temp = rng.Temperature
      dewP = rng.Dew_Point
      hum = rng.Humidity
      wS = rng.Wind_Speed
      wG = rng.Wind_Gust
      press = rng.Pressure
      precip = rng.Precipitation
      
      if(dataToPlot == 'Temperature'):
          plt.plot(temp,"-o")
          plt.xlabel("Date")
          plt.ylabel("Temperature(C)") 
      elif(dataToPlot == 'Dew_Point'):
          plt.plot(dewP,"-o")
          plt.xlabel("Date")
          plt.ylabel("Dew Point(C)")
      elif(dataToPlot == 'Humidity'):
          plt.plot(hum, "-o")
          plt.xlabel("Date")
          plt.ylabel("Humidity(%)")
      elif(dataToPlot == 'Wind_Speed'):
          plt.plot(wS, "-o")
          plt.xlabel("Date")
          plt.ylabel("Wind Speed(kmh)")
      elif(dataToPlot == 'Wind_Gust'):
          plt.plot(wG, '-o')
          plt.xlabel("Date")
          plt.ylabel("Wind Gust(kmh)")
      elif(dataToPlot == 'Pressure'):
          plt.plot(press, '-o')
          plt.xlabel("Date")
          plt.ylabel("Pressure(in)")
      elif(dataToPlot == 'Precipitation'):
          plt.plot(precip, '-o')
          plt.xlabel("Date")
          plt.ylabel("Precipitation(in)")
      else:
          print("Select the weather to plot")
    elif(selection == 'Median'):
        index_range = pd.date_range(start='2014-01', periods= len(df_median), freq='MS')
        df_median.set_index(index_range,inplace=True)
        rng = df_median[start_date:end_date].dropna(how='any')
        date = rng.Date
        temp = rng.Temperature
        dewP = rng.Dew_Point
        hum = rng.Humidity
        wS = rng.Wind_Speed
        wG = rng.Wind_Gust
        press = rng.Pressure
        precip = rng.Precipitation
      
        if(dataToPlot == 'Temperature'):
            plt.plot(temp,"-o")
            plt.xlabel("Date")
            plt.ylabel("Temperature(C)") 
        elif(dataToPlot == 'Dew_Point'):
            plt.plot(dewP,"-o")
            plt.xlabel("Date")
            plt.ylabel("Dew Point(C)")
        elif(dataToPlot == 'Humidity'):
            plt.plot(hum, "-o")
            plt.xlabel("Date")
            plt.ylabel("Humidity(%)")
        elif(dataToPlot == 'Wind_Speed'):
            plt.plot(wS, "-o")
            plt.xlabel("Date")
            plt.ylabel("Wind Speed(kmh)")
        elif(dataToPlot == 'Wind_Gust'):
            plt.plot(wG, '-o')
            plt.xlabel("Date")
            plt.ylabel("Wind Gust(kmh)")
        elif(dataToPlot == 'Pressure'):
            plt.plot(press, '-o')
            plt.xlabel("Date")
            plt.ylabel("Pressure(in)")
        elif(dataToPlot == 'Precipitation'):
            plt.plot(precip, '-o')
            plt.xlabel("Date")
            plt.ylabel("Precipitation(in)")
        else:
            print("Select the weather to plot")
    elif(selection == 'Standard_Deviation'):
        index_range = pd.date_range(start='2014-01', periods= len(df_std), freq='MS')
        df_std.set_index(index_range,inplace=True)
        rng = df_std[start_date:end_date].dropna(how='any')
        date = rng.Date
        temp = rng.Temperature
        dewP = rng.Dew_Point
        hum = rng.Humidity
        wS = rng.Wind_Speed
        wG = rng.Wind_Gust
        press = rng.Pressure
        precip = rng.Precipitation
      
        if(dataToPlot == 'Temperature'):
            plt.plot(temp,"-o")
            plt.xlabel("Date")
            plt.ylabel("Temperature(C)") 
        elif(dataToPlot == 'Dew_Point'):
            plt.plot(dewP,"-o")
            plt.xlabel("Date")
            plt.ylabel("Dew Point(C)")
        elif(dataToPlot == 'Humidity'):
            plt.plot(hum, "-o")
            plt.xlabel("Date")
            plt.ylabel("Humidity(%)")
        elif(dataToPlot == 'Wind_Speed'):
            plt.plot(wS, "-o")
            plt.xlabel("Date")
            plt.ylabel("Wind Speed(kmh)")
        elif(dataToPlot == 'Wind_Gust'):
            plt.plot(wG, '-o')
            plt.xlabel("Date")
            plt.ylabel("Wind Gust(kmh)")
        elif(dataToPlot == 'Pressure'):
            plt.plot(press, '-o')
            plt.xlabel("Date")
            plt.ylabel("Pressure(in)")
        elif(dataToPlot == 'Precipitation'):
            plt.plot(precip, '-o')
            plt.xlabel("Date")
            plt.ylabel("Precipitation(in)")
        else:
            print("Select the weather to plot")
    elif(selection == 'Frequency'):
        index_range = pd.date_range(start='2014-01', periods= len(df_freq), freq='MS')
        df_freq.set_index(index_range,inplace=True)
        rng = df_freq[start_date:end_date].dropna(how='any')
        date = rng.Date
        temp = rng.Temperature
        dewP = rng.Dew_Point
        hum = rng.Humidity
        wS = rng.Wind_Speed
        wG = rng.Wind_Gust
        press = rng.Pressure
        precip = rng.Precipitation
      
        if(dataToPlot == 'Temperature'):
            plt.plot(temp,"-o")
            plt.xlabel("Date")
            plt.ylabel("Temperature(C)") 
        elif(dataToPlot == 'Dew_Point'):
            plt.plot(dewP,"-o")
            plt.xlabel("Date")
            plt.ylabel("Dew Point(C)")
        elif(dataToPlot == 'Humidity'):
            plt.plot(hum, "-o")
            plt.xlabel("Date")
            plt.ylabel("Humidity(%)")
        elif(dataToPlot == 'Wind_Speed'):
            plt.plot(wS, "-o")
            plt.xlabel("Date")
            plt.ylabel("Wind Speed(kmh)")
        elif(dataToPlot == 'Wind_Gust'):
            plt.plot(wG, '-o')
            plt.xlabel("Date")
            plt.ylabel("Wind Gust(kmh)")
        elif(dataToPlot == 'Pressure'):
            plt.plot(press, '-o')
            plt.xlabel("Date")
            plt.ylabel("Pressure(in)")
        elif(dataToPlot == 'Precipitation'):
            plt.plot(precip, '-o')
            plt.xlabel("Date")
            plt.ylabel("Precipitation(in)")
        else:
            print("Select the weather to plot")
    else:
        print("Select the right one to analyse")
