#include <stdio.h>
#include <ctype.h>

// forward declarations define functions before they are real
// (chinken and egg prob)
int can_print_it(char ch);
void print_letters(char arg[]);

// loops through all the arguments passed
void print_arguments(int argc, char *argv[])
{
	int i = 0;

	for(i = 0; i < argc; i++) {
		print_letters(argv[i]);
	}
}

// for each letter in the arg, it checks to 
// see if it is ASCII coded and prints it if it is
void print_letters(char arg[])
{
	int i = 0;
	
	for(i = 0; arg[i] != '\0'; i++) {
		char ch =arg[i];

		if(can_print_it(ch)) {
			printf("'%c' == %d ", ch, ch);
		}
	}
	
	printf("\n");
}

// check for ascii
int can_print_it(char ch)
{
	//these are the funcs from ctype.h 
	return isalpha(ch) || isblank(ch);
}

int main(int argc, char *argv[])
{
	print_arguments(argc, argv);
	return 0;
}
