# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

 

# Example 1:

# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]



class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False

        self.nums.append(val)
        self.val_to_index[val] = len(self.nums) - 1        
        return True

    def remove(self, val: int) -> bool:
        if val in self.val_to_index:
            index = self.val_to_index[val]
            last_num = self.nums[-1]
            self.nums[index] = last_num
            self.val_to_index[last_num] = index
            self.nums.pop()
            del self.val_to_index[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.nums)

obj = RandomizedSet()

aa = obj.insert(1)
print(aa)

bb = obj.insert(1)
print(bb)

# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


