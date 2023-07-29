# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 09:54:20 2023

@author: Marko
"""

import pandas as pd

df = pd.read_csv("training_data.csv")
# перетворюємо значення на дати
df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())

df.dropna(subset=['Date'], inplace=True)
print(df.to_string())