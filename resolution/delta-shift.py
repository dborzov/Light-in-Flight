"""
Calibration matrix simulation within the delta function approximation.
-----------
Dima Borzov, 2013
"""


import numpy as np
import matplotlib.pyplot as plt


def c(f, d):
    T = 1e-6 / f
    if d % T > T/2.:
        return +10.
    else:
        return -10.

delay_list = np.arange(0., 60e-9, 1.849536e-10)
f_list = np.arange(10., 120., 5.)
#X, Y = np.meshgrid(delay_list, f_list)
C = np.zeros((len(f_list),len(delay_list)))

for i, row in enumerate(C):
    for j, element in enumerate(row):
        C[i,j] = c(f_list[i], delay_list[j])

plt.contourf(delay_list,f_list,C)
plt.gca().invert_yaxis()
cond_number = np.floor(np.linalg.cond(C))
plt.title('Delta function correlation coefficients, cond = ' +
    str(cond_number))
plt.xlabel('Delay, ns')
plt.ylabel('Modulation frequency')
plt.savefig('delta-shift.png')
plt.clf()
