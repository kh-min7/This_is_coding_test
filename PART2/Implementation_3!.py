n, m = map(int, input().split())
x, y, direction = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[0] * m for _ in range(n)]

array[x][y] = 1

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_count = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if array[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_count = 0
        continue

    else:
        turn_count += 1

    if turn_count == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
             x = nx
             y = ny
        else:
            break

        turn_count = 0

print(count)