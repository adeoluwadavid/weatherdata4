# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:06:10 2020

@author: Adewole
"""

import pandas as pd

a = pd.date_range(start='2014-01-01', end= '2020-10-01', freq='MS')

print(a)
b = pd.DataFrame(a)
print(b)
