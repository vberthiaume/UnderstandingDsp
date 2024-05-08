import numpy as np
import matplotlib.pyplot as plt

# these are constants that just need to be set for a given problem
fo = 2                  # fo is the frequency of my signal, the sine wave, in Hz. So my signal has fo cycles per second. This doesn't actually change anything to the plot because of the nature of it
numPointsPerCycle = 32  # how many sample points in one cycle of the signal
numCycles = 3           # how many repetitions of the signal do i want to plot

#these result from the constants above
to = 1/fo                   # the period of my signal, ie, the time it takes to do one cycle, is the inverse of fo
ts = to / numPointsPerCycle # the time period between samples is the period of the signal (so the time for 1 cycle) divided by the number of points in one cycle
fs = 1/ts                   # the sampling frequency, or how many times per second am I sampling the signal, is the inverse of the sampling period

# make an array for n, which are the time points shown on the x axis
numPoints = numCycles * numPointsPerCycle
n = np.arange (numPoints)
# print (n)

x = np.sin (2*np.pi * fo * n * ts)

# doc for plot, esp the string arg: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
plt.plot (n, x, '.')
plt.xlabel ('n')
plt.ylabel ('x')
plt.show()