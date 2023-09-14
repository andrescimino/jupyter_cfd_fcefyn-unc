# -*- coding: utf-8 -*-
"""
Created on Tue May 26 19:09:52 2020

@author: andres
"""
import numpy as np

x = np.arange(10)
print(x)
print('x[2:10]=',x[2:10])

print('x[:-7]=',x[:-7])

print('x[1:7:2]=', x[1:7:2])

y = np.arange(35).reshape(5,7)
print('y', y)
print('y[1:5:2,::3]', y[1:5:2,::3])


u = np.array((0, 1, 2, 3, 4, 5))

for i in range(1, len(u)):
    print(u[i] - u[i-1])
    
print('u[1:]=', u[1:]) 
print(' u[0:-1]=', u[0:-1]) 