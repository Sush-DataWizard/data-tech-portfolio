

#### Remove Duplicates from Sorted Array I ####

# method 1

nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]

def remDup(nums):
    k = 1
    for i in range(len(nums)):
        if nums[i] != nums[k-1]:
            nums[k] = nums[i]
            k += 1
    return k, nums

print(remDup(nums))


# method 1

nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
def remDup1(nums):
    k = 0 
    for i in range(len(nums)):
        if k < 1 or nums[i] != nums[k-1]:
            nums[k] = nums[i]
            k += 1

    return k, nums

print(remDup1(nums))
