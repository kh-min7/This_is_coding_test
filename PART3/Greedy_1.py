n = int(input())

people = list(map(int, input().split()))

people.sort()

result = 0
cnt = 0

for i in people:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0

print(result)

