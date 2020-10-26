# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:38:30 2020

@author: Adewole
"""

#import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel('Keffi_Weather_Combined2.xlsx')
p = pd.date_range(start='1/1/2014',periods=len(df),freq='1H' )
df.set_index(p,inplace=True)

Jan_date1 = "2020-01-01 00:00:00"
Jan_date2 = "2020-01-31 23:00:00"

Feb_date1 = "2020-02-01 00:00:00"
Feb_date2 = "2020-02-28 23:00:00"

Mar_date1 = "2020-03-01 00:00:00"
Mar_date2 = "2020-03-31 23:00:00"

Apr_date1 = "2020-04-01 00:00:00"
Apr_date2 = "2020-04-30 23:00:00"

May_date1 = "2020-05-01 00:00:00"
May_date2 = "2020-05-31 23:00:00"

June_date1 = "2020-06-01 00:00:00"
June_date2 = "2020-06-30 23:00:00"

July_date1 = "2020-07-01 00:00:00"
July_date2 = "2020-07-31 23:00:00"

Aug_date1 = "2020-08-01 00:00:00"
Aug_date2 = "2020-08-31 23:00:00"

Sept_date1 = "2020-09-01 00:00:00"
Sept_date2 = "2020-09-30 23:00:00"

#Oct_date1 = "2019-10-01 00:00:00"
#Oct_date2 = "2019-10-31 23:00:00"
#
#Nov_date1 = "2019-11-01 00:00:00"
#Nov_date2 = "2019-11-30 23:00:00"
#
#Dec_date1 = "2019-12-01 00:00:00"
#Dec_date2 = "2019-12-31 23:00:00"

rng1 = df[Jan_date1:Jan_date2].dropna(how='any')
rng2 = df[Feb_date1:Feb_date2].dropna(how='any')
rng3 = df[Mar_date1:Mar_date2].dropna(how='any')
rng4 = df[Apr_date1:Apr_date2].dropna(how='any')
rng5 = df[May_date1:May_date2].dropna(how='any')
rng6 = df[June_date1:June_date2].dropna(how='any')
rng7 = df[July_date1:July_date2].dropna(how='any')
rng8 = df[Aug_date1:Aug_date2].dropna(how='any')
rng9 = df[Sept_date1:Sept_date2].dropna(how='any')
#rng10 = df[Oct_date1:Oct_date2].dropna(how='any')
#rng11 = df[Nov_date1:Nov_date2].dropna(how='any')
#rng12 = df[Dec_date1:Dec_date2].dropna(how='any')


#January
temp = rng1.Temperature
dewP = rng1.Dew_Point
hum = rng1.Humidity
wS = rng1.Wind_Speed
wG = rng1.Wind_Gust
press = rng1.Pressure
prec = rng1.Precipitation

temp1 = (temp -32) * (5/9)
dewP1 = (dewP - 32) * (5/9)
hum1 = hum
wS1 = wS * 1.60934
wG1 = wG * 1.60934
press1 = press
prec1 = prec

a1 = round(np.std(temp1),2)
b1 = round(np.std(dewP1),2)
c1 = round(np.std(hum1),2)
d1 = round(np.std(wS1),2)
e1 = round(np.std(wG1),2)
f1 = round(np.std(press1),2)
g1 = round(np.std(prec1),2)


#February
tempF = rng2.Temperature
dewPF = rng2.Dew_Point
humF = rng2.Humidity
wSF = rng2.Wind_Speed
wGF = rng2.Wind_Gust
pressF = rng2.Pressure
precF = rng2.Precipitation

tempF1 = (tempF -32) * (5/9)
dewPF1 = (dewPF - 32) * (5/9)
humF1 = humF
wSF1 = wSF * 1.60934
wGF1 = wGF * 1.60934
pressF1 = pressF
precF1 = precF

a2 = round(np.std(tempF1),2)
b2 = round(np.std(dewPF1),2)
c2 = round(np.std(humF1),2)
d2 = round(np.std(wSF1),2)
e2 = round(np.std(wGF1),2)
f2 = round(np.std(pressF1),2)
g2 = round(np.std(precF1),2)

#March
tempM = rng3.Temperature
dewPM = rng3.Dew_Point
humM = rng3.Humidity
wSM = rng3.Wind_Speed
wGM = rng3.Wind_Gust
pressM = rng3.Pressure
precM = rng3.Precipitation

tempM1 = (tempM -32) * (5/9)
dewPM1 = (dewPM - 32) * (5/9)
humM1 = humM
wSM1 = wSM * 1.60934
wGM1 = wGM * 1.60934
pressM1 = pressM
precM1 = precM


a3 = round(np.std(tempM1),2)
b3 = round(np.std(dewPM1),2)
c3 = round(np.std(humM1),2)
d3 = round(np.std(wSM1),2)
e3 = round(np.std(wGM1),2)
f3 = round(np.std(pressM1),2)
g3 = round(np.std(precM1),2)

#April
tempA = rng4.Temperature
dewPA = rng4.Dew_Point
humA = rng4.Humidity
wSA = rng4.Wind_Speed
wGA = rng4.Wind_Gust
pressA = rng4.Pressure
precA = rng4.Precipitation

tempA1 = (tempA -32) * (5/9)
dewPA1 = (dewPA - 32) * (5/9)
humA1 = humA
wSA1 = wSA * 1.60934
wGA1 = wGA * 1.60934
pressA1 = pressA
precA1 = precA


a4 = round(np.std(tempA1),2)
b4 = round(np.std(dewPA1),2)
c4 = round(np.std(humA1),2)
d4 = round(np.std(wSA1),2)
e4 = round(np.std(wGA1),2)
f4 = round(np.std(pressA1),2)
g4 = round(np.std(precA1),2)

#May
tempMa = rng5.Temperature
dewPMa = rng5.Dew_Point
humMa = rng5.Humidity
wSMa = rng5.Wind_Speed
wGMa = rng5.Wind_Gust
pressMa = rng5.Pressure
precMa = rng5.Precipitation

tempMa1 = (tempMa -32) * (5/9)
dewPMa1 = (dewPMa - 32) * (5/9)
humMa1 = humMa
wSMa1 = wSMa * 1.60934
wGMa1 = wGMa * 1.60934
pressMa1 = pressMa
precMa1 = precMa


a5 = round(np.std(tempMa1),2)
b5 = round(np.std(dewPMa1),2)
c5 = round(np.std(humMa1),2)
d5 = round(np.std(wSMa1),2)
e5 = round(np.std(wGMa1),2)
f5 = round(np.std(pressMa1),2)
g5 = round(np.std(precMa1),2)

#June
tempJ = rng6.Temperature
dewPJ = rng6.Dew_Point
humJ = rng6.Humidity
wSJ = rng6.Wind_Speed
wGJ = rng6.Wind_Gust
pressJ = rng6.Pressure
precJ= rng6.Precipitation

tempJ1 = (tempJ -32) * (5/9)
dewPJ1 = (dewPJ - 32) * (5/9)
humJ1 = humJ
wSJ1 = wSJ * 1.60934
wGJ1 = wGJ * 1.60934
pressJ1 = pressJ
precJ1 = precJ


a6 = round(np.std(tempJ1),2)
b6 = round(np.std(dewPJ1),2)
c6 = round(np.std(humJ1),2)
d6 = round(np.std(wSJ1),2)
e6 = round(np.std(wGJ1),2)
f6 = round(np.std(pressJ1),2)
g6 = round(np.std(precJ1),2)

#July
tempJu = rng7.Temperature
dewPJu = rng7.Dew_Point
humJu = rng7.Humidity
wSJu = rng7.Wind_Speed
wGJu = rng7.Wind_Gust
pressJu = rng7.Pressure
precJu = rng7.Precipitation

tempJu1 = (tempJu -32) * (5/9)
dewPJu1 = (dewPJu - 32) * (5/9)
humJu1 = humJu
wSJu1 = wSJu * 1.60934
wGJu1 = wGJu * 1.60934
pressJu1 = pressJu
precJu1 = precJu


a7 = round(np.std(tempJu1),2)
b7 = round(np.std(dewPJu1),2)
c7 = round(np.std(humJu1),2)
d7 = round(np.std(wSJu1),2)
e7 = round(np.std(wGJu1),2)
f7 = round(np.std(pressJu1),2)
g7 = round(np.std(precJu1),2)
#
#August
tempAu = rng8.Temperature
dewPAu = rng8.Dew_Point
humAu = rng8.Humidity
wSAu = rng8.Wind_Speed
wGAu = rng8.Wind_Gust
pressAu = rng8.Pressure
precAu = rng8.Precipitation

tempAu1 = (tempAu -32) * (5/9)
dewPAu1 = (dewPAu - 32) * (5/9)
humAu1 = humAu
wSAu1 = wSAu * 1.60934
wGAu1 = wGAu * 1.60934
pressAu1 = pressAu
precAu1 = precAu


a8 = round(np.std(tempAu1),2)
b8 = round(np.std(dewPAu1),2)
c8 = round(np.std(humAu1),2)
d8 = round(np.std(wSAu1),2)
e8 = round(np.std(wGAu1),2)
f8 = round(np.std(pressAu1),2)
g8 = round(np.std(precAu1),2)

#Sept
tempS = rng9.Temperature
dewPS = rng9.Dew_Point
humS = rng9.Humidity
wSS = rng9.Wind_Speed
wGS = rng9.Wind_Gust
pressS = rng9.Pressure
precS = rng9.Precipitation

tempS1 = (tempS -32) * (5/9)
dewPS1 = (dewPS - 32) * (5/9)
humS1 = humS
wSS1 = wSS * 1.60934
wGS1 = wGS * 1.60934
pressS1 = pressS
precS1 = precS


a9 = round(np.std(tempS1),2)
b9 = round(np.std(dewPS1),2)
c9 = round(np.std(humS1),2)
d9 = round(np.std(wSS1),2)
e9 = round(np.std(wGS1),2)
f9 = round(np.std(pressS1),2)
g9 = round(np.std(precS1),2)

##October
#tempO = rng10.Temperature
#dewPO = rng10.Dew_Point
#humO = rng10.Humidity
#wSO = rng10.Wind_Speed
#wGO = rng10.Wind_Gust
#pressO = rng10.Pressure
#precO = rng10.Precipitation
#
#tempO1 = (tempO -32) * (5/9)
#dewPO1 = (dewPO - 32) * (5/9)
#humO1 = humO
#wSO1 = wSO * 1.60934
#wGO1 = wGO * 1.60934
#pressO1 = pressO
#precO1 = precO
#
#
#a10 = round(np.std(tempO1),2)
#b10 = round(np.std(dewPO1),2)
#c10 = round(np.std(humO1),2)
#d10 = round(np.std(wSO1),2)
#e10 = round(np.std(wGO1),2)
#f10 = round(np.std(pressO1),2)
#g10 = round(np.std(precO1),2)
#
##November
#tempN = rng11.Temperature
#dewPN = rng11.Dew_Point
#humN = rng11.Humidity
#wSN = rng11.Wind_Speed
#wGN = rng11.Wind_Gust
#pressN = rng11.Pressure
#precN = rng11.Precipitation
#
#tempN1 = (tempN -32) * (5/9)
#dewPN1 = (dewPN - 32) * (5/9)
#humN1 = humN
#wSN1 = wSN * 1.60934
#wGN1 = wGN * 1.60934
#pressN1 = pressN
#precN1 = precN
#
#
#a11 = round(np.std(tempN1),2)
#b11 = round(np.std(dewPN1),2)
#c11 = round(np.std(humN1),2)
#d11 = round(np.std(wSN1),2)
#e11 = round(np.std(wGN1),2)
#f11 = round(np.std(pressN1),2)
#g11 = round(np.std(precN1),2)
#
##December
#tempD = rng12.Temperature
#dewPD = rng12.Dew_Point
#humD = rng12.Humidity
#wSD = rng12.Wind_Speed
#wGD = rng12.Wind_Gust
#pressD = rng12.Pressure
#precD = rng12.Precipitation
#
#tempD1 = (tempD -32) * (5/9)
#dewPD1 = (dewPD - 32) * (5/9)
#humD1 = humD
#wSD1 = wSD * 1.60934
#wGD1 = wGD * 1.60934
#pressD1 = pressD
#precD1 = precD
#
#
#a12 = round(np.std(tempD1),2)
#b12 = round(np.std(dewPD1),2)
#c12 = round(np.std(humD1),2)
#d12 = round(np.std(wSD1),2)
#e12 = round(np.std(wGD1),2)
#f12 = round(np.std(pressD1),2)
#g12 = round(np.std(precD1),2)

print()
data = {'Tempe':[a1,a2,a3,a4,a5,a6,a7,a8,a9,],
        'Dew_Point':[b1,b2,b3,b4,b5,b6,b7,b8,b9,],
        'Humidity':[c1,c2,c3,c4,c5,c6,c7,c8,c9,],
        'Wind_Speed':[d1,d2,d3,d4,d5,d6,d7,d8,d9,],
        'Wind_Gust':[e1,e2,e3,e4,e5,e6,e7,e8,e9,],
        'Pressure':[f1,f2,f3,f4,f5,f6,f7,f8,f9,],
        'Precipitation':[g1,g2,g3,g4,g5,g6,g7,g8,g9,]}
output = pd.DataFrame(data)
print(output)
output.to_excel(r'C:\Users\Adewole\Documents\Astra_Agric\Keffi_Weather4\KW2\2020_Std.xlsx',index=False, header=True)


##Median
#print('Temperature median: ',np.median(temp1))
#print('Dew Point median: ',np.median(dewP1))
#print('Humidity median: ',np.median(hum1))
#print('Wind Speed median: ',np.median(wS1))
#print('Wind Gust median: ',np.median(wG1))
#print('Pressure median: ',np.median(press1))
#print('Precipitation median: ',np.median(prec1))
#print()
##Standard Deviation
#print('Temperature sd: ', np.std(temp1))
#print('Dew Point sd: ', np.std(dewP1))
#print('Humidity sd: ', np.std(hum1))
#print('Wind Speed sd: ', np.std(wS1))
#print('Wind Gust sd: ', np.std(wG1))
#print('Pressure sd: ', np.std(press1))
#print('Precipitation sd: ', np.std(prec1))
#print()
##Frequency
#freq={}
#for item in temp1:
#    if item in freq:
#        freq[item] += 1
#    else:
#        freq[item] = 1
#print('Temp Freq:',(freq))
#print()
#
#freq={}
#for item in dewP1:
#    if item in freq:
#        freq[item] += 1
#    else:
#        freq[item] = 1
#print('Dew Point',freq)
#print()
#freq={}
#for item in hum1:
#    if item in freq:
#        freq[item] += 1
#    else:
#        freq[item] = 1
#print('Humidity',freq)
#print()
#freq={}
#for item in wS1:
#    if item in freq:
#        freq[item] += 1
#    else:
#        freq[item] = 1
#print('Wind Speed',freq)
#print()
#freq={}
#for item in wG1:
#    if item in freq:
#        freq[item] += 1
#    else:
#        freq[item] = 1
#print('Wind Gust',freq)
#print()
#freq={}
#for item in press1:
#    if item in freq:
#        freq[item] += 1
#    else:
#        freq[item] = 1
#print('Pressure',freq)
#print()
#freq={}
#for item in prec1:
#    if item in freq:
#        freq[item] += 1
#    else:
#        freq[item] = 1
#print('Precipitation',freq)