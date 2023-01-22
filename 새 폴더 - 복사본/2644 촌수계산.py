from collections import deque

n = int(input())
x, y = map(int, input().split())

m = int(input())
graph = [[] * n for i in range(n + 1)]
visited = [False] * (n + 1)
res = [0] * (n + 1)
for i in range(m):
    a, b, = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(v):
    visited[v] = True
    queue = deque([v])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                res[i] = res[v] + 1


bfs(x)
if res[y] > 0:
    print(res[y])
else:
    print(-1)