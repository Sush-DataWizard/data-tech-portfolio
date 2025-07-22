def findDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num  # duplicate found
        seen.add(num)
    return -1  # should never happen if input is valid

# Example
nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))  # Output: 2
