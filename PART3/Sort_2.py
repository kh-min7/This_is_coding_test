n = int(input())

array = list(map(int, input().split()))
ans = []
tmp = 0

for i in range(1, max(array) + 1):
    for j in range(n):
        tmp += abs(array[j] - i)
    ans[i] = tmp

print(max(ans))
