#include <stdio.h>
#include <time.h>

void sleep(double secs)
{
	double clocks = (double) CLOCKS_PER_SEC;   // chage constant to a double to divide by it
	double endtime = clock()/clocks + secs;    // clock() gets how many clock ticks since start, divide by system constant
	while(clock()/clocks < endtime);		   // loop til endtime	
}


int main()
{
	int bar_length = 100;
	int i, j;
	double percent;
	for (i = 0; i <= bar_length; i++) {
		printf("\r[");
	    for (j = 0; j < i; j++) {
			printf("#");
		}
		for (j = i; j < bar_length; j++) {
			printf(" ");	
		}
		percent = ( (double) i / bar_length ) * 100;	
		printf("]\t%.0f %%", percent);	// %.0f just goes to the ones place (%.1f would be first decimal etc)
		sleep(0.03);
		fflush(stdout);
	}
	printf("\n");
	return 0;
}	
