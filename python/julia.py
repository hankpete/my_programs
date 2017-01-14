# Show the beautiful Julia Set!
#1-8-17

###messing with imshow
#import matplotlib.pyplot as plt
#import numpy as np
#
#grid = np.zeros( (10,10) )
#
#grid[1:5,5:9] = 1
#
#fig, ax = plt.subplots()
#
#ax.imshow(grid, extent= [0,1,0,1]) 
#
#plt.show()

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

#read file cpp code makes
df = pd.read_csv("../Cpp/julia_data.txt")
A = df.values

#show its data
plt.imshow(A, cmap=plt.get_cmap("hot"))
plt.show()
    
