# with 0 and 1 

a = [0,1,0,1,0,1,0,1,0,1,0,1]

L = 0
R = len(a) - 1
# print(L,R)

while L <= R:
    print(L,R)
    if a[L] == 0:
        L += 1
    elif a[R] == 1:
        R -= 1
    else:
        a[L], a[R] = a[R], a[L]
        L += 1
        R -= 1

print(a)


# with random Number

a = [1,5,2,6,9,3,7,2,7]

n = len(a)
for i in range(n):
    for j in range(1, n-i):
        if a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]

print(a)