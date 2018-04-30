n, m = map(int, input().split())
a = [[None] * n for i in range(m)]
for i in range(n):
    row = input().split()
    for j in range(m):
        a[j][n - i - 1] = row[j]
print()
for i in range(m):
    print(*a[i])
