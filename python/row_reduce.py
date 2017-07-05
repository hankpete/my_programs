# row reduce matrix

import numpy as np

m = np.random.randint(2, 5)
n = np.random.randint(2, 5)
A = np.zeros([m, n])
for i in range(m):
    for j in range(n):
        A[i,j] = np.random.randint(100)
print(A)
current_col = 0
while current_col != n:
    rows = [] 
    for x in range(m):
        rows.append(x)
    r = 0
    while r < m:
        if A[r, current_col] != 0:
            j = 0
            while j < current_col:
                if A[r, j] != 0:
                    break
                else:
                    j += 1
            if j == current_col:
                break    #of form [0 , ...,0, x, ...]
            else:
                r += 1
        else:
            r += 1
    if r == m:    #no pivots in this column
        current_col += 1 
        continue
    rows.remove(r)    #alter all but this row
    A[r, :] = A[r, :] / A[r, current_col] #make it have a 1 at the pivot
    for i in rows:
        if A[i, current_col] != 0:
            A[i, :] = A[i, :] - A[r, :] * A[i, current_col] #row reduce if it's not 0 already
    current_col += 1
print(A)


