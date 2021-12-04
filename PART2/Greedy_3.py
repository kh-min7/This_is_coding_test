n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_est = min(data)
    result = max(result, min_est)

print(result)