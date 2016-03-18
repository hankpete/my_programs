# make some fermat numbers. find which ones aren't prime. find their prime factors
# Henry Peterson 9/25/15

import math

# make some fermat numbers
f_nums = []

print "Fermat Nums\n"
n = 0
for i in range(6):
    print 2**(2**n) + 1
    f_nums.append(2**(2**n) + 1)
    n += 1
    
print
# find which ones are not prime
f_composites = []
def is_prime(num):
    factor = 2
    while num > 1:
        remainder = num%factor
        if factor > math.sqrt(num):
            # prime
            return True
            break
        else:
            if remainder == 0:
                # not prime
                return False
                break
            else:
                factor += 1

print "Composite ones\n"
for n in f_nums:
    if not is_prime(n):
        print n
        f_composites.append(n)
        
# look at each composite number and find its factors. are any prime?
print
for num in f_composites:
    print num
    comp_factors = []
    for i in range(num/2):
        if num%i == 0:
            print str(i) + "\t"
            comp_factors.append(i)

    for n in comp_factors:
        if is_prime(n):
            print "\t" + str(n)

            
    
