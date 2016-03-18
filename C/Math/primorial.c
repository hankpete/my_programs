#include <stdio.h>
#include <math.h>
#include <string.h>

#define RANGE 10

void sieve(int *nums) {
    
    int primes[RANGE];
    int i = 0;
   
    primes[0] = 2;
    
    int n = 0;
    int done = 0;
    while (done != 1) {
        for(i = 0; i<RANGE; i++) {
            if (nums[i]%primes[n] == 0) {
                nums[i] = 0;
            }
        }
        n++;
        done = 1;
        for(i = 0; i<RANGE; i++) {
            if (nums[i] != 0) {
                primes[n] = nums[i];
                done = 0;
                break;
            }
        }    
    }
    memcpy(nums, primes, sizeof(nums));   
} 


int main() {
    
    int nums[RANGE];

    int i = 0;

    for(i = 2; i<RANGE+2; i++) {
        nums[i] = i;
    }
    
    sieve(nums);

    for (i = 0; i < RANGE; i++) {
        printf("%d, ", nums[i]);
    }
    
    return 0;
}
