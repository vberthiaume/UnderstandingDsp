import numpy as np
from scipy.ndimage import shift

a, b, delay = 3, 5, 1

x1 = np.arange (10) * a
x1delay = shift (x1, delay, cval=0) * b
y1 = x1 + x1delay

x2 = np.arange (10)
x2delay = shift (x2, delay, cval=0) * b
y2 = a * (x2 + x2delay)

print (y1)
print (y2)
