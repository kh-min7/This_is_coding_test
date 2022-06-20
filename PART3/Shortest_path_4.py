import heapq, sys
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append((b, 1))
  graph[b].append((a, 1))

start = 1

def dik(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for ndist, nnow in graph[start]:
      cost = dist + ndist
      if cost < distance[nnow]:
        distance[nnow] = cost
        heapq.heappush(q, (cost, nnow))
       
dik(start)

max_node = 0
max_distance = 0

result = []

for i in range(1, n + 1):
  if max_distance < distance[i]:
    max_distance = distance[i]
    max_node = i
    result = [max_node]
  elif max_distance == distance[i]:
    result.append(i)

print(max_node, max_distance, len(result))