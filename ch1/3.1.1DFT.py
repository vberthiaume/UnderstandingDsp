import numpy as np


def DFT(xn, N):
    #arrays = [xn*np.cos(2*np.pi*n*m/N) - 1j*xn*np.sin(2*np.pi*n*m/N) for n in np.arange(N)]
    #return np.sum(arrays, 1)
    Xm = []
    for m in np.arange(N):
        xm = 0
        for n in np.arange(N):
            xm += xn[n]*np.cos(2*np.pi*n*m/N) - 1j*xn[n]*np.sin(2*np.pi*n*m/N)    
        Xm.append(xm)
        
    return Xm


fo = 1000
fs = 8000
N = 8
n = np.arange(N)

xn = np.sin(2*np.pi*fo*n/fs) + .5*np.sin(2*np.pi*2*fo*n/fs + 3*np.pi/4)

print "xn:"
print xn

Xn = DFT(xn, N)
for xn in Xn:
    print('{:.4f}'.format(xn))