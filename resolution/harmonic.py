import numpy as np
import matplotlib.pyplot as plt

def component(m):
    flips = [x/float(m) + 1./float(2.*m) for x in range(m)]
    flips.append(1.)
    return flips

def l2(interval,m):
    sign = (-1.)**len([x for x in component(m) if interval[0] >= x])
    inside = [x for x in component(m) if interval[0] < x and interval[1] > x]
    array = [interval[0]] + inside  + [interval[1]]
    l2 = sign * sum([(-1)**i*(array[i+1]-x) for i,x in enumerate(array[:-1])])
    return l2

INTERVAL = [0.07,0.3]
fourier = [l2(INTERVAL,n) for n in range(1,100)]
norma = np.abs(fourier[0])
significant = [i for i,x in enumerate(fourier) if np.abs(x) > 0.05*norma]
threshold = max(significant)
print threshold

xx = [x for x, _ in enumerate(fourier)]
print fourier
plt.axhline(0, color='black', lw=2)
plt.vlines(xx,[0],fourier)
plt.vlines(threshold,-norma,norma,color='r')
plt.savefig('fourier.png')
plt.clf()
