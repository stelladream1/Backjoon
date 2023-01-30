import heapq

from collections import deque

import sys

input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())  # 가로 세로
graph = [[] * m for _ in range(n)]
for i in range(n):
    a = input().strip()
    graph[i] = list(a)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y,cnt):
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    q = deque([(x, y,cnt)])
    result = -1
    while q:
        x, y,cnt = q.popleft()

        if result < cnt:
            result = cnt
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 'L' and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append([nx, ny, cnt+1])
                    
    return result

result = -1
for i in range(n):
    for j in range(m):
        if graph[i][j] =='L':

            result = max(result, bfs(i, j,0))
print(result)
