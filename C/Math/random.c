#include <stdlib.h>
#include <time.h>
#include <stdio.h>

int main() 
{
	srand(time(NULL));
	int i;
	int r;
	for (i = 0; i < 10; i++) {
		r = rand() % 5;
		printf("%d\n", r);
	}

	return 0;
}
