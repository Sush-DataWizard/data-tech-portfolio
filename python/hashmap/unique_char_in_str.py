from collections import Counter

def firstUniqChar(s: str) -> int:
    # Step 1: Count frequency of each character
    freq = Counter(s)
    
    # Step 2: Find the first char with frequency 1
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1

# Examples
print(firstUniqChar("leetcode"))      # Output: 0
print(firstUniqChar("loveleetcode"))  # Output: 2
print(firstUniqChar("aabb"))          # Output: -1
