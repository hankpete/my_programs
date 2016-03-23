#!/usr/bin/python3

# uses sieve method to make primes
# multiplies them together to get primorial primes
# check if prime

from math import *

def sieve(n):
    
    nums = []
    for i in range(2, n+1):
        nums.append(i)

    primes = []

    x = 0
    while nums:

        primes.append(nums[0])
        
        new_nums = []
        for i in nums:
            if i % primes[x] != 0:
                new_nums.append(i)
 
        x += 1
        nums = new_nums

    return primes

def gen_primorial(array):
    
    primorial = 1
    for i in array:
        primorial *= i
    primorial += 1
    
    return primorial

def is_prime(x):
    
    for i in range(2, int(floor(sqrt(float(x))))):
        if x % i == 0:
            return False
    
    return True

def main():

    print("Primes 'p' for which 'p# + 1' is prime:\n") 
    primes_list = sieve(1000)    
    for n in primes_list:
        if n:
            primes = sieve(n)
            primorial = gen_primorial(primes)
            check = is_prime(primorial)
            if check:
                print(n) 
# run it
main()


