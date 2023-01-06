import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(sys.stdin.readline().strip())

visited = [[0] * m for _ in range(n)]
count = 0


def bfs(x, y):
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        if graph[x][y] == '-':
            if y+1 < m and graph[x][y+1] == '-' and visited[x][y+1] == 0:
                visited[x][y+1] = 1
                q.append((x, y+1))

        elif graph[x][y] == '|':
            if x+1 < n and graph[x+1][y] == '|' and visited[x+1][y] == 0:
                visited[x+1][y] = 1
                q.append((x+1, y))

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            bfs(i, j)
            count = count+1
print(count)
