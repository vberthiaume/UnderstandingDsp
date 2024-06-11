import numpy as np
import matplotlib.pyplot as plt

#clear the terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float) #after this each element is the sum of all elements before that index
    ret[n:] = ret[n:] - ret[:-n]    #starting at index n, substract the value that is at position n before the end?
    return ret / n                  #divide the whole thing by n. ret[::] also works to select the whole array

n = np.arange(8)
x = [0, 0, 0, 1, 0, 0, 0, 0]
y = moving_average (x)

# set print options to only print 2 decimals
np.set_printoptions (formatter={'float': lambda x: "{0:0.2f}".format(x)})
print (x)
print (y)

plt.stem(n, x, 'b-.')
plt.stem(n, y, 'r-.')

plt.show()