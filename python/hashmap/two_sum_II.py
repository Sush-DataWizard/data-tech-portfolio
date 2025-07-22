def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []  # no solution (though problem guarantees one)


numbers = [2,3,4]
target = 6

print(twoSum(numbers, target))