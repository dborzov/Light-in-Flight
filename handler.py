"""
Handler
-----------------
Contains functions to manipulate ground truth data

Dima Borzov, 2013
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import csv


def csv2png(filename):
    afile = open('csv/'+filename+'.csv', "rb")
    reader = list(csv.reader(afile))
    resolution = (len(reader),len(reader[0]))
    screen = np.zeros(resolution)
    for i, row in enumerate(reader):
        for j, element in enumerate(row):
            screen[i,j] = float(element)
    plt.imshow(screen,interpolation='nearest')
    plt.savefig('video/'+filename+'.png')
    plt.clf()

    print '-------------------'
    print 'Filename: ', filename
    print 'File resolution:', resolution[0], 'x', resolution[1]
