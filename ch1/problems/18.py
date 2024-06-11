import numpy as np
import matplotlib.pyplot as plt

# basic params
numPoints = 16
numPoints2 = int (numPoints/2)
numCycles = 4
n = np.arange (numPoints)

# OG signals
x = np.cos (2 * np.pi * n * numCycles/numPoints)
y = x[::2]

# shifted signals
xshift = np.cos (2 * np.pi * (n+1) * numCycles/numPoints)
yshift = xshift[::2]

# display the thing
fig, axarr = plt.subplots(4, sharex=False)
axarr[0].stem(n[:numPoints2], x[:numPoints2], '.')
axarr[0].set_title('x')

axarr[1].stem(n[:numPoints2], y, '.')
axarr[1].set_title('y')

axarr[2].stem(n[:numPoints2], xshift[:numPoints2], '.')
axarr[2].set_title('xshift')

axarr[3].stem(n[:numPoints2], yshift, '.')
axarr[3].set_title('yshift')
axarr[3].set_ylim([-1, 1])

plt.tight_layout()
plt.show()
