# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:57:18 2019

@author: moi
"""

import numpy as np

# loss function and its derivative
def mse(y_true, y_pred):
    return np.mean(np.power(y_true-y_pred, 2))

def mse_prime(y_true, y_pred):
    return 2*(y_pred-y_true)/y_true.size
