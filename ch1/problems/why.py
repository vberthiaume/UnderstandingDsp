import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import shift

useShift = True

# set up our basic variables
num = 10
n = np.arange (num)
x = np.zeros (num)
x[0] = 1

# (b) an integrator: y(n) = x(n) + y(n–1),
y1 = x
if useShift:
    y1 += shift (y1, 1)
else:
    for i in n:
        y1[i] += y1[i-1]

# (c) a leaky integrator: y(n) = Ax(n) + (1–A)y(n–1) [the scalar value A is a real-valued constant in the range 0 <A<1],
A = .5
y2 = A * x
y2 += (1-A) * shift (y2, 1)

# plot things
fig, axarr = plt.subplots (2, sharex=True)

axarr[0].plot(n, y1, '.')
axarr[0].set_title('y1')
axarr[1].plot(n, y2, '.')
axarr[1].set_title('y2')

plt.tight_layout()
plt.show()
