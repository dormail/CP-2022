# tests for exercise 3

import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt

def f(x, alpha):
    res = 2 * np.power(1-x, 1 / (1-alpha))
    return res

f = np.vectorize(f)

x = rand(10000,1)

#hist, bin_edges = np.histogram(f(x,2), bins=10, range=(2,12))
#plt.hist(hist, bins=bin_edges)

n, bins, patches = plt.hist(f(x, 3), 50, density=True)
plt.yscale('log')
plt.xscale('log')

plt.show()

