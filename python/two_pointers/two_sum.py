def two_sum():

    nums = [2,7,11,15]
    target = 9

    left,right = 0 , len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left+1, right+1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
        
print(two_sum())
