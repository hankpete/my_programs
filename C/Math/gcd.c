#include <stdio.h>
#include <stdlib.h>

int find_g(int x, int y) 
{
	// note, x > y
	int r;
	int i = 1;

	while (i*y < x) {
	i++;
	}
	
	if (i*y == x) {
		return y;
	} else {
		i--;
		r = x - y*i;
		find_g(y, r);
	}
}

int main(int argc, char *argv[])
{
	if (argc != 3){
		printf("Please pass two numbers into the function call to find their greatest common divisor.\n");
		exit(1);
	}

	int a = atoi(argv[1]);
	int b = atoi(argv[2]);

	int g;

	if (a > b) {
		g = find_g(a, b);
	} else if (a < b) {
		g = find_g(b, a);
	} else {
		// a == b
		g = a;
	}

	printf("%d\n", g);

	return 0;
}	
