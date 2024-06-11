import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import shift

# Draw the unit impulse responses (the output sequences when the input is a
# unit sample impulse applied at time n=0) of the four processes listed
# in Problem 1.20. Let A = 0.5 for the leaky integrator. Assume that all sample values
# within the systems are zero at time n = 0

# set up our basic variables
num = 10
n = np.arange (num)
x = np.zeros (num)
x[0] = 1
y = np.zeros (num)

fig, axarr = plt.subplots (4, sharex=True)

# (a) a 4th-order comb filter: y(n) = x(n) – x(n–4),
ya = x - shift (x, 4)
axarr[0].plot(n, ya, '.')
axarr[0].set_title('ya')

print ("ya: ", ya)

# (b) an integrator: y(n) = x(n) + y(n–1),
yb = x
if True:
    yb += shift (yb, 1)
else:
    for i in n:
        yb[i] += yb[i-1]
axarr[1].plot(n, yb, '.')
axarr[1].set_title('yb')

print ("ya: ", ya)
print ("yb: ", yb)

# (c) a leaky integrator: y(n) = Ax(n) + (1–A)y(n–1) [the scalar value A is a real-valued constant in the range 0 <A<1],
A = .5
yc = A * x
yc += (1-A) * shift (yc, 1)
axarr[2].plot(n, yc, '.')
axarr[2].set_title('yc')

print ("ya: ", ya)
print ("yb: ", yb)
print ("yc: ", yc)

# (d) a differentiator: y(n) = 0.5x(n) – 0.5x(n-2)
yd = (.5 * x) - (.5 * shift (x, 2))
axarr[3].plot(n, yd, '.')
axarr[3].set_title('yd')

print ("ya: ", ya)
print ("yb: ", yb)
print ("yc: ", yc)
print ("yd: ", yd)

plt.tight_layout()
plt.show()
