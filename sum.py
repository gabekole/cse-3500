
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
        lower_num = nums[left_index]
        higher_num = nums[right_index]
        current_sum = lower_num + higher_num

        if(current_sum == target):
            return True
        if(current_sum > target):
            right_index -= 1
        if(current_sum < target):
            left_index += 1
        
    return False

if __name__ == "__main__":
    pass