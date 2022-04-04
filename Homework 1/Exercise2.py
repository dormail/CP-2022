# Exercise2.py

# Some Euler Mascheroni constant stuff
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def formula1(n):
    result = 0
    for k in range(1,n+1):
        result = result + 1/k
    result = result - np.log(n)
    return result

def formula2(n):
    result = 0
    for k in range(1,n+1):
        result = result + (-1)**k * np.floor(np.log2(k)) / k
    return result

formula1 = np.vectorize(formula1)
formula2 = np.vectorize(formula2)

n_min = 100
n_max = 1000
n = np.arange(n_min, n_max+1, 20)
exact = .5772156649015

error1 = np.abs(formula1(n) - exact)
error2 = np.abs(formula2(n) - exact)

# curve fit to get n
def f(n, K, p):
    return K * 1 / n**p

popt1, pcov1 = curve_fit(f, n, error1)
popt2, pcov2 = curve_fit(f, n, error2)

print('Format: [K, p]')
print('popt1 = ' + str(popt1))
print('popt2 = ' + str(popt2))

fit_err1 = np.diag(np.sqrt(np.abs(pcov1)))
fit_err2 = np.diag(np.sqrt(np.abs(pcov2)))

print('fit_err1 = ' + str(fit_err1))
print('fit_err2 = ' + str(fit_err2))

# plotting
f = np.vectorize(f)

plt.scatter(n, error1, label='Absolute Error Formula 1',
        marker='+')
plt.scatter(n, error2, label='Abosulte Error Formula 2',
        marker='+')

plt.plot(n, f(n, popt1[0], popt1[1]), label=f'Fit function Error 1, p={popt1[1]}')
plt.plot(n, f(n, popt2[0], popt2[1]), label=f'Fit function Error 2, p={popt2[1]}')

plt.legend()

plt.yscale('log')
plt.xlabel('$n$')

plt.savefig('build/Ex2.pdf')
