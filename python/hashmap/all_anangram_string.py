def findAnagrams(s: str, p: str):
    from collections import Counter
    
    res = []
    k = len(p)

    p_counter = Counter(p)
    s_counter = Counter(s[:k])

    print(p_counter)
    print(s_counter)

    if p_counter == s_counter:
        res.append(0)
    
    for i in range(k, len(s)):
        s_counter[s[i]] += 1

        left_char = s[i - k]
        s_counter[left_char] -= 1 

        if s_counter[left_char] == 0:
            del s_counter[left_char] 

        if s_counter == p_counter:
            res.append(i - k + 1)


    return res


s = "cbaebabacd"
p = "abc"

print(findAnagrams(s,p))