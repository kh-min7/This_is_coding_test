n, m = map(int, input().split())

a = list(map(int, input().split()))

cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] != a[j]:
            cnt += 1
        print(a[i], a[j])

print(cnt)

# 더 효율적인 방법 생각하기