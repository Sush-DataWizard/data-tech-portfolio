
# Easy solution is to use SORTED() but 
# SORTED() it takes O(n log n) time.
# But the problem explicitly asks for an O(n) solution, which sorting cannot achieve.

def longest_consecutive(nums):
    num_set = set(nums)
    print(num_set)
    longest = 0

    for num in num_set:
        # only start counting from the beginning of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # count up the streak
            while current_num + 1 in num_set:

                current_num += 1
                current_streak += 1
                print(current_num, current_streak)

            longest = max(longest, current_streak)
            print(longest)

    return longest


nums = [100,4,200,1,3,2]
print(longest_consecutive(nums))