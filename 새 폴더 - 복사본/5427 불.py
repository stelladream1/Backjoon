import heapq

from collections import deque

import sys

input = sys.stdin.readline
INF = sys.maxsize



def bfs(x, y, time):
    queue = deque([(x, y, time)])
    visited[x][y] = True
    cnt = 0
    while queue:
        cnt = cnt + 1
        while fire and fire[0][2] < cnt:
            x, y, time = fire.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == '.' or graph[nx][ny] == '@':
                        graph[nx][ny] = '*'
                        fire.append([nx, ny,time+1])

        while queue and queue[0][2] < cnt:
            x, y, time = queue.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == '.' and visited[nx][ny] == False:
                        visited[nx][ny] = True
                        queue.append([nx, ny, time + 1])
                else:
                    return cnt

    return "IMPOSSIBLE"


N = int(input())
for _ in range(N):
    m, n = map(int, input().split())  # 세로 가로

    graph = [[] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    fire = deque()

    for j in range(n):
        a = input().strip()
        for i in range(len(a)):
            if a[i] == '*':
                fire.append([j, i, 0])
        graph[j] = list(a)

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(n):
        for j in range(m):
            if graph[i][j] == '@':
                print(bfs(i, j, 0))
