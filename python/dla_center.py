# display data from cpp code
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Cpp/dla_grid.txt")
A = df.values

plt.imshow(A, cmap=plt.get_cmap("Greens"))
plt.show()
