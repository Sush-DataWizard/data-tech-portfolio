def substring_with_concat():
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    
    from collections import Counter

    word_len = len(words[0])
    print(word_len)
    total_len = word_len * len(words)
    print(total_len)
    word_count = Counter(words)
    print(word_count)
    result = []

    for i in range(len(s) - total_len + 1):
        seen = {}
        for j in range(0, total_len, word_len):
            word = s[i + j:i + j + word_len] 
            print(word)
            if word in word_count:
                seen[word] = seen.get(word, 0) + 1
                print(seen)
                if seen[word] > word_count[word]:
                    break
            else:
                break
        if len(seen) == len(word_count):
            result.append(i)

    return result

print(substring_with_concat())