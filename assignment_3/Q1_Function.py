#!/usr/bin/env python
# coding: utf-8

# In[17]:

import numpy as np

def diverged(x, y, res = 500, max_iter = 100):
    """
    Parameters:
    x, y : array like
           Between -2 and 2, of the same size
           
    res : size of the array
          Pre-set value is 500
          
    max_iter : Number of iterations 
               Pre-set value is 100
    Returns: 
    diverged : array-like, bool
               If a value of c leads to divergence in max_iter, the corresponding 
               bool entry is changed to "True"
               
    it_of_div : array-like, int
                records the iteration of divergence (considered to be |z| > 2)"""

    # setting up output arrays
    diverge = np.zeros((res, res), dtype=bool) 
    it_of_div = np.zeros((res, res), dtype=int)

    # Iterate over pixels
    for row in range(res):
        for col in range(res): #iterating through x, y linspaces
            c = x[col] + 1j * y[row]
            z = 0 # initial z = z0

            for i in range(max_iter):
                z = z*z + c
                if abs(z) > 2:
                    diverge[row, col] = True 
                    it_of_div[row, col] = i
                    break
            else:
                it_of_div[row, col] = max_iter
                
    return diverge, it_of_div

