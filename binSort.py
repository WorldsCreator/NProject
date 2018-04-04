from random import randint

n, x = map(int, input().split(' '))
a = []
for i in range(n):
    a.append(randint(0, 10))
print(*a)
a.sort()
print(*a)
l = 0
r = n
while l < r - 1:
    c = (l + r) // 2
    if x < a[c]:
        r = c
    else:
        l = c
        if x == c:
            break
if a[l] == x:
    print("A[{}]={}".format(l + 1, x))
else:
    print("Not found")

    try:
        if x - l > r - x:
            print(a[r])
        else:
            print(a[l])
    except IndexError:
        print(a[l])
