# I did not understand the question and test case

# Example 1:
#     Input: nums = [3,2,3]
#     Output: 3

# Example 2:
#     Input: nums = [2,2,1,1,1,2,2]
#     Output: 2



nums = [2,2,1,1,1,2,2]

def majorityElement(nums):

    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate

print(majorityElement(nums))


# 2 -> c=0  cn=2 c=1
# 2 -> c=2, cn=2 
# 1 -> c = 1
# 1 -> c = 0
# 1 -> c = 1
# 1 -> c = 2
