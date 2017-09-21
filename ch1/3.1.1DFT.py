import numpy as np
import matplotlib.pyplot as plt

def plotStem(axarr, y, title):
    markerline, stemlines, baseline = axarr.stem(y, '-.')
    axarr.set_xlim([-1,len(y)+1])
    axarr.set_ylim([min(y)-1,max(y)+1])
    axarr.set_title(title)

def DFT(xn):
    Xm = []
    N = len(xn)
    for m in np.arange(N):
        xm = 0
        for n in np.arange(N):
            xm += xn[n]*np.cos(2*np.pi*n*m/N) - 1j*xn[n]*np.sin(2*np.pi*n*m/N)    
        Xm.append(xm)
        
    return Xm


#DEFINE x(n)
###############################################################
#fo = 1000
#fs = 8000
#N = 8
#n = np.arange(N)
#xn = np.sin(2*np.pi*fo*n/fs) + .5*np.sin(2*np.pi*2*fo*n/fs + 3*np.pi/4)
###############################################################
#xn = 2*np.cos(2*np.pi*3*1500*n/4000 + np.pi/4)
#xn = [9,9,9,9,9,9,9,9]
#xn = [1,0,0,0,0,0,0,0]
#xn = [0,1,0,0,0,0,0,0]
###############################################################
fs = 8000
N = 16
NPadded = N
Ao = 1
k = 3
fo = k*fs/N
phi = 0 #np.pi/4
n = np.arange(N)
#n = np.linspace(-N, N, 32)
#noise = 4*np.random.rand(N) - 2

n       = np.pad(n, (0,NPadded-N), 'constant', constant_values=(0))
#noise   = np.pad(noise, (0,NPadded-N), 'constant', constant_values=(0))

xn = Ao * np.sin( 2*np.pi * fo * n/fs + phi ) #+ noise
###############################################################

#do DFT
Xm      = DFT(xn)
XmMag   = np.absolute(Xm)
XmPhase = np.angle(Xm)

#print stuff
print "x(n):", xn
print "\nX(n)"
for x in Xm:
    print('{:.4f}'.format(x))

#plot stuff
fig, axarr = plt.subplots(3, sharex=False)
plotStem(axarr[0], xn, "x(n)")
plotStem(axarr[1], XmMag, "|X(m)|")
plotStem(axarr[2], XmPhase, "phase X(m)")

plt.tight_layout()
plt.show()