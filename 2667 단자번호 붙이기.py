from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
visited = [[False] * n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

count = 0


def bfs(x, y):
    global count
    visited[x][y] = True
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        graph[x][y] = count
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    count = count + 1


temp = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            bfs(i, j)
            temp.append(count+1)
            count = 0

print(len(temp))
temp.sort()
for i in temp:
    print(i)
