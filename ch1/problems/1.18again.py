import numpy as np
import matplotlib.pyplot as plt

# basic params
numPoints = 16
numPoints2 = numPoints/2
numCycles = 4
n = np.arange (numPoints)
n2 = np.arange (numPoints2)

# OG signals
x = np.cos (2 * np.pi * n * numCycles/numPoints)
x2 = np.cos (2 * np.pi * n2 * numCycles/numPoints)
y = x[::2]

# shifted signals
xshift = np.cos (2 * np.pi * (n+1) * numCycles/numPoints)
xshift2 = np.cos (2 * np.pi * (n2+1) * numCycles/numPoints)
yshift = xshift[::2]

# display the thing
fig, axarr = plt.subplots(4, sharex=False)
axarr[0].plot(n[:8], x[:8], '.')
axarr[0].set_title('x')
    
axarr[1].plot(n2, y, '.')
axarr[1].set_title('y')

axarr[2].plot(n2, xshift2, '.')
axarr[2].set_title('xshift')
    
axarr[3].plot(n2, yshift, '.')
axarr[3].set_title('yshift')
axarr[3].set_ylim([-1, 1])
plt.show()