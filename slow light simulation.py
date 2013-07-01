import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import csv

# Linear sizes of the modelling area
RESOLUTION_X = 1000
RESOLUTION_Y = 1000
LENGTH = 10.  # in cm
WIDTH = 10.  # in cm

def y2j(y):
    if np.abs(j+80) <= center:
        return np.floor(y/(dy))
    else:
        return 480

dx = LENGTH/ float(RESOLUTION_X)
center = RESOLUTION_Y/2
dy = WIDTH/ float(center)

xgrid = np.linspace(0., LENGTH, RESOLUTION_X)
y = 4.*np.ones(RESOLUTION_X)
yp = -0.3*np.ones(RESOLUTION_X) # y prime
resolution = (RESOLUTION_X,RESOLUTION_Y)
n = np.ones(resolution) # refractive index distribution

for i in range(200):
    n[540 + i] *= 1.5

log_dndx = open('slow_light/log_dndx.txt','wb')
dndx = np.zeros(resolution)
for i, row in enumerate(dndx[:-1]):
    for j, _ in enumerate(row[:-1]):
        dndx[i,j] = (n[i+1,j] - n[i,j])/dx
        if dndx[i,j]:
            log_dndx.write('['+str(i)+','+str(j)+']=' + str(dndx[i,j])+'\n')

log_rhs = open('slow_light/log_rhs.txt','wb')
for i, x in enumerate(xgrid[1:]):
    rhs = -1.*(1 + yp[i]**2)*yp[i]*dndx[i,y2j(y[i])]/n[i+1,y2j(y[i])]
    if rhs:
        log_rhs.write('['+str(i)+']=' + str(rhs)+'\n')
    yp[i+1] = yp[i] + rhs * dx
    y[i+1] = y[i] + yp[i] * dx




screen = 0.2*n

for i, x in enumerate(xgrid):
    j = np.floor(y[i]/(dy))
    if np.abs(j+80) <= center:
        for r in range(80):
            screen[i, center + j + r] = 0.5

plt.imshow(screen,interpolation='nearest')
plt.savefig('slow_light/1.png')
plt.clf()
plt.imshow(dndx,interpolation='nearest')
plt.savefig('slow_light/1dndx.png')
