# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 12:48:50 2023

@author: Marko
"""

import pandas as pd

df = pd.read_csv('training_data.csv')

print(df.duplicated())

df.drop_duplicates(inplace=True)
print(df.to_string())