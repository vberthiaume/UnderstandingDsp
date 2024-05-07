import numpy as np
import matplotlib.pyplot as plt

# make an array for n that goes from 0 to 31
numCycles = 2

numPoints = 32
n = np.arange(numPoints)
# print (n)

# the equation I'm trying to plot is this one 
# x(n) = sin (2 * pi * f * n * ts)
# where f is the frequency of the sine wave
# and ts is the sampling period in seconds, that is how much time between samples,
# which is the inverse of the sampling frequency fs: fs = 1/ts
# here we have 32 samples per cycle, which means
# hertz are cycles per seconds

# x1 = np.sin (np.pi*n)
#NOW HERE NEED TO UNDERSTAND THE RELATIONSHIP BETWEEN N, F, FS, TS EVERYTING LOL
f = 2
fs = 32 #sampling frequency, ie how many samples for one cycle
ts = 1/fs

x = np.sin (2 * np.pi * f * n * ts)


# doc for plot: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
# 'bo' here is b for blue and o for circle. See the notes section
plt.plot (n, x, 'o')
plt.xlabel ('n')
plt.ylabel ('x')
plt.show()