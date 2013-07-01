import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import csv
import slowlight.nsetup as nsetup
import slowlight.grid as grid

SIGMA = 100
RAYS_NUMBER = 10


def finite_diff(a,i):
    if i>4 and i<grid.RESOLUTION_X-5:
        return -1.*(a[i+4] - a[i-4])/280. + (a[i+3] - a[i-3])*4./105. - (a[i+2] - a[i-2])/5. + (a[i+1] - a[i-1]) * 4./5.
    else:
        return 0.


resolution = (grid.RESOLUTION_X,grid.RESOLUTION_Y)
n = nsetup.nsetup(resolution, 'parameters') # refractive index distribution

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



# simulation stuff

xgrid = np.linspace(0., grid.LENGTH, grid.RESOLUTION_X)

def ray(start, direction):
    y = start*np.ones(grid.RESOLUTION_X)
    yp = +direction*np.ones(grid.RESOLUTION_X) # y prime
    for i, x in enumerate(xgrid[1:]):
        rhs1 = -1.*(1 + yp[i]**2)*yp[i]*dndx[i,grid.y2j(y[i])] / n[i+1,grid.y2j(y[i])]
        rhs2 = (1 + yp[i]**2)**2 * dndy[i,grid.y2j(y[i])] / n[i,grid.y2j(y[i])]
        yp[i+1] = yp[i] + (rhs1 + rhs2) * grid.dx
        y[i+1] = y[i] + yp[i] * grid.dx
    return y, yp

y, yp = ray(1.,0.2)


# visualizing results

for i,x in enumerate(xgrid[:-SIGMA]):
    screen = 0.2*n
    for k in range(80):
        for r in range(30):
            screen[i+k, grid.y2j(y[i+k]) + r] = 2.
    plt.imshow(screen,interpolation='nearest')
    plt.savefig('slowlight/video2/'+str(i)+'.png')
    plt.clf()


plt.imshow(dndx,interpolation='nearest')
plt.savefig('slowlight/1dndx.png')
plt.clf()
plt.imshow(dndy,interpolation='nearest')
plt.savefig('slowlight/1dndy.png')
plt.clf()
