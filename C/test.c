#include <stdio.h>
#include <string.h>

void test(int *array) {
    int other[1] = {1};
    
    memcpy(array,other, sizeof(array));    
}

int main() {

    int array[3] = {0, 1, 2};

    test(array);
    
    printf("%d", array[0]);

    return 0;

} 
