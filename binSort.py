from random import randint

r, x = map(int, input().split(' '))
a = []
for i in range(r):
    a.append(randint(0, r))
print(*a)
a.sort()
print(*a)
l = 0
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

    if r < len(a):
        cl = []
        if x - l > r - x:
            cl.append(r)
            cl.append(a[r])
        else:
            cl.append(r)
            cl.append(a[l])
        print("Nearest: A[{}]={}".format(cl))
    else:
        print("Nearest: A[{}]={}".format(l, a[l]))
