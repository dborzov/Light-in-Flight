import numpy as np
import grid

def nsetup(resolution,description):
    n = np.ones(resolution) # refractive index distribution
    if description == 'straight':
        for i in range(200):
            n[540 + i] *= 1.5
    if description == 'skewed':
        for i,row in enumerate(n):
            for j,_ in enumerate(row):
                x = grid.i2x(i)
                y = grid.j2y(j)
                if x < 5. - 0.2* y and x > 3. - 0.2* y:
                    n[i,j] = 1.5

    return n
