#include <stdio.h>
#include <stdbool.h>


bool isHeap(int array[], int length)
{
    for(int index = 0; index < length; index++){
        if(2*index < length && array[2*index] > array[index])
            return false;
        if(2*index + 1 < length && array[2*index+1] > array[index])
            return false;

    }

    return true;
}



int main()
{
    int arr[] = {1, 2, 3, 4, 5, 10};
    printf("%d", isHeap(arr, 6));    
    
    
    return 0;
}