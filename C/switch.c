#include <stdio.h>

int main(int argc, char *argv[])
{
	if (argc != 2) {
		printf("You need one argument.\n");
		return 1; //how to end a program early
	}

	int i;
	for (i = 0; argv[1][i] != '\0'; i++) {
		char letter = argv[1][i];
		
		//it keeps track of where each case is and jumps to right one 
		switch(letter) {
			case 'h':
			case 'H': 
				printf("%d: H!!! Yassss\n", i);
				break;
			case 's':
			case 'S':
				printf("%d: S. Not bad.\n", i);
				break;
			default:
				printf("%d: %c. meh.\n", i, argv[1][i]);
			}
	}

	return 0;
}
