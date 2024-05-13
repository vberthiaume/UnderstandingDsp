import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

#basic stuff
fo = 1
numPointsPerCycle = 32
numCycles = 3

#these result from the constants above
ts = 1 / (fo * numPointsPerCycle)

# make an array for n, which are the time points shown on the x axis
numPoints = numCycles * numPointsPerCycle
n = np.arange (numPoints)

#basic signals
x1 = np.sin (2*np.pi * fo * n * ts)
x2 = np.sin (2*np.pi * 3 * n * ts)
y = np.square (np.abs(x1 + x2))

#fft -- this isn't quite right but I have no idea what I'm doing. Get back to this!
yf = scipy.fftpack.fft (y)
yf = 1/numPoints * yf[:numPoints//2]
xf = np.linspace (0.0, 1.0/(2.0*ts), numPoints//2)

# display the thing
fig, axarr = plt.subplots(4, sharex=False)

axarr[0].plot(n, x1, '.')
axarr[0].set_title('x1')

axarr[1].plot(n, x2, '.')
axarr[1].set_title('x2')

axarr[2].plot(n, y)
axarr[2].set_title('y')

axarr[3].plot(xf, yf, '.')
axarr[3].set_title('y fft')

plt.show()
