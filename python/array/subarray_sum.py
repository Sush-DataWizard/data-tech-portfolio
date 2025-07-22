def subarraySum(nums, k):
    count = 0
    prefix_sum = 0
    prefix_map = {0: 1}  # to handle when subarray itself equals k

    for num in nums:
        prefix_sum += num
        # check if prefix_sum - k seen before
        if (prefix_sum - k) in prefix_map:
            count += prefix_map[prefix_sum - k]
        # update map
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        print(prefix_map)
    return count

# Example
nums = [1, 2, 3]
k = 3
print(subarraySum(nums, k))  # Output: 2
