#include <stdio.h>
#include <errno.h>
#include <time.h>
#include <stdlib.h>

// abort with an error
void die(const char *message)
{
	if(errno) {
		perror(message);
	} else {
		printf("ERROR: %s\n", message);
	}

	exit(1);
}

int main(int argc, char *argv[]) 
{
	if (argc < 2) die("USAGE: ./gen_pass [number of letters]");

	// to get rand
	srand(time(NULL));

	// set defaults that may be changed
	int n = atoi(argv[1]);
	
	char *CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	char *LOWS = "abcdefghijklmnopqrstuvwxyz";
	char *NUMS = "0123456789";
	char *SYMS = "!@#$%*";

	int flip1;
	int flip2;
	
	char letter;
	char pass[n+1];

	int i;
	for (i = 0; i < n; i++) {
		flip1 = rand() % 10;
		switch(flip1){
			case 0:
			case 1:
				flip2= rand() % 26;
				letter = CAPS[flip2];						
				break;
			case 3:
			case 4:
			case 5:
			case 6:
				flip2 = rand() % 26;
				letter = LOWS[flip2];
				break;
			case 7:
			case 8:
				flip2 = rand() % 10;
				letter = NUMS[flip2];
				break;
			case 9:
				flip2 = rand() % 6;
				letter = SYMS[flip2];
				break;
		}

		pass[i] = letter;
	}

	pass[n] = '\0';
	printf("%s\n", pass);

	return 0;
}
