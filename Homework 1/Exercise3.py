# Exercise3.py

import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt

def f(x, alpha):
    res = 2 * np.power(1-x, 1 / (1-alpha))
    return res

f = np.vectorize(f)

# parameters
samples = 10000
alpha_true = 5

x = rand(samples,1)

# creating a plot we will only use to create bins and samples
bin_count = 50
n, bins, patches = plt.hist(f(x, alpha_true), bins=bin_count, density=False, label='Occurences in interval')

plt.xlabel('y')
plt.ylabel('n(y)')

plt.xscale('log')
plt.yscale('log')
plt.savefig('build/Ex3-log.pdf')
plt.clf()

# testing if the distribution is correct

# testing powerlaw for occurences and the middle point of each interval
midpoints = np.zeros(bin_count)

for i in range(0, bin_count):
    midpoints[i] = (bins[i] + bins[i+1]) / 2

# same procedure as in Ex 2: testing a power law with a curve fit
from scipy.optimize import curve_fit

def p(x, A, alpha):
    return A * np.power(x, -1 * alpha)

popt, pcov = curve_fit(p, midpoints, n, p0=(n[0],5))
# extracting the parameters and errors
A = popt[0]
alpha = popt[1]
errors = np.sqrt(np.diag(pcov))
alpha_err = errors[1]

print(f'\\alpha = {alpha:.4f} \pm {alpha_err:.4f}')


# now actual plotting
n, bins, patches = plt.hist(f(x, alpha_true), bins=bin_count, density=False, label='Random distribution')

x_plot = np.linspace(2,10)
plt.plot(x_plot, p(x_plot,A,alpha), label=rf'Power law $A \cdot x^{{-\alpha}}$ with $\alpha = {alpha:.3f}$')

plt.legend()

plt.xlabel('y')
plt.ylabel('n(y)')

plt.savefig('build/Ex3.pdf')
