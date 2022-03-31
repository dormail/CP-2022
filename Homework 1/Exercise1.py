# Exercise1.py
# Round off errors and computer arithmetic
import numpy as np
import matplotlib.pyplot as plt

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def formula1(n):
    result = 0
    for i in range(0,n+1):
        result = result + (-5)**i / factorial(i)
    return result

def formula2(n):
    result = 0
    for i in range(0,n+1):
        result = result + (5)**i / factorial(i)
    return 1/result

formula1 = np.vectorize(formula1)
formula2 = np.vectorize(formula2)

n_min = 1
n_max = 12
n = np.arange(n_min, n_max+1, 1)

exact = np.exp(-5)

plt.scatter(n, np.abs(formula1(n) - exact), label='Absolute Error Formula 1',
        marker='+')
plt.scatter(n, np.abs(formula2(n) - exact), label='Abosulte Error Formula 2',
        marker='+')

plt.legend()

plt.xlabel('$n$')

plt.savefig('build/Ex1.pdf')

