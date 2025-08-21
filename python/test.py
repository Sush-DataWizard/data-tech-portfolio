def solve(A, B):
    n = len(A)
    cs = sum(A[0:B]) 
    ms = cs

    for i in range(1,B+1):
        cs = cs - A[B-i] + A[-i]
        ms = max(cs,ms)

    return ms


A = [5, -2, 3 , 1, 2]
B = 3

print(solve(A,B))
