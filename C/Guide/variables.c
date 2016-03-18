#include <stdio.h>

int main(int argc, char *argv[])
{
	//big numbers
	long big_num = 1024L * 1024L * 1024L;		//long for big

	printf("big af %ld\n", big_num);		//use %ld for big

	//tiny numbers
	double tiny_num = 0.000000789;

	printf("tiny af %e\n", tiny_num);		//use %e for sci note

	//null
	char null = '\0';
	int percent = null * big_num * tiny_num;

	printf("null percent = %d%%\n", percent);		// use %% for a % sign
	
	return 0;
}
