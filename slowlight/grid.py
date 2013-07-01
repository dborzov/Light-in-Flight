"""
The grid. A digital frontier. I try to picture bits of information traveling throught the wires. What do they look like? Motocycles?
"""
import numpy as np


# Linear sizes of the modelling area
RESOLUTION_X = 1000
RESOLUTION_Y = 1000
LENGTH = 10.  # in cm
WIDTH = 10.  # in cm


dx = LENGTH/ float(RESOLUTION_X)
center = RESOLUTION_Y/2
dy = WIDTH/ float(RESOLUTION_Y)

def y2j(y):
    j = center + np.floor(y/(dy))
    if j>=0 and j+80 <= RESOLUTION_Y:
        return j
    else:
        print 'y2j getting out of range'
        return 480

i2x = lambda i:i*dx
j2y = lambda j:(j)*dy - center*dy


