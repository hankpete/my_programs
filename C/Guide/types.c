#include <stdio.h>

int main(int argc, char *argv[])
{
	int integer = 1;
	float floating_small = 0.987f;
	double floating_big = 123.123;
	char letter = 'r';
	char string[] = "wow!";
	
	printf("An integer: %d\n", integer);
	printf("A small floating point: %f\n", floating_small);
	printf("A big floating point: %f\n", floating_big);
	printf("A character: %c\n", letter);
	printf("A string: %s\n", string);
	printf("In total: %d %f %f %c %s\n", integer, floating_small, floating_small, letter, string);

	return 0;
}
