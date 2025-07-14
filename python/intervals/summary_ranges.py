
def summary_ranges(nums):
    result = []
    
    start = nums[0]

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            # End of current range
            end = nums[i - 1]
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}->{end}")
            start = nums[i]  # Start new range

    # Handle the last range
    end = nums[-1]
    if start == end:
        result.append(str(start))
    else:
        result.append(f"{start}->{end}")

    return result


nums = [0,1,2,4,5,7]
print(summary_ranges(nums))