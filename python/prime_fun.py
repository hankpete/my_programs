# experimenting with primes from new book

numbers = [2]
for i in range(15):
	product = 1
	for n in numbers:
		product = product*n
	numbers.append(product+1)
for j in numbers:
	print j
	print
	print
