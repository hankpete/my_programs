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

import matplotlib.pyplot as plt
import numpy as np

#read file cpp code makes
f = open("../Cpp/A_julia.txt", 'r')

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

#show its data
plt.imshow(A, cmap=plt.get_cmap("hot"))
plt.show()
    
