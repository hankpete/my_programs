#include <stdio.h>

int main(int argc, char *argv[])
{
	int i;
	
	if (argc == 1) {
		printf("GTFO man you didn't pass any arguments to my program. bitch.\n");
	} else if ( argc > 1 && argc < 4) {
		printf("Your args:\n ");
		for (i = 0; i < argc; i++) {
			printf("%s\n", argv[i]);
			}
		}
	else {
		printf("That's way too much homie, gimme a break.\n");
	}
	
	return 0;
}
