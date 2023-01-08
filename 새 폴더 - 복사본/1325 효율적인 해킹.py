# import sys
# from collections import deque



# def bfs(v):
#     global count
#     count = 0
#     q = deque([v])
#     visited = [0] * (n + 1)
#     visited[v] = 1
#     while q:
#         v = q.popleft()
#         for i in graph[v]:
#             if visited[i] == 0:
#                 q.append(i)
#                 visited[i] = 1
#                 count = count + 1


# n, m = map(int, sys.stdin.readline().split())

# graph = [[] for _ in range(n + 1)]
# for _ in range(m):
#     x, y = map(int, sys.stdin.readline().split())
#     graph[y].append(x)

# array = []

# for i in range(1, n + 1):
#     bfs(i)
#     array.append(count)

# maxi = max(array)
# for i in range(len(array)):
#     if array[i] == maxi:
#         print(i+1, end=" ")

import sys
from collections import deque



def bfs(v):
    global count
    count = 0
    q = deque([v])
    visited = [0] * (n + 1)
    visited[v] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                count = count + 1


n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[y].append(x)

array = []

for i in range(1, n + 1):
    bfs(i)
    array.append([i, count])


maxi = array[0][1]
for i in array:
    if i[1] == maxi:
        print(i[0], end=" ")