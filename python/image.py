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

import matplotlib.pyplot as plt
import numpy as np

f = open("/home/hpeter/gits/my_programs/C++/A_julia.txt", 'r')

lines = f.readlines()
Nx = len( lines[0] )
Ny = len( lines ) 
A = np.zeros( (Ny, Nx) )


i = 0
for line in lines:
    j = 0
    for element in line:
        if element == '1':
            A[i][j] = 1
            j += 1
        elif element == '0':
            j += 1
    i += 1
f.close()


plt.imshow(A)
plt.show()
    
