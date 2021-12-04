n, m, k = map(int, input().split())

a = list(map(int, input().split()))

a.sort()

c = 0
result = 0

for _ in range(m):
    if c < k:
        result += a[-1]
        c += 1
    elif c == k:
        result += a[-2]
        c = 0
    print(result)
print(result)
