from collections import deque
import math

n, l, r = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

count = 0


def bfs(x, y):
    visited[x][y] = 1
    queue = deque([(x, y)])
    temp = [[x, y]]
    result = graph[x][y]
    global Flag
    global count
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                    temp.append([nx, ny])
                    result = result + graph[nx][ny]

    if len(temp) > 1:
        for i, j in temp:
            Flag = True
            graph[i][j] = math.trunc(result / len(temp))


while True:
    Flag = False
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i, j)

    if Flag == True:
        count = count + 1
    else:
        break
print(count)
