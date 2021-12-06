n, m = map(int, input().split())
x, y, direction = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[0] * m for _ in range(n)]

array[x][y] = 1


