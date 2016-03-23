#include <stdio.h>
#include <math.h>

int main() {
	
	int n = 0;
	double pi = 0;

	for (n = 0; n < 10000; n++) {
		if (n % 2 == 0) {
			pi += 1.0 / (pow(3, n)*(2*n + 1));
		} else {
			pi -= 1.0 / (pow(3, n)*(2*n + 1));
		}
	}

	pi *= 2*sqrt(3);

	printf("pi = %lf\n", pi);

	return 0;

}
