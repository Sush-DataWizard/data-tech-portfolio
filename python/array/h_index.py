citations = [3,0,6,1,5]
citations = [1,3,1]

a = sorted(citations, reverse=True)

print(a)
n = len(a)

for i in range(n):
    print(i)
    if a[i] >= i + 1:
        h = i+1
    else:
        break

print(h)