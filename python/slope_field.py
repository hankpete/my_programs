# python program to plot slope fields

import numpy as np
import matplotlib.pyplot as plt

# some constants 
MIN = -5
MAX = 5
NUM = 30

# define some useful functions
# def F(x, y):
#         # dy/dx = F(x, y)
#         return (np.sqrt(np.abs(x))+ y/2)
F = lambda x,y: np.sin(x*y)

def get_y_line(x, y1, x1, m):
        # y - y1 = m(x - x1)
        return ( m*(x - x1) + y1 )

# define vals for dots we want to use
xvals = np.linspace(MIN, MAX, NUM)
yvals = np.linspace(MIN, MAX, NUM)

# length of half of each line
d = .1

# loop for each dot

for x in xvals:
        for y in yvals:
                # plot the dot
                # plt.plot(x, y, "g.")    # green dot

                # calculate stuff for slope line
                m = F(x, y)

                # fancy trig to get how far to go to have half of line = d
                #xdist = d*np.cos(np.arctan(m))
                #yval_right = get_y_line((x + xdist), y, x, m)
                #yval_left = get_y_line((x - xdist), y, x, m)
                #plt.plot([x-xdist, x+xdist], [yval_left, yval_right], "b-")

                # or use vectors!
                u = np.zeros(2)
                u[0] = 1; u[1] = m
                u /= np.sqrt(1 + m**2)
                u *= d/2
                plt.plot([x-u[0], x+u[0]], [y-u[1], y+u[1]], "b-") 


# optionally plot a solution
#xs = np.linspace(MIN, MAX, 1000)
#plt.plot(xs, np.e**xs, "r-")

plt.xlim([MIN - 1, MAX + 1])
plt.ylim([MIN - 1, MAX + 1]) 
plt.show()


