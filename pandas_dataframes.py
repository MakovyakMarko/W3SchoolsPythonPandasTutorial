# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 17:38:58 2023

@author: Marko
"""

import pandas as pd

data = {
        "calories":[420,380,390],
        "duration":[50,40,45]
        }

df = pd.DataFrame(data)
print(df)

# знайти рядок
print(df.loc[0])

# повернути рядок 0 і 1
print(df.loc[[0,1]])

# створення власних індексів
df = pd.DataFrame(data, index =["day1","day2","day3"])
print(df)
print(df.loc["day2"])

# завантаження файлу в DataFrame
df = pd.read_csv("world-data-2023.csv")
print(df)