
from collections import Counter
from collections import defaultdict

def validAnagrams():

    s = "anagram"
    t = "nagaram"
        
    return Counter(s) == Counter(t)

print(validAnagrams())