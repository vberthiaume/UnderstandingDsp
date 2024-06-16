import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import shift

#21: 
# Draw the unit impulse responses (the output sequences when the input is a
# unit sample impulse applied at time n=0) of the four processes listed
# in Problem 1.20. Let A = 0.5 for the leaky integrator. Assume that all sample values
# within the systems are zero at time n = 0

#22:
# the same, but x is a step function which is just ones. Another definition for the step
# function is that it is the cumulative sum of unit impulse responses. Not sure how that
# is more useful yet

#if do22 is false we're doing 21 :thinkaboutit:
do22 = True

# set up our basic variables
num = 10
n = np.arange (num)
if do22:
    x = np.ones (num)
else:
    x = np.zeros (num)
    x[0] = 1

y = np.zeros (num)

# (a) a 4th-order comb filter: y(n) = x(n) – x(n–4),
ya = x.copy() - shift (x, 4)

# (b) an integrator: y(n) = x(n) + y(n–1),
yb = x.copy()
for i in n:
    yb[i] += yb[i-1]

# (c) a leaky integrator: y(n) = Ax(n) + (1–A)y(n–1) [the scalar value A is a real-valued constant in the range 0 <A<1],
A = .5
yc = A * x.copy()
for i in n:
    yc[i] += (1-A) * yc[i-1]

# (d) a differentiator: y(n) = 0.5x(n) – 0.5x(n-2)
yd = (.5 * x.copy()) - (.5 * shift (x, 2))

# plot everything
fig, axarr = plt.subplots (4, sharex=True)

axarr[0].plot(n, ya, '.')
axarr[0].set_title('ya')

axarr[1].plot(n, yb, '.')
axarr[1].set_title('yb')

axarr[2].plot(n, yc, '.')
axarr[2].set_title('yc')

axarr[3].plot(n, yd, '.')
axarr[3].set_title('yd')

plt.tight_layout()
plt.show()
