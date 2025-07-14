def word_pattern():

    pattern = "abba"
    s = "dog cat cat dog"

    words = s.split()
    if len(words) != len(pattern):
        return False

    char_to_word = {}
    word_to_char = {}

    for a,b in zip(pattern, words):
        if a in char_to_word:
            if char_to_word[a] != b:
                return False
        else:
            if b in word_to_char:
                return False
            char_to_word[a] = b
            word_to_char[b] = a


    return True


print(word_pattern())