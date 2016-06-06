#include <stdio.h>
#include <string.h>

int numberize (char letter) {
	if (letter == ' ') {return 26;}
	
	char *alphaLow = "abcdefghijklmnopqrstuvwxyz";
	char *alphaHigh = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	int i;
	for (i = 0; i < 26; i++) {
		if (alphaHigh[i] == letter || alphaLow[i] == letter) {
			return i;
		}
	}
}

int main(void) {
	
	char *names[100] = {"Henry Peterson", "Jim Sullivan", "Yang Vang"};
	int namesLen = 3;
	
	int i;
	int j;
	int k = 0;
	int z;
	int intName[50];
	for (i = 0; i < namesLen; i++) {
		for (j = 0; j < strlen(names[i]); j++) {
			intName[k] = numberize(names[i][j]);
			k++;
			if (j + 1 == strlen(names[i])) {
				for (z = 0; z < k; z++) {
					if (intName[z] == 26) { 
						printf("  ");
						continue;
					}
					printf("%d ", intName[z]);
					intName[z] = 26;
				}
				printf("\n");
				k = 0;
			}
		}
	}
	return 0;
}
