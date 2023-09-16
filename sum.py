import time 
import matplotlib.pylab as plt

def brute_force_sum(nums, target):
    for num_1 in nums:
        for num_2 in nums:
            if num_1 + num_2 == target:
                return True
    return False

def smart_sum_target(nums, target):
    nums_sorted = sorted(nums)

    left_index = 0
    right_index = len(nums_sorted) - 1

    while(left_index <= right_index):
        lower_num = nums_sorted[left_index]
        higher_num = nums_sorted[right_index]
        current_sum = lower_num + higher_num

        if(current_sum == target):
            return True
        if(current_sum > target):
            right_index -= 1
        if(current_sum < target):
            left_index += 1
        
    return False

def getRunTime(func):
        i = 10
        run_times = dict()
        while(i <= 1_000_000):
            start = time.process_time()
            targets = []
            with open('./CollectionNumbers/listNumbers-'+str(i)+'-nsol.txt') as f:
                lines = f.read().splitlines()
                targets = [int(numeric_string) for numeric_string in lines]
            numbers = []
            with open('./CollectionNumbers/listNumbers-'+str(i)+'.txt') as f:
                lines = f.read().splitlines()
                numbers = [int(numeric_string) for numeric_string in lines]
            
            for target in targets:
                func(numbers, target)
            
            run_times[i] = (time.process_time() - start)/10.0

            i *= 10
        return run_times

if __name__ == "__main__":
    # arr = [0, -1, 2, -3, 1]
    # x= -2
    # print(smart_sum_target(arr, x))
    # print(brute_force_sum(arr, x))

    

    
    smart_run_times = getRunTime(smart_sum_target)
    brute_run_times = getRunTime(brute_force_sum)

    print(smart_run_times)
    print(brute_run_times)

    data_1 = sorted(smart_run_times.items()) 
    data_2 = sorted(brute_run_times.items())

    x1, y1 = zip(*data_1)
    x2, y2 = zip(*data_2)

    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.show()