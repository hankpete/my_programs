#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <gmp.h>

int check_primorial (int p) 
{
    int *primes;
	int *final_primes;

	// put it on the heap cuz it can get big
	primes = malloc(sizeof(int)*p);
	final_primes = malloc(sizeof(int)*p);

    int i, k;

	// start primes as all 1s, final as array of 0s
    for(i = 2; i<p; i++) {
		primes[i] = 1;
		final_primes[i] = 0;
    }
	

	// go through the multiples, set composites to 0
	for (i = 2; i<p; i++) {
		if (primes[i]) {
			for (k = i; k*i < p; k++) {
				primes[k*i] = 0;
			}
		}
	}

	// now put the index vals of all the 1s in primes in a list
	int j = 0;
	for (i = 2; i < p; i++) {
		if (primes[i]) {
			final_primes[j] = i;
			j++;
		}
	}

	mpz_t primorial;		// going to get big, use gmp
	mpz_init_set_str (primorial, "1", 10);
	mpz_t prime_num;
	mpz_init (prime_num);		// make a new number p to be able to use gmp funcs
	for (i = 0; i<p; i++) {
		if (final_primes[i] == 0) {
			break;
		}
		mpz_set_ui (prime_num, final_primes[i]);		// make p the i'th prime 
		mpz_mul (primorial, primorial, prime_num);		// primorial *= p
	}	

	mpz_t one;
	mpz_init_set_str (one, "1", 10);    
	mpz_add (primorial, primorial, one);

	// check if it is prime
	int check;
   	check = mpz_probab_prime_p (primorial, 10);
	
	free(primes);
	free(final_primes);

	return check;
}


int main(int argc, char *argv[])
{	
	
    int *primes;
	int *final_primes;
	int range = 45000;

	// put it on the heap cuz it can get big
	primes = malloc(sizeof(int)*range);
	final_primes = malloc(sizeof(int)*range);

    int i, k;

	// start primes as all 1s, final as array of 0s
    for(i = 2; i<range; i++) {
		primes[i] = 1;
		final_primes[i] = 0;
    }
	

	// go through the multiples, set composites to 0
	for (i = 2; i<range; i++) {
		if (primes[i]) {
			for (k = i; k*i < range; k++) {
				primes[k*i] = 0;
			}
		}
	}

	// now put the index vals of all the 1s in primes in a list
	int j = 0;
	for (i = 2; i < range; i++) {
		if (primes[i]) {
			final_primes[j] = i;
			j++;
		}
	}
	
	int check;
	for (i = 0; i < range; i++) {
		if (final_primes[i] == 0) {
			break;
		} else {
			check = check_primorial(final_primes[i] + 1 );	//run the function, make it inclusive
			
			if (check == 1) {
				printf("p = %d ---> p# + 1 ---> probably prime!\n", final_primes[i]);
			} else if (check == 2) {
				printf("p = %d ---> p# + 1 ---> prime!!\n", final_primes[i]);
			} else {
				// do nothing... printf("%d ---> p# + 1 ---> not prime :(\n", final_primes[i]);
			}
		}
	}
	
	return 0;
}
