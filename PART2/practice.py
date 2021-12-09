from collections import deque

n, m, v = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))
