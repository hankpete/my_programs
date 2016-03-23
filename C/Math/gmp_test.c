#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>

int main() {

	mpz_t i;	//multiple precision integer

	mpz_init (i); //initialize i

	char *num;
	num = "897";
	mpz_set_str (i, num, 10); //set i to str num in base 10

	mpz_t j;
	mpz_init_set_str (j, "31415", 10);	 //init and set all at once

	mpz_mul (i, i, j); //set i to i*j

	mpz_t p;
	mpz_init_set_str (p, "7", 10);
	int is_prime;
	is_prime = mpz_probab_prime_p (p, 100); //built in prime test! probability test with 100 tries

	gmp_printf("%Zd\n", i);
	//gmp_printf("%Zd\n", j);
	printf("%d\n", is_prime);	//0 = probs not prime, 1 = probs prime, 2 = defs prime 
	
	mpz_t big;
	mpz_init_set_str (big, "88887776655893454637283746", 10);
	int small = 5;
	mpz_t new_small;
	mpz_init (new_small);

	mpz_set_ui (new_small, small);
	mpz_mul (big, big, new_small);

	gmp_printf("%Zd\n", big);

	return 0;

}
