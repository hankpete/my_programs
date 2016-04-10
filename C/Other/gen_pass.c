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
		printf("%s\n", message);
	}

	exit(1);
}

void help()
{
	char *string = "\n'gen_pass' is a password generator written in C."
					"\n\nUsable Flags:"
					"\n       -h            show this message"
					"\n       -c [number]   maximum number of capital letters"
					"\n       -l [number]   maximum number of lower case letters"
					"\n       -n [number]   maximum number of numbers"
					"\n       -s [number]   maximum number of symbols"
					"\n       -i [number]   maximum number of total letters"
					"\n\nExample Usage:"
					"\n       gen_pass -i 12 -c 5 -l 5 -n 2\n\n";
					 
	printf("%s", string);
	exit(1);
}

int main(int argc, char *argv[]) 
{
	if (argc < 2) die("USAGE: gen_pass <flag> [param] <flag> [param]....\ngen_pass -h for options.");

	// to get rand
	srand(time(NULL));

	// set defaults that may be changed
	int n = 100;
	int caps = 100;
	int lows = 100;
	int nums = 100;
	int syms= 100;
	
	// check for flags and get the new params
	int i;
	int new_num;
	for (i = 1; i < argc; i += 2) {
		if (argv[i][0] == '-'){ 
			if (argv[i][1] != 'h') {
				// look at the number given next
				if (argv[i+1]) {
					new_num = atoi(argv[i+1]);
				} else {
					die("Error: param or flag not stated.");
				}
			}
			switch(argv[i][1]){	
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
				case 'h':
					help();
					break;
				default:
					die("Invalid use of flags.");
			}
		} else {
			die("USAGE: gen_pass <flag> [param] <flag> [param]....\n./gen_pass -h for options.");
		}
	}

	if ((caps + lows + nums + syms) < n) {
		die("Impossible password configuration");
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
		flip1 = rand() % 4;
		switch(flip1){
			case 0:
				if (caps) {
					flip2= rand() % 26;
					letter = CAPS[flip2];						
					pass[i] = letter;
					caps -= 1;
				} else {
					i--;	//gotta go back
				}
				break;
			case 1:
				if (lows) {
					flip2 = rand() % 26;
					letter = LOWS[flip2];
					pass[i] = letter;
					lows -= 1;
				} else {
					i--;
				}
				break;
			case 2:
				if (nums) {
					flip2 = rand() % 10;
					letter = NUMS[flip2];
					pass[i] = letter;
					nums -= 1;
				} else {
					i--;
				}
				break;
			case 3:
				if (syms) {
					flip2 = rand() % 6;
					letter = SYMS[flip2];
					pass[i] = letter;
					syms -= 1;
				} else {
					i--;
				}
				break;
		}

	}

	pass[n] = '\0';
	printf("%s\n", pass);

	return 0;
}
