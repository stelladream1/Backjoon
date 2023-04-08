import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1
count = 0


def dfs(v):
    visited[v] = 1

    for i in range(1, n + 1):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i)

dfs(1)
print(sum(visited)-1)

import sys
sys.setrecursionlimit(10**7)
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
count = 0
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1
