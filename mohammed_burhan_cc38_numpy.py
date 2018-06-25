# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:36:20 2018

@author: Lenovo
"""

import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(150,20,1000)
print(incomes)
plt.hist(incomes,100)
print(incomes.std())
print(incomes.var())