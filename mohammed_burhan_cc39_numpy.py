# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:41:40 2018

@author: Lenovo
"""



import numpy as np
x = np.random.randint(5, 15, 40)
print("Original array:")
print(x)
print("Most frequent value in the above array:")
print(np.bincount(x).argmax())   #with numpy 

#without numpy
from collections import Counter

b = Counter(x)
c=b.most_common()
print(c)
dictionary=dict[c]
