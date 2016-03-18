#include <stdio.h>

int main(int argc, char *argv[])
{
	int nums[4] = {3};
	char name[6] = {'H'};

	// printing raw
	printf("raw nums: %d %d %d %d\n", nums[0], nums[1], nums[2], nums[3]);
	printf("raw name each: %c %c %c %c %c %c\n", name[0], name[1], name[2], name[3], name[4], name[5]);
	printf("raw name: %s\n", name);

	//setup nums
	nums[0] = 6;
	nums[1] = 6;
	nums[2] = 6;
	nums[3] = 7;

	//setup name 
	name[0] = 'H';
	name[1] = 'e';
	name[2] = 'n';
	name[3] = 'r';
	name[4] = 'y';
	name[5] = '\0';

	printf("new nums: %d %d %d %d\n", nums[0], nums[1], nums[2], nums[3]);  
        printf("new name each: %c %c %c %c %c %c\n", name[0], name[1], name[2], name[3], name[4], name[5]);
        printf("new name: %s\n", name);

	// another way to use name - the good way!
	char *another = "Henry";
	
	printf("another way: %s\n", another);
	printf("each in other way: %c %c %c %c %c %c\n",another[0], another[1], another[2], another[3], another[4], another[5]);

	return 0;
}
