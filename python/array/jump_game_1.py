# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.


nums = [2,3,1,1,4]
# nums = [3,2,1,0,4]

n = len(nums)

def jump_game(nums):
    goal = n - 1

    for i in range(n-2, -1, -1):
        if i + nums[i] >= goal:
            goal = i
            print(goal)

    return goal == 0


print(jump_game(nums))