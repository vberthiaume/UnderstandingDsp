import numpy as np
import matplotlib.pyplot as plt

# make an array for n
numCycles = 3
numPointsPerCycle = 32
numPoints = numCycles * numPointsPerCycle
n = np.arange(numPoints)
# print (n)

# the equation I'm trying to plot is this one 
# x(n) = sin (2 * pi * f * n * ts)

# and ts is the sampling period in seconds, that is how much time between samples,
# which is the inverse of the sampling frequency fs: fs = 1/ts
# here we have 32 samples per cycle, which means
# hertz are cycles per seconds

f = 2   # f is the frequency of the sine wave
ts = 1 / numPointsPerCycle  # time period between samples

x = np.sin (2*np.pi * f * n * ts)

# doc for plot: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
# 'bo' here is b for blue and o for circle. See the notes section
plt.plot (n, x, 'o')
plt.xlabel ('n')
plt.ylabel ('x')
plt.show()