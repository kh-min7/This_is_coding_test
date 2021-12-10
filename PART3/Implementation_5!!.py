n = int(input())
k = int(input())

array = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, input().split())
    array[a][b] = 1

l = int(input())
move = []
for _ in range(l):
    x, c = input().split()
    move.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

