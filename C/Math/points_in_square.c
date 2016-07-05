#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double r() {
	//return a random floar btwn 0 and 1
	return (double) rand() / (double) RAND_MAX;
}

int main(int argc, char *argv[]) {
	
	int iterations = 1000;
	if ( argc == 2 ) {
		iterations = atoi( argv[1] );
	}

	srand( time(NULL) );
	
	int i;
	double sum = 0;
	double x1;
	double x2;
	double y1;
	double y2;	
	for ( i = 0; i < iterations; i++ ) {
		x1 = r();
		x2 = r();
		y1 = r();
		y2 = r();
		sum += sqrt( pow( (x1-x2), 2 ) + pow( (y1-y2), 2 ) );	
	}	

	printf("%f\n", sum / (double) iterations);
	
	return 0;
}
