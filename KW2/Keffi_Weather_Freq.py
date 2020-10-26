# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:38:30 2020

@author: Adewole
"""

#import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter

df = pd.read_excel('Keffi_Weather_Combined2.xlsx')
p = pd.date_range(start='1/1/2014',periods=len(df),freq='1H' )
df.set_index(p,inplace=True)

Jan_date1 = "2014-01-01 00:00:00"
Jan_date2 = "2014-01-31 23:00:00"

Feb_date1 = "2014-02-01 00:00:00"
Feb_date2 = "2014-02-28 23:00:00"

Mar_date1 = "2014-03-01 00:00:00"
Mar_date2 = "2014-03-31 23:00:00"

Apr_date1 = "2014-04-01 00:00:00"
Apr_date2 = "2014-04-30 23:00:00"

May_date1 = "2014-05-01 00:00:00"
May_date2 = "2014-05-31 23:00:00"

June_date1 = "2014-06-01 00:00:00"
June_date2 = "2014-06-30 23:00:00"

July_date1 = "2014-07-01 00:00:00"
July_date2 = "2014-07-31 23:00:00"

Aug_date1 = "2014-08-01 00:00:00"
Aug_date2 = "2014-08-31 23:00:00"

Sept_date1 = "2014-09-01 00:00:00"
Sept_date2 = "2014-09-30 23:00:00"

Oct_date1 = "2014-10-01 00:00:00"
Oct_date2 = "2014-10-31 23:00:00"

Nov_date1 = "2014-11-01 00:00:00"
Nov_date2 = "2014-11-30 23:00:00"

Dec_date1 = "2014-12-01 00:00:00"
Dec_date2 = "2014-12-31 23:00:00"

rng1 = df[Jan_date1:Jan_date2].dropna(how='any')
rng2 = df[Feb_date1:Feb_date2].dropna(how='any')
rng3 = df[Mar_date1:Mar_date2].dropna(how='any')
rng4 = df[Apr_date1:Apr_date2].dropna(how='any')
rng5 = df[May_date1:May_date2].dropna(how='any')
rng6 = df[June_date1:June_date2].dropna(how='any')
rng7 = df[July_date1:July_date2].dropna(how='any')
rng8 = df[Aug_date1:Aug_date2].dropna(how='any')
rng9 = df[Sept_date1:Sept_date2].dropna(how='any')
rng10 = df[Oct_date1:Oct_date2].dropna(how='any')
rng11 = df[Nov_date1:Nov_date2].dropna(how='any')
rng12 = df[Dec_date1:Dec_date2].dropna(how='any')

#January
temp = rng1.Temperature
dewP = rng1.Dew_Point
hum = rng1.Humidity
wS = rng1.Wind_Speed
wG = rng1.Wind_Gust
press = rng1.Pressure
prec = rng1.Precipitation

temp1 = round((temp -32) * (5/9),2)
dewP1 = round((dewP - 32) * (5/9),2)
hum1 = hum

wS1 = round((wS * 1.60934),2)
wG1 = round((wG * 1.60934),2)
press1 = press
prec1 = prec

a111 = Counter(temp1).most_common(5)
a11 = list(a111)
a1 = a11[0][0]
b111 = Counter(dewP1).most_common(5)
b11 = list(b111)
b1 = b11[0][0]
c111 = Counter(hum1).most_common(5)
c11 = list(c111)
c1 = c11[0][0]
d111 = Counter(wS1).most_common(5)
d11 = list(d111)
d1 = d11[0][0]
e111 = Counter(wG1).most_common(5)
e11 = list(e111)
e1 = e11[0][0]
f111 = Counter(press1).most_common(5)
f11 = list(f111)
f1 = f11[0][0]
g111 = Counter(prec1).most_common(5)
g11 = list(g111)
g1 = g11[0][0]


#February
tempF = rng2.Temperature
dewPF = rng2.Dew_Point
humF = rng2.Humidity
wSF = rng2.Wind_Speed
wGF = rng2.Wind_Gust
pressF = rng2.Pressure
precF = rng2.Precipitation

tempF1 = round((tempF -32) * (5/9),2)
dewPF1 = round((dewPF - 32) * (5/9),2)
humF1 = humF

wSF1 = round((wSF * 1.60934),2)
wGF1 = round((wGF * 1.60934),2)
pressF1 = pressF
precF1 = precF

a112 = Counter(tempF1).most_common(5)
a12 = list(a112)
a2 = a12[0][0]
b112 = Counter(dewPF1).most_common(5)
b12 = list(b112)
b2 = b12[0][0]
c112 = Counter(humF1).most_common(5)
c12 = list(c112)
c2 = c12[0][0]
d112 = Counter(wSF1).most_common(5)
d12 = list(d112)
d2 = d12[0][0]
e112 = Counter(wGF1).most_common(5)
e12 = list(e112)
e2 = e12[0][0]
f112 = Counter(pressF1).most_common(5)
f12 = list(f112)
f2 = f12[0][0]
g112 = Counter(precF1).most_common(5)
g12 = list(g112)
g2 = g12[0][0]

#March
tempM = rng3.Temperature
dewPM = rng3.Dew_Point
humM = rng3.Humidity
wSM = rng3.Wind_Speed
wGM = rng3.Wind_Gust
pressM = rng3.Pressure
precM = rng3.Precipitation

tempM1 = round((tempM -32) * (5/9),2)
dewPM1 = round((dewPM - 32) * (5/9),2)
humM1 = humM

wSM1 = round((wSM * 1.60934),2)
wGM1 = round((wGM * 1.60934),2)
pressM1 = pressM
precM1 = precM

a113 = Counter(tempM1).most_common(5)
a13 = list(a113)
a3 = a13[0][0]
b113 = Counter(dewPM1).most_common(5)
b13 = list(b113)
b3 = b13[0][0]
c113 = Counter(humM1).most_common(5)
c13 = list(c113)
c3 = c13[0][0]
d113 = Counter(wSM1).most_common(5)
d13 = list(d113)
d3 = d13[0][0]
e113 = Counter(wGM1).most_common(5)
e13 = list(e113)
e3 = e13[0][0]
f113 = Counter(pressM1).most_common(5)
f13 = list(f113)
f3 = f13[0][0]
g113 = Counter(precM1).most_common(5)
g13 = list(g113)
g3 = g13[0][0]

#April
tempA = rng4.Temperature
dewPA = rng4.Dew_Point
humA = rng4.Humidity
wSA = rng4.Wind_Speed
wGA = rng4.Wind_Gust
pressA = rng4.Pressure
precA = rng4.Precipitation

tempA1 = round((tempA -32) * (5/9),2)
dewPA1 = round((dewPA - 32) * (5/9),2)
humA1 = humA

wSA1 = round((wSA * 1.60934),2)
wGA1 = round((wGA * 1.60934),2)
pressA1 = pressA
precA1 = precA

a114 = Counter(tempA1).most_common(5)
a14 = list(a114)
a4 = a14[0][0]
b114 = Counter(dewPA1).most_common(5)
b14 = list(b114)
b4 = b14[0][0]
c114 = Counter(humA1).most_common(5)
c14 = list(c114)
c4 = c14[0][0]
d114 = Counter(wSA1).most_common(5)
d14 = list(d114)
d4 = d14[0][0]
e114 = Counter(wGA1).most_common(5)
e14 = list(e114)
e4 = e14[0][0]
f114 = Counter(pressA1).most_common(5)
f14 = list(f114)
f4 = f14[0][0]
g114 = Counter(precA1).most_common(5)
g14 = list(g114)
g4 = g14[0][0]



data = {'Tempe':[a1,a2,a3,a4],
        'Dew_Point':[b1,b2,b3,b4],
        'Humidity':[c1,c2,c3,c4],
        'Wind_Speed':[d1,d2,d3,d4],
        'Wind_Gust':[e1,e2,e3,e4],
        'Pressure':[f1,f2,f3,f4],
        'Precipitation':[g1,g2,g3,f4]}
output = pd.DataFrame(data)
print(output)
#output.to_excel(r'C:\Users\Adewole\Documents\Astra_Agric\Keffi_Weather4\KW2\2020_Std.xlsx',index=False, header=True)

