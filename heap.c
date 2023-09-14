#include <stdio.h>


int isHeap(int array[], int length, int index)
{
    if(index >= length)
        return 0;
    if(array[index] < array[2*index])
        return 0;
    if(array[index] < array[2*index+1])
        return 0;

    return isHeap(array, length, 2*index+1) && isHeap(array, length, 2*index+1);
}



int main()
{
    int arr[] = {1, 2, 3, 4, 5, 10};
    isHeap(&arr);

    return 0;
}