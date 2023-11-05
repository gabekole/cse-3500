import random
import sys
import time
import matplotlib.pyplot as plt

def medianOfMedians(L):
    if(len(L) <= 5):
        return sorted(L)[len(L) // 2]
            

    res = [0] * (len(L) // 5)

    for i in range(0, len(L) // 5):
        res[i] = medianOfMedians(L[i: i+5])

    return medianOfMedians(res)

def quickSortLast(L):
    if len(L) <= 1:
        return L
    pivot = L[-1]
    leftHalf = [k for k in L[:-1] if k < pivot]
    rightHalf = [k for k in L[:-1] if k >= pivot]
    return quickSortLast(leftHalf) + [pivot] + quickSortLast(rightHalf)

def quickSortMedian(L):
    if len(L) <= 1:
        return L
    
    pivot = medianOfMedians(L)
    leftHalf = [k for k in L[:-1] if k < pivot]
    rightHalf = [k for k in L[:-1] if k >= pivot]
    return quickSortLast(leftHalf) + [pivot] + quickSortLast(rightHalf)


random_last_data = []
random_mid_data = []
x = []

for n in range(100, 3000, 100):
    print(sys.setrecursionlimit(10000))

    rand_list=[]
    for i in range(n):
        rand_list.append(random.randint(3,9))
    list_sorted = sorted(rand_list)

    start = time.process_time()
    quickSortLast(rand_list.copy())
    end = time.process_time()
    rand_last = end-start

    start = time.process_time()
    quickSortMedian(rand_list.copy())
    end = time.process_time()
    rand_mid = end-start


    start = time.process_time()
    quickSortLast(rand_list.copy())
    end = time.process_time()
    sorted_last = end-start

    start = time.process_time()
    quickSortMedian(rand_list.copy())
    end = time.process_time()
    sorted_mid = end-start

    print(f'n: {n}\nSorted-Mid: {sorted_mid*1000}')
    print(f'Sorted-Last: {sorted_last*1000}')
    print(f'Random-mid: {rand_mid*1000}')
    print(f'Random-last: {rand_last*1000}')

    x.append(n)
    random_last_data.append(rand_last)
    random_mid_data.append(rand_mid)

plt.plot(x, random_last_data, 'r')
plt.plot(x, random_mid_data, 'b')
plt.show()