def isHappy():

    n = 19
    seen = set()

    while n != 1:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    
    return True

print(isHappy())