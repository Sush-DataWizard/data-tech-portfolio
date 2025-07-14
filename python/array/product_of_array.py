nums = [1,2,3,4]

n = len(nums)
answer = [1] * n

prefix = 1

for i in range(n):
    answer[i] = prefix
    prefix *= nums[i]

print(answer)

suffix = 1

for i in reversed(range(n)):
    answer[i] *= suffix
    suffix *= nums[i]

print(answer)