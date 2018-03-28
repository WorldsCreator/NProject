def nextEqual(r, k):
    try:
        if r[k] == r[k + 1]:
            return 1 + nextEqual(r, k + 1)
        else:
            return 1
    except IndexError:
        return 1

n = int(input())
a = input().split(' ')
res = nextEqual(a, 0)
ch = a[0]
for i in range(n):
    num = nextEqual(a, i)
    if num > res:
        res = num
        ch = a[i]
print(ch + ' ' + str(res))
