#include <stdio.h>
#include <stdbool.h>


bool isHeap(int array[], int length)
{
    for(int index = 0; index < length; index++){
        // printf("%d left: %d right:%d\n", array[index], array[2*index+1], array[2*index+2]);
        if(2*index + 1< length && array[2*index+1] > array[index])
            return false;
        if(2*index + 2 < length && array[2*index+2] > array[index])
            return false;

    }

    return true;
}



int main()
{
    //     10
    //  5      6
    // 4 5   1
    int arr[] = {10, 5, 6, 4, 5, 1};
    printf("%d\n", isHeap(arr, 5));    
    
    
    return 0;
}