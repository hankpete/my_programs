#include <stdio.h>
#include <math.h>

int main() {

	double e = 2.0;
	int n = 2;

	int factorial = 1;
	int i = 0;
	for (n = 2; n < 20; n++) {
		for (i = 2; i <= n; i++) {
			factorial *= i;
		}
		e += 1.0 / factorial;
		factorial = 1;
	}

	printf("e = %lf\n", e);

	return 0;

}
