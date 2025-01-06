from collections import deque
from sys import stdin

n = int(stdin.readline().strip())
m = int(stdin.readline().strip())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

queue = deque([1])
visited[1] = True

while queue:
    current = queue.popleft()

    for nxt in graph[current]:
        if not visited[nxt]:
            visited[nxt] = True
            queue.append(nxt)

print(visited.count(True) - 1)
