from collections import deque

n = int(input())
k = int(input())

graph = [[] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)


def dfs(start):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
    return sum(visited) - 1


print(dfs(1))
