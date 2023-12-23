import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

test = "Hello World"
print(test)

# Numpy is the main package for scientific computing in python
t_x = np.array([1, 2,3])

def sigmoid(z):
    return 1/ (1 + np.exp(-z))

def sigmoid_derivative(z):
    s = 1/(1 + np.exp(-z))
    ds = s*(1 - s)
    return ds

# np.shape --> Get the shape of a numpy array
# np.reshape --> Reshape the dim of an array to some other dim

# Unrolling 3D array to 1D vector
# (length, height, depth)-->v.shape((l*h*d, 1))


