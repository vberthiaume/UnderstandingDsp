import numpy as np
import matplotlib.pyplot as plt


n = np.arange (8)
print (n)
x = np.sin (2*np.pi * n)
print (x)
y = np.sin (2*np.pi * 2*n)

#shifted signals
xshift = np.sin (2*np.pi * (n+1))
yshift = np.sin (2*np.pi * 2*(n+1))

# display the thing
fig, axarr = plt.subplots(4, sharex=False)

axarr[0].plot(n, x, '.')
axarr[0].set_title('x')

axarr[1].plot(n, y, '.')
axarr[1].set_title('y')

axarr[2].plot(n, xshift, '.')
axarr[2].set_title('xshift')

axarr[3].plot(n, yshift, '.')
axarr[3].set_title('yshift')

plt.show()
