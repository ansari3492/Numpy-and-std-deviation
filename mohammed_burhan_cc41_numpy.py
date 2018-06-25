# -*- coding: utf-8 -*-
"""
Created on Mon May 28 10:01:44 2018

@author: Lenovo
"""

import pandas as pd
import numpy as np
df=pd.read_csv("Automobile.csv")
price = pd.read_csv("Automobile.csv")

#Price['Price'] = Price['Price'].fillna(Price['Price'].mean())
price = price.fillna(price.mean())
x = np.array(price)

print(price.std())
print(price.var())
np.mean(price)