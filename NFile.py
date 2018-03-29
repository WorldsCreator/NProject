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
i = 1
while i < n:
    num = nextEqual(a, i)
    if num > res:
        res = num
        ch = a[i]
    i += num
print(ch + ' ' + str(res))
