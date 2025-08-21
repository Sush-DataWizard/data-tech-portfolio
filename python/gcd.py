
def gcd(A, B):
    while B != 0:
        A,B = B,A%B        
    return A

A = 3
B = 6
print("main-op",gcd(A,B))