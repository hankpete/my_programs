#include <stdio.h>

int main(int argc, char *argv[])
{
	int i = 0;

	//go through the strings passed to argv
	//skipping i = 0 bc that is ./ex10
	for(i=1; i < argc; i++) {
		printf("arg %d: %s\n", i, argv[i]);
	}

	//my own array of strings
	char *my_arr[] = {
		"Henry", "likes", "Sabrina"
	};
	int length = 3;

	for(i = 0; i < length; i++) {
		printf("my_arr arg %d: %s\n", i, my_arr[i]);
	}

	return 0;
} 
