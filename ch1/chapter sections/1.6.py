import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import shift

#basic stuff
fo = 1
numPointsPerCycle = 32
numCycles = 1

#these result from the constants above
ts = 1 / (fo * numPointsPerCycle)

# make an array for n, which are the time points shown on the x axis
numPoints = numCycles * numPointsPerCycle
n = np.arange (numPoints)

#basic signals
x = np.sin (2*np.pi * fo * n * ts)
y = - x/2

# xprime = np.right_shift (x, 4)
xprime = shift (x, 4, cval=0)
yprime = - xprime/2

# display the thing
fig, axarr = plt.subplots(4, sharex=False)

axarr[0].plot(n, x, '.')
axarr[0].set_title('x')

axarr[1].plot(n, y, '.')
axarr[1].set_title('y')

axarr[2].plot(n, xprime)
axarr[2].set_title('xprime')

axarr[3].plot(n, yprime, '.')
axarr[3].set_title('yprime')

plt.show()
