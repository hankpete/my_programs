# makes circles that expand by same amount of area each time
#
# Henry Peterson 8/2/15

print "Importing libraries....."
import matplotlib.pyplot as plt
import numpy as np

n = int(raw_input("How many dots? "))
i = int(raw_input("\nHow many cycles? "))
a = float(raw_input("\nArea change? "))
rads = 2*np.pi / n
xvals = [0] * n
yvals = [0] * n
r = 0

for cycle in range(i):
    current_a = np.pi * r**2
    r = np.sqrt((current_a + a) / np.pi)
    for dot in range(n):
        xvals.append(r * np.cos(rads * dot))
        yvals.append(r * np.sin(rads * dot))

plt.plot(xvals, yvals, "r-")
plt.show()
