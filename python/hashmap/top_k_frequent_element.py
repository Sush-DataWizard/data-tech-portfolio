from collections import Counter

def topKFrequent(nums, k):
    freq = Counter(nums)
    bucket = [[] for _ in range(len(nums)+1)]

    for num, count in freq.items():
        bucket[count].append(num)

    res = []
    for i in range(len(bucket)-1, 0, -1):  # from high freq to low
        print(i)
        for num in bucket[i]:
            res.append(num)
            if len(res) == k:
                return res

# Example
nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))  # Output: [1, 2]
