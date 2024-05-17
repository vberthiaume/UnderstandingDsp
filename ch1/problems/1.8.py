import numpy as np
import matplotlib.pyplot as plt

# get an input sinusoid
nMax = 8           
n = np.arange (nMax)

#1.8
x = np.cos (2 * np.pi * 2 * n/nMax)   
# xshift = [np.cos(2*np.pi*2*x/nMax) for x in n+1]    #this works because arrays are circular here. so n[8] is actually n[0]
xshift = np.cos ( 2 * np.pi * 2 * (n+1)/nMax)   


# display the thing
fig, axarr = plt.subplots(2, sharex=False)
if True :
    # fig, axarr = plt.subplots(2, sharex=False)

    axarr[0].plot(n, x)
    axarr[0].set_title('x')
        
    axarr[1].plot(n, xshift)
    axarr[1].set_title('xshift')
else :
    markerline, stemlines, baseline = axarr[0].stem(n, x, '-.')
    axarr[0].set_xlim([-1,8])
    axarr[0].set_ylim([-1.5,1.5])

    markerline, stemlines, baseline = axarr[1].stem(n, xshift, '-.')
    axarr[1].set_xlim([-1,8])
    axarr[1].set_ylim([-1.5,1.5])

plt.show()