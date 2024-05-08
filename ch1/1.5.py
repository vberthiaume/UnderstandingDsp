import numpy as np
import matplotlib.pyplot as plt

# make an array for n, which are the time points shown on the x axis
numCycles = 3                               #how many repetitions of the signal below
numPointsPerCycle = 32                      #how many sample points in one cycle of the signal
numPoints = numCycles * numPointsPerCycle
n = np.arange (numPoints)
# print (n)

f = 2                       # f is the frequency of my signal
ts = 1 / numPointsPerCycle  # time period in seconds between samples

x = np.sin (2*np.pi * f * n * ts)

# doc for plot, esp the string arg: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
plt.plot (n, x, '.')
plt.xlabel ('n')
plt.ylabel ('x')
plt.show()