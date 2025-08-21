from math import gcd
from math import isqrt

# function to compute lcm
def lcm(a, b):
    return a * b // gcd(a, b)

# function to find minimal k such that k(k+1)/2 divisible by p
def min_k(p):
    k = 1
    while True:
        if (k * (k + 1) // 2) % p == 0:
            return k
        k += 1

# function to find smallest period of a string
def smallest_period(s):
    n = len(s)
    for i in range(1, n + 1):
        if n % i == 0:
            if s[:i] * (n // i) == s:
                return i
    return n


def stringholics(strings):
    ans = 1
    for s in strings:
        p = smallest_period(s)
        print(p)
        k = min_k(p) 
        print(k)
        ans = lcm(ans, k)
        print(ans)
        print("----------")
    return ans

# Example usage
strings = ["abab"]
# strings = ["abab", "aaaa", "abc"]

print(stringholics(strings))  
