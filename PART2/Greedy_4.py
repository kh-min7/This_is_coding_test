import time
start_time = time.time() # 측정 시작

n, k = map(int, input().split())
cnt = 0

while n != 1:
    if n % k == 0:
        n /= k
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)


end_time = time.time() # 측정 종료
print("time: ", end_time - start_time) # 수행 시간 출력