# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 17:51:09 2023

@author: Marko
"""

import pandas as pd

df = pd.read_csv('data.csv')
print(df.to_string())

print(df)

print(pd.options.display.max_rows)

pd.options.display.max_rows = 9999
print(df)