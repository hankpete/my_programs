# find smallest base primitive primes

import math 

def is_prime(num):
    factor = 2
    while num > 1:
        remainder = num%factor
        if factor > math.sqrt(num):
            # prime
            return True
        else:
            if remainder == 0:
                # not prime
                return False
            else:
                factor += 1

n = int(raw_input("n = "))
primes = []
for i in range(3, n):
	if is_prime(i):
		primes.append(i)

print "p  |  g"
print "--------"
a = 2
h = 1
twocount = 0
count = 0
for x in range(len(primes)):
	p = primes[x]
	while True:
		m = pow(a, h, p)
		if m == 1:
			if h == (p-1):
				count += 1.0
				if count%100 == 0:  
					print "currently at: " + str(p) + "  |  " + str(a)
				if a == 2:
					twocount += 1.0
				a = 2
				h = 1
				break
			elif h != (p-1):
				a += 1
				h = 1
		else:
			h += 1

print "percent that have g = 2 -->" + str(twocount/count * 100)

#did it from 0-100,000 primes and got percent 2 --> 37.5664685643