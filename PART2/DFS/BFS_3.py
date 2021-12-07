n, m = map(int, input().split())

array = []

for _ in range(n):
    array.append(list(map(int(input()))))

visited = [[0] * m for _ in range(n)]

def dfs():
