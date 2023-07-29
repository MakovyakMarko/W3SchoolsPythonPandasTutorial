# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 12:41:58 2023

@author: Marko
"""

import pandas as pd

df = pd.read_csv('training_data.csv')

df.loc[7, 'Duration'] = 45
print(df.head(8))
# редагуємо дані, щоб не було неправильних
for x in df.index:
    if df.loc[x,'Duration']>=60:
        df.loc[x,'Duration'] = 60
     
print(df.to_string())

# видаляємо рядки з неправильними даними
for x in df.index:
    if df.loc[x,'Duration']<45:
        df.drop(x, inplace=True)

print(df.to_string())