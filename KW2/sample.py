# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:58:39 2020

@author: Adewole
"""

import pandas as pd


df = pd.read_excel('Keffi_Weather_Mean.xlsx')
p = pd.period_range(start='2014',periods=len(df),freq='1M' )
#df.set_index(p,inplace=True)

#start_date = "2014-02-01 00:00:00"
#end_date = "2014-02-28 23:00:00"
#
#rng = df[start_date:end_date].dropna(how='any')
#
#print(rng.Temperature)

print(p)

q = pd.DataFrame(p)
print(q)

q.to_excel(r'C:\Users\Adewole\Documents\Astra_Agric\Keffi_Weather4\KW2\SX.xlsx')