
def Minimum_Size_Subarray_Sum():

    target = 7
    nums = [2,3,1,2,4,3]

    n = len(nums)
    left = 0
    min_length = float('inf')
    total = 0

    for right in range(n):
        total += nums[right]

        while total >= target:
            min_length = min(min_length, right-left+1)
            total -= nums[left]
            left += 1
    
    return  0 if min_length == float('inf') else min_length


print(Minimum_Size_Subarray_Sum())