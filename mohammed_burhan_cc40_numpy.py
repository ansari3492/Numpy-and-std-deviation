# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:31:19 2018

@author: Lenovo
"""

import numpy as np
my_array=input("enter the array value: ")
lst=my_array.split(' ')
myarray=np.asarray(lst)
a=myarray.reshape(3,3)
print(a)
