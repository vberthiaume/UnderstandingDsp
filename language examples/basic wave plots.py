
import numpy as np
import matplotlib.pyplot as plt

n = np.arange (0, 2*np.pi, 0.1)

x1 = np.sin (n)
x2 = np.cos (n)

# Plotting Sine Graph
plt.plot (n, x1, color='green')
plt.plot (n, x2, color='darkblue')
plt.show()