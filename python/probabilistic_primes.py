# probabilistic prime checks

import random, math 

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

#a_list = [2,3,5,7] 

def fermat(n, k):
	for iteration in range(k):
		#a = a_list[random.randrange(len(a_list))]
		a = random.randrange(2, n)
		if ((a**(n - 1)) % n) != 1:
			# not prime
			return False
		# else prime
		return True

def miller_rabin(n, k):
    a_list = range(2, n-1)
    s = n - 1
    t = 0
    while s % 2 == 0:
        # keep halving s until it is odd
        # count with t
        s = s//2
        t += 1

    for iteration in range(k):
        a = a_list[random.randrange(len(a_list))]
        a_list.remove(a)
        x = pow(a, s, n)
        if x != 1:
            i = 0
            while x != (n - 1):
                if i == (t - 1):
                    return False
                else:
                    i += 1
                    x = (x**2) % n
    return True

if miller_rabin(1257963, 100):
    print "probs prime"	
else:
    print "composite"
