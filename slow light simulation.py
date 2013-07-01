import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import csv
import slowlight.nsetup as nsetup
import slowlight.grid as grid

def finite_diff(a,i):
    if i>4 and i<grid.RESOLUTION_X-5:
        return -1.*(a[i+4] - a[i-4])/280. + (a[i+3] - a[i-3])*4./105. - (a[i+2] - a[i-2])/5. + (a[i+1] - a[i-1]) * 4./5.
    else:
        return 0.

xgrid = np.linspace(0., grid.LENGTH, grid.RESOLUTION_X)
y = -1.*np.ones(grid.RESOLUTION_X)
yp = +0.7*np.ones(grid.RESOLUTION_X) # y prime
resolution = (grid.RESOLUTION_X,grid.RESOLUTION_Y)
n = nsetup.nsetup(resolution, 'straight') # refractive index distribution


log_dndx = open('slowlight/log_dndx.txt','wb')
dndx = np.zeros(resolution)
for i, row in enumerate(dndx[:-1]):
    for j, _ in enumerate(row[:-1]):
        dndx[i,j] = finite_diff(n[:,j], i)/grid.dx
        if dndx[i,j]:
            log_dndx.write('['+str(i)+','+str(j)+']=' + str(dndx[i,j])+'\n')

log_dndy = open('slowlight/log_dndy.txt','wb')
dndy = np.zeros(resolution)
for i, row in enumerate(dndy[:-1]):
    for j, _ in enumerate(row[:-1]):
        dndy[i,j] = finite_diff(n[i,:], j)/grid.dy
        if dndy[i,j]:
            log_dndy.write('['+str(i)+','+str(j)+']=' + str(dndy[i,j])+'\n')


log_rhs = open('slowlight/log_rhs.txt','wb')
log_rhs2 = open('slowlight/log_rhs2.txt','wb')
for i, x in enumerate(xgrid[1:]):
    rhs1 = -1.*(1 + yp[i]**2)*yp[i]*dndx[i,grid.y2j(y[i])] / n[i+1,grid.y2j(y[i])]
    rhs2 = (1 + yp[i]**2)**2 * dndy[i,grid.y2j(y[i])] / n[i,grid.y2j(y[i])]
    if rhs1:
        log_rhs.write('['+str(i)+']=' + str(rhs1)+'\n')

    if rhs2:
        log_rhs2.write('['+str(i)+']=' + str(rhs2)+'\n')

    yp[i+1] = yp[i] + (rhs1 + rhs2) * grid.dx
    y[i+1] = y[i] + yp[i] * grid.dx




screen = 0.2*n

for i, x in enumerate(xgrid):
    j = np.floor(y[i]/(grid.dy))
    if np.abs(j+80) <= grid.center:
        for r in range(30):
            screen[i, grid.center + j + r] = 0.5

plt.imshow(screen,interpolation='nearest')
plt.savefig('slowlight/1.png')
plt.clf()
plt.imshow(dndx,interpolation='nearest')
plt.savefig('slowlight/1dndx.png')
plt.clf()
plt.imshow(dndy,interpolation='nearest')
plt.savefig('slowlight/1dndy.png')
plt.clf()
