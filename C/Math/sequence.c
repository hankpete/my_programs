#include <stdio.h>
#include <math.h>

//recursion!!!
double function(double number, int count) {
	int i = count;
	if (count == 0) {
		return number;
	} else {
    	number = sqrt(2*number);
		printf("%lf\n", number);
		i -= 1;
	}
    return function(number, i);
}

int main(int argc, char *argv[]){
    
    double a_n = sqrt(2);
	int i = 20;

	a_n = function(a_n, i);

    printf("The sequence should go to 2.\n");
    printf("After %d iterations, a_%d = %lf.\n", i, i, a_n);

    return 0;
}        
