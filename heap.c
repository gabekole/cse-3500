#include <stdio.h>


int isHeap(int array[], int length)
{
    for(int index = 0; index < length; index++){
        if(2*index < length && array[2*index] > array[index])
            return 0;
        if(2*index + 1 < length && array[2*index+1] > array[index])
            return 0;

    }

    return 1;
}



int main()
{
    int arr[] = {1, 2, 3, 4, 5, 10};
    printf("%d", isHeap(arr, 6));    
    
    
    return 0;
}