# take data from the Cpp code and plot it

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Cpp/rand_pts.txt", names='AB')

xvals = df['A'].values
yvals = df['B'].values

plt.plot(xvals, yvals)
plt.show()
