def longest_substring():
    s = "abcabcbb"
    char_set = set()

    print(char_set)
    # s = "abcabcbb"
    # s = "bbbbb"
    # s = "pwwkew"
    
    left = 0
    max_len = 0

    for right in range(len(s)):

        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1 

        char_set.add(s[right])

        max_len = max(max_len, right - left + 1)
    
    return max_len, char_set

print(longest_substring())