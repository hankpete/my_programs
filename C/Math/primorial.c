#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <gmp.h>

int main(int argc, char *argv[])
{	
    int *primes;
	int *final_primes;
	int p = atoi(argv[1]) + 1;	

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

	if (check == 1) {
		gmp_printf("p = %d ---> p# + 1 = %Zd ---> probably prime!\n", p, primorial);
	} else if (check == 2) {
		gmp_printf("p = %d ---> p# + 1 = %Zd ---> prime!!\n", p, primorial);
	} else {
		gmp_printf("%d ---> p# + 1 = %Zd ---> not prime :(\n", p, primorial);
	}
	
	return 0;
}
