import sys
from collections import deque


input = sys.stdin.readline

n,m = map(int,input().split())

graph = []
res = 0
for i in range(m):
    graph.append(list(map(int,input().split())))
queue = deque([])


dx = [0,0,-1,1]
dy = [-1,1,0,0]

for i in range(m):
    for j in range(n):
        if graph[i][j]==1:
            queue.append([i,j])

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= m or nx < 0 or ny <0 or ny >=n:
                continue
            if graph[nx][ny]== 0:
                queue.append([nx,ny])
                graph[nx][ny] = graph[x][y] + 1

bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)