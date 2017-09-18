import numpy as np


def DFT(xn, N, m):
    #arrays = [xn*np.cos(2*np.pi*n*m/N) - 1j*xn*np.sin(2*np.pi*n*m/N) for n in np.arange(N)]
    #return np.sum(arrays, 1)
    Xm = []
    for n in np.arange(N):
        Xm.append(xn[n]*np.cos(2*np.pi*n*m/N) - 1j*xn[n]*np.sin(2*np.pi*n*m/N))
        
    return np.sum(Xm, 0)


fo = 1000
fs = 8000
N = 8
n = np.arange(N)

xn = np.sin(2*np.pi*fo*n/fs) + .5*np.sin(2*np.pi*2*fo*n/fs + 3*np.pi/4)

print "xn:"
print xn

print "DFT(xn, N, 1):"
print DFT(xn, N, 1)