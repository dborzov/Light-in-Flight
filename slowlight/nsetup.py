import numpy as np
import grid


def nsetup(resolution,description):
    n = np.ones(resolution) # refractive index distribution
    if description == 'straight':
        for i in range(200):
            n[540 + i] *= 1.5
    if description == 'skewed':
        slope = 0.4
        b = 4.
        for i,row in enumerate(n):
            for j,_ in enumerate(row):
                x = grid.i2x(i)
                y = grid.j2y(j)
                if x < 5. - slope * y and x > 3. - slope* y:
                    n[i,j] = 1.5
    if description == 'parameters':
        slope = -2.
        b = 4.
        norm = np.sqrt(1 + slope**2)
        for i,row in enumerate(n):
            for j,_ in enumerate(row):
                x = grid.i2x(i)
                y = grid.j2y(j)
                rx = x -b
                dist = np.abs(- rx * slope + y)/norm
                if dist < 1.:
                    if dist >0.5:
                        n[i,j] = 1.+0.75/(1. + dist)
                    else:
                        n[i,j] = 1.5

    if description == 'U':
        center_x = 2.
        dilation = 0.25
        center_y = -0.
        radius = 3.0
        thickness = 2.
        for i,row in enumerate(n):
            for j,_ in enumerate(row):
                x = grid.i2x(i)
                y = grid.j2y(j)
                if x > center_x-1.:
                    dist = np.sqrt(dilation*(x - center_x)**2 + (y - center_y)**2)
                    if dist < radius:
                        if dist > 2. * thickness - radius:
                            n[i,j] = 1.+0.5*np.cos((dist - thickness)*np.pi/(2.*(radius - thickness)))
                        else:
                            pass

    return n
