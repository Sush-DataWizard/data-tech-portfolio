
def longest_increasing_subarray(lst):
    if not lst:
        return []

    max_lenth = 1
    current_length = 1
    start = 0
    max_start = 0

    for i in range(1,len(lst)):
        if lst[i] >= lst[i-1]:
            current_length += 1
        else:
            if current_length > max_lenth:
                max_lenth = current_length
                max_start = start

            current_length = 1  
            start = i

    return lst[max_start:max_start+max_lenth]

# Example usage
lst = [1, 3, 2, 4, 5, 6, 4, 7, 8]
result = longest_increasing_subarray(lst)
print("Longest increasing contiguous subarray:", result)

print(len(result))
