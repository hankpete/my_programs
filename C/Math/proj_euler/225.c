#include <stdio.h>

//int trib_help(int x, int y, int z, int A);

int trib(int a, int b, int c, int n)
{
		if (n==0) {
			return a;
		} else if (n==1) {
			return b;
		} else if (n==2) {
			return c;
		} else {
			return trib(b, c, a+b+c, n-1);
		}

}

int main(int argc, char *argv[])
{

	int odds[10000];
	int i;

	long tribs[1000];
	for (i=0; i<10; i++) {
		tribs[i] = trib(1, 1, 1, i+3);
		printf("%d\n", tribs[i]);
	}
/*
	for (i = 0; i < 10000; i++) {
		odds[i] = 27 + 2*i;
	}

	int winner_odds[200];
	int j;
	int won = 1;

	for (i = 0; i < 1000; i++) {
		for (j = 0; j < n; j++) {
			x = trib(1, 1, 1, j);
			if (x % odds[i] == 0) {
				won = 0;
			}
		}
		if (won) {
			winner_odds[0] = odds[i];
		}
	}

	for (i = 0; i < 200; i++) {

		printf("%d\n", winner_odds[i]);
	}
*/
	return 0;

}
