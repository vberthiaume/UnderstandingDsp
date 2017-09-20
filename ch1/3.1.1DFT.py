import numpy as np
import matplotlib.pyplot as plt

def plotStem(axarr, x, y, title):
    markerline, stemlines, baseline = axarr.stem(x, y, '-.')
    axarr.set_xlim([min(x)-1,max(x)+1])
    axarr.set_ylim([min(y)-1,max(y)+1])
    axarr.set_title(title)

def DFT(xn, N):
    Xm = []
    for m in np.arange(N):
        xm = 0
        for n in np.arange(N):
            xm += xn[n]*np.cos(2*np.pi*n*m/N) - 1j*xn[n]*np.sin(2*np.pi*n*m/N)    
        Xm.append(xm)
        
    return Xm

#fo = 1300
#fs = 8000
#N = 8
#n = np.arange(N)
#xn = np.sin(2*np.pi*fo*n/fs) + .5*np.sin(2*np.pi*2*fo*n/fs + 3*np.pi/4)

#xn = 2*np.cos(2*np.pi*3*1500*n/4000 + np.pi/4)
#xn = [9,9,9,9,9,9,9,9]
#xn = [1,0,0,0,0,0,0,0]
#xn = [0,1,0,0,0,0,0,0]

#define xn
fs = 8000
N = 8

Ao = 2
k = 3
fo = k*fs/N
phi = 0 #np.pi/4

n = np.arange(N)
xn = Ao * np.cos( 2*np.pi * fo * n/fs + phi )

#do DFT
Xn = DFT(xn, N)
XnMag = np.absolute(Xn)
XnPhase = [np.arctan(np.imag(x) / np.real(x)) for x in Xn]

#print stuff
print "x(n):"
print xn

print "\nX(n)"
for x in Xn:
    print('{:.4f}'.format(x))

#plot stuff
fig, axarr = plt.subplots(3, sharex=False)
plotStem(axarr[0], n, xn, "x(n)")
plotStem(axarr[1], n, XnMag, "|X(n)|")
plotStem(axarr[2], n, XnPhase, "phase X(n)")

plt.tight_layout()
plt.show()