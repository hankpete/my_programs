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
	if (argc < 2) die("USAGE: ./gen_pass <flag> [param]");//\n./gen_pass -h for options.");

	// to get rand
	srand(time(NULL));

	// set defaults that may be changed
	int n = 100;
	int caps = n;
	int lows = n;
	int nums = n;
	int syms= n;
	
	// check for flags and get the new params
	int i;
	int new_num;
	for (i = 1; i < argc; i++) {
		if (argv[i][0] == '-'){ 
			i++;		// look at the number given next
			if (argv[i]) {
				new_num = atoi(argv[i]);
			}
			switch(argv[i-1][1]){	
				case 'i':
					n = new_num;
					break;
				case 'c':
					caps = new_num;
					break;
				case 'l':
					lows = new_num;
					break;
				case 'n':
					nums = new_num;
					break;
				case 's':
					syms = new_num;
					break;
				default:
					die("Invalid use of flags.");
			}
		} else {
			die("USAGE: ./gen_pass <flag> [param]");
		}
	}

	if ((caps + lows + nums + syms) < n) {
		n = (caps + lows + nums + syms);
		printf("Note: your password length was changed to fit your parameters.\n");
	}			
				 
	char *CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	char *LOWS = "abcdefghijklmnopqrstuvwxyz";
	char *NUMS = "0123456789";
	char *SYMS = "!@#$%*";

	int flip1;
	int flip2;
	
	char letter;
	char pass[n+1];

	for (i = 0; i < n; i++) {
		flip1 = rand() % 10;
		switch(flip1){
			case 0:
			case 1:
				if (caps) {
					flip2= rand() % 26;
					letter = CAPS[flip2];						
					caps -= 1;
				} else {
					i--;	//gotta go back
				}
				break;
			case 3:
			case 4:
			case 5:
			case 6:
				if (lows) {
					flip2 = rand() % 26;
					letter = LOWS[flip2];
					lows -= 1;
				} else {
					i--;
				}
				break;
			case 7:
			case 8:
				if (nums) {
					flip2 = rand() % 10;
					letter = NUMS[flip2];
					nums -= 1;
				} else {
					i--;
				}
				break;
			case 9:
				if (syms) {
					flip2 = rand() % 6;
					letter = SYMS[flip2];
					syms -= 1;
				} else {
					i--;
				}
				break;
		}

		pass[i] = letter;
	}

	pass[n] = '\0';
	printf("%s\n", pass);

	return 0;
}
