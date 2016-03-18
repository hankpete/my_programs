#include <stdio.h>

int main(int argc, char *argv[])
{
	int i = 0;

	while (i < argc) {
		printf("%s - %d\n", argv[i], i*2);
		i++;
	}

	//make my own array
	char *names[] = {"Henry", "Ajay", "Other ppl...."};
	int length = 3;
	int a = 0;

	while (a < length) {
		printf("%s\n", names[a]);
		a++;
	}

	return 0;
}
