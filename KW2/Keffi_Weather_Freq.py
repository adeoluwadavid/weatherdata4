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

Jan_date1 = "2017-01-01 00:00:00"
Jan_date2 = "2017-01-31 23:00:00"

Feb_date1 = "2017-02-01 00:00:00"
Feb_date2 = "2017-02-28 23:00:00"

Mar_date1 = "2017-03-01 00:00:00"
Mar_date2 = "2017-03-31 23:00:00"

Apr_date1 = "2017-04-01 00:00:00"
Apr_date2 = "2017-04-30 23:00:00"

May_date1 = "2017-05-01 00:00:00"
May_date2 = "2017-05-31 23:00:00"

June_date1 = "2017-06-01 00:00:00"
June_date2 = "2017-06-30 23:00:00"

July_date1 = "2017-07-01 00:00:00"
July_date2 = "2017-07-31 23:00:00"

Aug_date1 = "2017-08-01 00:00:00"
Aug_date2 = "2017-08-31 23:00:00"

Sept_date1 = "2017-09-01 00:00:00"
Sept_date2 = "2017-09-30 23:00:00"

Oct_date1 = "2017-10-01 00:00:00"
Oct_date2 = "2017-10-31 23:00:00"

Nov_date1 = "2017-11-01 00:00:00"
Nov_date2 = "2017-11-30 23:00:00"

Dec_date1 = "2017-12-01 00:00:00"
Dec_date2 = "2017-12-31 23:00:00"

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

#May
tempMa = rng5.Temperature
dewPMa = rng5.Dew_Point
humMa = rng5.Humidity
wSMa = rng5.Wind_Speed
wGMa = rng5.Wind_Gust
pressMa = rng5.Pressure
precMa = rng5.Precipitation

tempMa1 = round((tempMa -32) * (5/9),2)
dewPMa1 = round((dewPMa - 32) * (5/9),2)
humMa1 = humMa

wSMa1 = round((wSMa * 1.60934),2)
wGMa1 = round((wGMa * 1.60934),2)
pressMa1 = pressMa
precMa1 = precMa

a115 = Counter(tempMa1).most_common(5)
a15 = list(a115)
a5 = a15[0][0]
b115 = Counter(dewPMa1).most_common(5)
b15 = list(b115)
b5 = b15[0][0]
c115 = Counter(humMa1).most_common(5)
c15 = list(c115)
c5 = c15[0][0]
d115 = Counter(wSMa1).most_common(5)
d15 = list(d115)
d5 = d15[0][0]
e115 = Counter(wGMa1).most_common(5)
e15 = list(e115)
e5 = e15[0][0]
f115 = Counter(pressMa1).most_common(5)
f15 = list(f115)
f5 = f15[0][0]
g115 = Counter(precMa1).most_common(5)
g15 = list(g115)
g5 = g15[0][0]

#June
tempJ = rng6.Temperature
dewPJ = rng6.Dew_Point
humJ = rng6.Humidity
wSJ = rng6.Wind_Speed
wGJ = rng6.Wind_Gust
pressJ = rng6.Pressure
precJ = rng6.Precipitation

tempJ1 = round((tempJ -32) * (5/9),2)
dewPJ1 = round((dewPJ - 32) * (5/9),2)
humJ1 = humJ

wSJ1 = round((wSJ * 1.60934),2)
wGJ1 = round((wGJ * 1.60934),2)
pressJ1 = pressJ
precJ1 = precJ

a116 = Counter(tempJ1).most_common(5)
a16 = list(a116)
a6 = a16[0][0]
b116 = Counter(dewPJ1).most_common(5)
b16 = list(b116)
b6 = b16[0][0]
c116 = Counter(humJ1).most_common(5)
c16 = list(c116)
c6 = c16[0][0]
d116 = Counter(wSJ1).most_common(5)
d16 = list(d116)
d6 = d16[0][0]
e116 = Counter(wGJ1).most_common(5)
e16 = list(e116)
e6 = e16[0][0]
f116 = Counter(pressJ1).most_common(5)
f16 = list(f116)
f6 = f16[0][0]
g116 = Counter(precJ1).most_common(5)
g16 = list(g116)
g6 = g16[0][0]

#July
tempJu = rng7.Temperature
dewPJu = rng7.Dew_Point
humJu = rng7.Humidity
wSJu = rng7.Wind_Speed
wGJu = rng7.Wind_Gust
pressJu = rng7.Pressure
precJu = rng7.Precipitation

tempJu1 = round((tempJu -32) * (5/9),2)
dewPJu1 = round((dewPJu - 32) * (5/9),2)
humJu1 = humJu

wSJu1 = round((wSJu * 1.60934),2)
wGJu1 = round((wGJu * 1.60934),2)
pressJu1 = pressJu
precJu1 = precJu

a117 = Counter(tempJu1).most_common(5)
a17 = list(a117)
a7 = a17[0][0]
b117 = Counter(dewPJu1).most_common(5)
b17 = list(b117)
b7 = b17[0][0]
c117 = Counter(humJu1).most_common(5)
c17 = list(c117)
c7 = c17[0][0]
d117 = Counter(wSJu1).most_common(5)
d17 = list(d117)
d7 = d17[0][0]
e117 = Counter(wGJu1).most_common(5)
e17 = list(e117)
e7 = e17[0][0]
f117 = Counter(pressJu1).most_common(5)
f17 = list(f117)
f7 = f17[0][0]
g117 = Counter(precJu1).most_common(5)
g17 = list(g117)
g7 = g17[0][0]

#August
tempAu = rng8.Temperature
dewPAu = rng8.Dew_Point
humAu = rng8.Humidity
wSAu = rng8.Wind_Speed
wGAu = rng8.Wind_Gust
pressAu = rng8.Pressure
precAu = rng8.Precipitation

tempAu1 = round((tempAu -32) * (5/9),2)
dewPAu1 = round((dewPAu - 32) * (5/9),2)
humAu1 = humAu

wSAu1 = round((wSAu * 1.60934),2)
wGAu1 = round((wGAu * 1.60934),2)
pressAu1 = pressAu
precAu1 = precAu

a118 = Counter(tempAu1).most_common(5)
a18 = list(a118)
a8 = a18[0][0]
b118 = Counter(dewPAu1).most_common(5)
b18 = list(b118)
b8 = b18[0][0]
c118 = Counter(humAu1).most_common(5)
c18 = list(c118)
c8 = c18[0][0]
d118 = Counter(wSAu1).most_common(5)
d18 = list(d118)
d8 = d18[0][0]
e118 = Counter(wGAu1).most_common(5)
e18 = list(e118)
e8 = e18[0][0]
f118 = Counter(pressAu1).most_common(5)
f18 = list(f118)
f8 = f18[0][0]
g118 = Counter(precAu1).most_common(5)
g18 = list(g118)
g8 = g18[0][0]

#September
tempS = rng9.Temperature
dewPS = rng9.Dew_Point
humS = rng9.Humidity
wSS = rng9.Wind_Speed
wGS = rng9.Wind_Gust
pressS = rng9.Pressure
precS = rng9.Precipitation

tempS1 = round((tempS -32) * (5/9),2)
dewPS1 = round((dewPS - 32) * (5/9),2)
humS1 = humS

wSS1 = round((wSS * 1.60934),2)
wGS1 = round((wGS * 1.60934),2)
pressS1 = pressS
precS1 = precS

a119 = Counter(tempS1).most_common(5)
a19 = list(a119)
a9 = a19[0][0]
b119 = Counter(dewPS1).most_common(5)
b19 = list(b119)
b9 = b19[0][0]
c119 = Counter(humS1).most_common(5)
c19 = list(c119)
c9 = c19[0][0]
d119 = Counter(wSS1).most_common(5)
d19 = list(d119)
d9 = d19[0][0]
e119 = Counter(wGS1).most_common(5)
e19 = list(e119)
e9 = e19[0][0]
f119 = Counter(pressS1).most_common(5)
f19 = list(f119)
f9 = f19[0][0]
g119 = Counter(precS1).most_common(5)
g19 = list(g119)
g9 = g19[0][0]

#October
tempO = rng10.Temperature
dewPO = rng10.Dew_Point
humO = rng10.Humidity
wSO = rng10.Wind_Speed
wGO = rng10.Wind_Gust
pressO = rng10.Pressure
precO = rng10.Precipitation

tempO1 = round((tempO -32) * (5/9),2)
dewPO1 = round((dewPO - 32) * (5/9),2)
humO1 = humO

wSO1 = round((wSO * 1.60934),2)
wGO1 = round((wGO * 1.60934),2)
pressO1 = pressO
precO1 = precO

a1110 = Counter(tempO1).most_common(5)
a110 = list(a1110)
a10 = a110[0][0]
b1110 = Counter(dewPO1).most_common(5)
b110 = list(b1110)
b10 = b110[0][0]
c1110 = Counter(humO1).most_common(5)
c110 = list(c1110)
c10 = c110[0][0]
d1110 = Counter(wSO1).most_common(5)
d110 = list(d1110)
d10 = d110[0][0]
e1110 = Counter(wGO1).most_common(5)
e110 = list(e1110)
e10 = e110[0][0]
f1110 = Counter(pressO1).most_common(5)
f110 = list(f1110)
f10 = f110[0][0]
g1110 = Counter(precO1).most_common(5)
g110 = list(g1110)
g10 = g110[0][0]

#November
tempN = rng11.Temperature
dewPN = rng11.Dew_Point
humN = rng11.Humidity
wSN = rng11.Wind_Speed
wGN = rng11.Wind_Gust
pressN = rng11.Pressure
precN = rng11.Precipitation

tempN1 = round((tempN -32) * (5/9),2)
dewPN1 = round((dewPN - 32) * (5/9),2)
humN1 = humN

wSN1 = round((wSN * 1.60934),2)
wGN1 = round((wGN * 1.60934),2)
pressN1 = pressN
precN1 = precN

a1111 = Counter(tempN1).most_common(5)
a111 = list(a1111)
a11 = a111[0][0]
b1111 = Counter(dewPN1).most_common(5)
b111 = list(b1111)
b11 = b111[0][0]
c1111 = Counter(humN1).most_common(5)
c111 = list(c1111)
c11 = c111[0][0]
d1111 = Counter(wSN1).most_common(5)
d111 = list(d1111)
d11 = d111[0][0]
e1111 = Counter(wGN1).most_common(5)
e111 = list(e1111)
e11 = e111[0][0]
f1111 = Counter(pressN1).most_common(5)
f111 = list(f1111)
f11 = f111[0][0]
g1111 = Counter(precN1).most_common(5)
g111 = list(g1111)
g11 = g111[0][0]


#December
tempD = rng12.Temperature
dewPD = rng12.Dew_Point
humD = rng12.Humidity
wSD = rng12.Wind_Speed
wGD = rng12.Wind_Gust
pressD = rng12.Pressure
precD = rng12.Precipitation

tempD1 = round((tempD -32) * (5/9),2)
dewPD1 = round((dewPD - 32) * (5/9),2)
humD1 = humD

wSD1 = round((wSD * 1.60934),2)
wGD1 = round((wGD * 1.60934),2)
pressD1 = pressD
precD1 = precD

a1112 = Counter(tempD1).most_common(5)
a112 = list(a1112)
a12 = a112[0][0]
b1112 = Counter(dewPD1).most_common(5)
b112 = list(b1112)
b12 = b112[0][0]
c1112 = Counter(humD1).most_common(5)
c112 = list(c1112)
c12 = c112[0][0]
d1112 = Counter(wSD1).most_common(5)
d112 = list(d1112)
d12 = d112[0][0]
e1112 = Counter(wGD1).most_common(5)
e112 = list(e1112)
e12 = e112[0][0]
f1112 = Counter(pressD1).most_common(5)
f112 = list(f1112)
f12 = f112[0][0]
g1112 = Counter(precD1).most_common(5)
g112 = list(g1112)
g12 = g112[0][0]


data = {'Tempe':[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12],
        'Dew_Point':[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12],
        'Humidity':[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12],
        'Wind_Speed':[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12],
        'Wind_Gust':[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12],
        'Pressure':[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12],
        'Precipitation':[g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12]}
output = pd.DataFrame(data)
print(output)

#print(Counter(humAu1))
#print(humAu1)
#output.to_excel(r'C:\Users\Adewole\Documents\Astra_Agric\Keffi_Weather4\KW2\2018_Freq.xlsx',index=False, header=True)

