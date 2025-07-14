def contains_nearby_duplicate(nums, k):
    num_to_index = {}

    for i, num in enumerate(nums):
        print(i,num)
    #     if num in num_to_index and abs(i - num_to_index[num]) <= k:
    #         return True
    #     num_to_index[num] = i  # update last seen index

    # return False

nums = [1,2,3,1]
k = 3

print(contains_nearby_duplicate(nums, k))