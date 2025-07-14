
# Integers are in the range of 1 to n
# No Duplicate


nums1 = [1,2,3,4,6]
n = len(nums1)


total = (n + 1) * (n + 2) // 2
sum_of_L = sum(nums1)

print(total-sum_of_L)



# Question 2 
# Integers are in the range of 1 to n

nums = [2, 3, 5, 6]
a = 2
b = 6

expected_total = (b - a + 1) * (a + b) // 2
actual_sum = sum(nums)
missing = expected_total - actual_sum
