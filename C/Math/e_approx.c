#include <stdio.h>
#include <math.h>

// recursion!!!
int factorial(int n) {
	if (n == 1) {
		return 1;
	} else {
		return n*factorial(n-1);
	}
}

int main() {

	double e = 1; 
	int i = 0;

	for (i = 1; i < 10; i++) {
		e += 1.0 / factorial(i);
	}

	printf("e = %lf\n", e);

	return 0;

}
