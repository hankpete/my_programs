#include <stdio.h>
#include <math.h>

double function(double number) {
    number = sqrt(2*number);
    return number;
}

int main(int argc, char *argv[]){
    
    double a_n = sqrt(2);
    int i;

    for(i = 0; i < 100; i++){
        printf("%lf\n", a_n);
        a_n = function(a_n);
    }

    printf("%lf\n", a_n);
    printf("The sequence should go to 2.\n");
    printf("After %d iterations, a_%d = %lf.\n", i, i, a_n);

    return 0;
}        
