n = int(input())
coins = list(map(int, input().split()))

coins.sort()

sum = 1
for i in coins:
    if i <= sum:
        sum += i
    else:
        print(sum)