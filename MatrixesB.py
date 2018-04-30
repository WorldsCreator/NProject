n, m = map(int, input().split())
a = [[None] * m for i in range(n)]
for i in range(n):
    a[i] = input().split()
print(a[::-1])
