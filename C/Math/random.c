#include <stdlib.h>
#include <time.h>
#include <stdio.h>

int main() 
{
	srand(time(NULL));
	int r = rand();

	printf("%d\n", r);

	return 0;
}
