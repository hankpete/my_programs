# compute rectangles in square of dimensions n x n and cubes in a cube of dimensions n x n x n
# output lots of cool data

#print "importing libraries..."
#import matplotlib.pyplot as plt
#import numpy as np

# side length
n = int(raw_input("n = "))

txt = open("coordinates.txt", "a")

# find coordinates (x, y, row, columm) of rectangles in square
rectangles = []
count = 0
for x in range(n):
	for y in range(n):
		max_c = n - x 
		max_r = n - y 
		for c in range(max_c):
			for r in range(max_r):
				possible_rect = str(x) + str(y) + str(r) + str(c)
				if possible_rect not in rectangles:
					rectangles.append(possible_rect)
					count += 1

#print "Rectangles:"
# count = 0
# for rect in rectangles:
# 	print rect
# 	count += 1
# print count
# print (n**2)/4*(n+1)**2

# find coordinates (x, y, z, s) of cubes in a cube
cubes = []
count = 0
for x in range(n):
	for y in range(n):
		for z in range(n):
			points = [x, y, z]
			points.sort()
			max_s = n - points[2] 
			for s in range(max_s):
				possible_cube = str(x) + str(y) + str(z) + str(s)
				if possible_cube not in cubes:
					cubes.append(possible_cube)
					count += 1

txt.write("\n" + str(n) + "x" + str(n) + "\t" + str(n) + "x" + str(n) + "x" + str(n)+ "\n")
for i in range(len(cubes)):
	txt.write(str(rectangles[i]) + "\t" + str(cubes[i]) + "\n")
txt.write("\n")
txt.close()

# print "Cubes:"
# count = 0
# for cube in cubes:
# 	print cube
# 	count += 1
# print count
# print (n**2)/4*(n+1)**2

# convert them to binary code
# binary_rects = []
# for rect in rectangles:
# 	rect = int(rect)
# 	binary_rect = 0
# 	while rect:
# 		exponent = np.floor(np.log10(rect))
# 		part = n**exponent
# 		rect -= 10**exponent
# 		binary_rect += part
# 	binary_rects.append(binary_rect)
# # for rect in binary_rects:
# # 	print rect

# binary_cubes = []
# for cube in cubes:
# 	cube = int(cube)
# 	binary_cube = 0
# 	while cube:
# 		exponent = np.floor(np.log10(cube))
# 		part = n**exponent
# 		cube -= 10**exponent
# 		binary_cube += part
# 	binary_cubes.append(binary_cube)
# # for cube in binary_cubes:
# # 	print cube

# # sort correctly and graph
# binary_rects.sort()
# binary_cubes.sort()

# new_cubes = []
# odd_rects = []
# for rect in binary_rects:
# 	match = False
# 	for cube in binary_cubes:
# 		if cube == rect:
# 			match = True
# 			new_cubes.append(cube)
# 			binary_cubes.remove(cube)
# 	if not match:
# 		odd_rects.append(rect)

# for cube in binary_cubes:
# 	new_cubes.append(cube)
# for rect in odd_rects:
# 	binary_rects.remove(rect)
# 	binary_rects.append(rect)

# for i in range(len(binary_rects)):
# 	print "(" + str(int(binary_rects[i])) + "," + str(int(new_cubes[i])) + ")"
# # for i in new_cubes:
# # 	print i
# # print
# # for i in binary_rects:
# # 	print i

# plt.title("Rectangles and Cubes")
# plt.xlabel("Rectangles")
# plt.ylabel("Cubes")
# plt.plot(binary_rects, new_cubes, "ro")
# plt.plot(range(int(new_cubes[count-1]) + 1), "b-")
# plt.show()

# #clojure