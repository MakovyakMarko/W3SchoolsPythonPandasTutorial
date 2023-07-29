# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 13:21:32 2023

@author: Marko
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

plt.show()

df["Duration"].plot(kind = 'hist')