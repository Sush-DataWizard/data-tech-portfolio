def twoSum():

    nums = [2,7,11,15]
    target = 9
    
    hashmap = {} 

    for i, num in enumerate(nums):
        print(i, num)
        
        c = target - num
        if c in hashmap:
            return [hashmap[c], i]
        hashmap[num] = i

print(twoSum())