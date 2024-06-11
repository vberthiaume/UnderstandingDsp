import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-np.pi/2, np.pi/2, .2)
y = np.sin(x)

plt.stem(x, y, 'b-.')
plt.stem(x, x, 'r-.')

plt.show()