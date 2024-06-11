import numpy as np
import matplotlib.pyplot as plt

# get an input sinusoid
nMax = 10
n = np.arange(nMax)

#1.6
x1 = np.cos(np.pi*n)
x2 = np.cos((np.pi*n)/2)
x3 = [np.cos(0) for x in n]

#1.7
# x1 = [0 if abs(np.sin(np.pi*x)) < 1e-5 else np.sin(np.pi*x) for x in n]
# x2 = np.sin((np.pi*n)/2)   
# x3 = [np.sin(0) for x in n]

# display the thing
fig, axarr = plt.subplots(3, sharex=False)

axarr[0].plot(n, x1)
axarr[0].set_title('x1')

axarr[1].plot(n, x2)
axarr[1].set_title('x2')

axarr[2].plot(n, x3)
axarr[2].set_title('x3')

plt.show()