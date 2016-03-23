#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
   	
    int RANGE = atoi(argv[1]); 
    int *primes;
	
	// put it on the heap cuz it can get big
	primes = malloc(sizeof(int)*RANGE);

    int i, k;

	// start primes as all 1s
    for(i = 2; i<RANGE; i++) {
		primes[i] = 1;
    }
	

	// go through the multiples, set composites to 0
	for (i = 2; i<RANGE; i++) {
		if (primes[i]) {
			for (k = i; k*i < RANGE; k++) {
				primes[k*i] = 0;
			}
		}
	}

	// now print the index vals of all the 1s in primes
	int j = 0;
	for (i = 2; i < RANGE; i++) {
		if (primes[i]) {
			printf("%d, ", i);
			j++;
		}
	}

	printf("\n");

	free(primes);

	return 0;
}
