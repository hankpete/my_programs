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

f = open("/home/hpeter/gits/programs/C++/A_julia.txt", 'r')

lines = f.readlines()
# first line of form "N = ..."
string = lines[0]
length = len(string)
N = int( string[4:length] )
A = np.zeros( (N, N) )

i = 0
j = 0
for line in lines:
    if line[0] == 'N':
        continue
    if i == N:
        i = 0
        j += 1
    A[i][j] = int(line)
    i += 1

f.close()


plt.imshow(A)
plt.show()
    
