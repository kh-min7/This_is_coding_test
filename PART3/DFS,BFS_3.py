n, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

