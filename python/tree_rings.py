# makes circles that expand by same amount of area each time
#
# Henry Peterson 8/2/15, 1-6-17

import matplotlib.pyplot as plt
import numpy as np

#dots = int(input("How many dots? "))
#yrs = int(input("How many years? "))
#area = float(input("Area change? "))
dots = 1000
yrs = 25
area = 1
rads = 2 * np.pi / dots
xvals = np.zeros(dots * yrs)
yvals = np.zeros(dots * yrs)
radius = 0

for yr in range(yrs):
    current_area = np.pi * radius**2
    radius = np.sqrt( (current_area + area) / np.pi )
    for dot in range(dots):
        xvals[dot + yr * dots] = radius * np.cos(rads * dot)
        yvals[dot + yr * dots] = radius * np.sin(rads * dot)
        
plt.plot(xvals, yvals, "r.", markersize=0.5)
plt.show()