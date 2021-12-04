n = int(input())
a = input().split()

x, y = 1, 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

move = ['U', 'D', 'L', 'R']

for direction in a:
    for i in range(len(move)):
        if move[i] == direction:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)
