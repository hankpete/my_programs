#include <stdio.h>

int main(int argc, char * argz[])
{
	int array[] = {1, 2, 3, 4, 5};
	char name[] = "Henry";
	char full_name[] = {'H', 'e', 'n', 'r', 'y', ' ', 'P', 'e', 't', 'e', 'r', 's', 'o', 'n', '\0'};

	printf("Size of an int: %u\n", sizeof(int));
	printf("Size of my array: %u\n", sizeof(array));
	printf("Number of elements in array = size of array / size of int = %u\n", sizeof(array)/sizeof(int));
	printf("First element of array = %d\n", array[0]);

	printf("Size of a char: %u\n", sizeof(char));
	printf("Size of name array: %u\n", sizeof(name));
	printf("Size of full name array: %u\n", sizeof(full_name));
	printf("name = %s, fullname = %s\n", name, full_name);

	return 0;
}
