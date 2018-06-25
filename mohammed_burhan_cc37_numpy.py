# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:29:41 2018

@author: Lenovo
"""
import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
print(incomes)
plt.hist(incomes,50)
np.median(incomes)
np.mean(incomes)