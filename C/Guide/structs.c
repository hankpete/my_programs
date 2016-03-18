#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>

// struct works similarly to classes in OOP 
struct Team {
	char *name;
	int wins;
	int losses;
	int ties;
};

struct Team *Team_create(char *name, int wins, int losses, int ties)
{
	// malloc = memory allocate to ask os for piece of raw mem
	struct Team *who = malloc(sizeof(struct Team));
	// assert makes sure the piece of mem is valid (not null)
	assert(who != NULL);

	// initialize each field of struct Team, setting each part
	who->name = strdup(name);	//strdup duplicates string (copies original string into memory it creates like malloc)
	who->wins = wins;
	who->losses = losses;
	who->ties = ties;

	return who;
}

void Team_destroy(struct Team *who)
{
	assert(who != NULL);

	// free returns the memory given by malloc and strdp
	free(who->name);
	free(who);
}

void Team_print(struct Team *who)
{
	printf("Name: %s\n", who->name);
	printf("\tWins: %d\n", who->wins);
	printf("\tLosses: %d\n", who->losses);
	printf("\tTies: %d\n", who->ties);
}

int main(int argc, char *argv[])
{
	//make a couple of teams
	struct Team *jets = Team_create("NY Jets", 8, 8, 0);
	struct Team *bears = Team_create("Chicago Bears", 4, 11, 1);

	// print them out and where they r in memory
	printf("The NY Jets are at memory location %p:\n", jets);	// %p shows where smthn is
	Team_print(jets);

	printf("The Chicago Bears are at memory location %p\n", bears);
	Team_print(bears);

	// change values and print again
	jets->wins += 1;
	jets->losses -= 1;
	jets->ties = 0;
	Team_print(jets);

	bears->wins -= 2;
	bears->losses += 2;
	bears->ties = 1;
	Team_print(bears);

	// destroy both to clean up
	Team_destroy(jets);
	Team_destroy(bears);

	return 0;
}
