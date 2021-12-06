n = input()

mid = len(n) // 2

ans = 0

for i in range(mid):
    ans += int(n[i])
    ans -= int(n[-1-i])

if ans == 0:
    print("LUCKY")
else:
    print("READY")