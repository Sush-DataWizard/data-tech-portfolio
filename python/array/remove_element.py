

# Output: 2, nums = [2,2,_,_]

nums = [3,2,2,3]
val = 3

nums = [0,1,2,2,3,0,4,2]
val = 2

def remove_element(nums, val):

    k = 0
    for i in range(len(nums)):
        if (nums[i] != val):
            nums[k] = nums[i]
            k += 1
    return k, nums

print(remove_element(nums, val))


# time complexity: O(n)
# space complexity: O(1)
