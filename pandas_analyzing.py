# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 09:10:01 2023

@author: Marko
"""

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))

print(df.head())

print(df.tail())

print(df.info())