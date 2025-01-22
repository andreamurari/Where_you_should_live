# -*- coding: utf-8 -*-
"""Where_you_should_live

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S369334tf2NQFHsTfJZBmtRgd4zxLcUU
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import builtins as bt

ds = pd.read_csv('/content/Quality_of_Life.csv')

category = ds.select_dtypes(include=['object']).columns
value = ds.select_dtypes(include=['float64']).columns
ds.drop(category.drop(['country']), axis=1,  inplace= True)

ds = ds[~(ds == 0).any(axis=1)]
ds ['Purchasing Power Value'] = 100*(ds ['Purchasing Power Value']/max(ds ['Purchasing Power Value']))
ds ['Safety Value'] = 100*(ds ['Safety Value']/max(ds ['Safety Value']))
ds ['Health Care Value'] = 100*(ds ['Health Care Value']/max(ds ['Health Care Value']))
ds ['Climate Value'] = 100*(ds ['Climate Value']/max(ds ['Climate Value']))
ds ['Cost of Living Value'] = 100*(ds ['Cost of Living Value']/max(ds ['Cost of Living Value']))
ds ['Traffic Commute Time Value'] = 100*(ds ['Traffic Commute Time Value']/max(ds ['Traffic Commute Time Value']))
ds ['Pollution Value'] = 100*(ds ['Pollution Value']/max(ds ['Pollution Value']))

a = float(bt.input("EN: On a scale of 1 to 5 how important it is to you the purchaising power? \nIT: In una scala da 1 a 5 quanto è importante il potere d'acquisto? \n\n"))
b = float(bt.input("\n\nEN: On a scale of 1 to 5 how important it is to you the safety? \nIT: In una scala da 1 a 5 quanto è importante la sicurezza? \n\n"))
c = float(bt.input("\n\nEN: On a scale of 1 to 5 how important it is to you the health care? \nIT: In una scala da 1 a 5 quanto è importante la salute? \n\n"))
d = float(bt.input("\n\nEN: On a scale of 1 to 5 how important it is to you the climate? \nIT: In una scala da 1 a 5 quanto è importante il clima? \n\n"))
e = float(bt.input("\n\nEN: On a scale of 1 to 5 how important it is to you to have a low cost of living? \nIT: In una scala da 1 a 5 quanto è importante che il costo della vita sia basso? \n\n"))
f = float(bt.input("\n\nEN: On a scale of 1 to 5 how important it is to you the traffic commute time? \nIT: In una scala da 1 a 5 quanto è importante il tempo di percorrenza del traffico? \n\n"))
g = float(bt.input("\n\nEN: On a scale of 1 to 5 how important it is to you the pollution rate? \nIT: In una scala da 1 a 5 quanto è importante il tasso d'inquinamento? \n\n"))
"""
a = 1
b = 5
c = 5
d = 1
e = 1
f = 1
g = 5"""

ds ['Total weighted score'] = ds.iloc [:,1]*a + ds.iloc [:,2]*b + ds.iloc [:,3]*c + ds.iloc [:,4]*d + ds.iloc [:,5]/e + ds.iloc [:,6]/f + ds.iloc [:,7]/g
ds.sort_values(by=['Total weighted score'], ascending=False, inplace = True)
ds.head(5)

