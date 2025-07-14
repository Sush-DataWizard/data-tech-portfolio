
from collections import Counter
from collections import defaultdict

def groupAnagrams():

    strs = ["eat","tea","tan","ate","nat","bat"]

    anagrams = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        print(key, word)
        anagrams[key].append(word)

    print(anagrams)
    return list(anagrams.values())

print(groupAnagrams())