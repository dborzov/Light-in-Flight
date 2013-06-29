"""
Video
-----------------
A script that makes an array of png files from the csv data

Dima Borzov, 2013
"""

import handler

for i in range(1,444):
    handler.csv2png(str(i))
