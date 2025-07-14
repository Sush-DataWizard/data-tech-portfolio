def Ransom_Note():

    from collections import Counter
    ransomNote = "a"
    magazine = "b"
        
    ransom_count = Counter(ransomNote)
    print("r : ",ransom_count)

    magazine_count = Counter(magazine)
    print("m : ",magazine_count)

    for char in ransom_count:
        print(char)
        print(ransom_count[char])
        print(magazine_count.get(char, 0))
        if ransom_count[char] > magazine_count.get(char, 0):
            return False
    return True


print(Ransom_Note())