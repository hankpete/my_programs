#include <stdio.h>

int main(int argc, char *argv[])
{
	//create our arrays
	int nums[] = {2, 4, 8, 16, 32};
	char *words[] = {
		"dog", "cat", "mouse", "hog", "ohhh"
	};

	// safely get size
	int count = sizeof(nums) / sizeof(int);
	int i = 0;

	// first way - indexing
	for(i = 0; i < count; i++){
		printf("%s = %d is duh tru tru.\n", words[i], nums[i]);
	}

	printf("---\n");

	// set POINTERS to start of arrays
	int *pt_nums = nums;
	char **pt_words = words;

	// second way - pointers
	for(i = 0; i < count; i++) {
		printf("%s number %d.\n", *(pt_words+i), *(pt_nums+i));
	}

	printf("---\n");

	// third way - pointers can be used like arrays
	for(i = 0; i< count; i++) {
		printf("%s is %d big.\n", pt_words[i], pt_nums[i]);
	}

	printf("---\n");

	// fourth way - dumb complex way. think of them as a number
	// referencing a specific spot in the computer
	// so this is looking at how far away that number is to the original
	for(pt_words = words, pt_nums = nums;
		(pt_nums - nums) < count;
		pt_words++, pt_nums++)
	{
		printf("%s is hella %d.\n", *pt_words, *pt_nums);
	}

	return 0;
}
