from collections import deque

n = int(input())
dx = [-1, 1, -1, 1, 2, -2, -2, 2]
dy = [2, 2, -2, -2, 1, 1, -1, -1]


for _ in range(n):
    graph = []
    m = int(input())
    graph = [[0] * m for _ in range(m)]
    x, y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    graph[x][y] = 1

    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        if x == end_x and y == end_y:
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

    print(graph[end_x][end_y]-1)
