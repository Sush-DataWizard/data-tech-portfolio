# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

def max_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    
    for x in nums[1:]:
        current_sum = max(x, current_sum + x)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example usage
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))  # Output: 6
