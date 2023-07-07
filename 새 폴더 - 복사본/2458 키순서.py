import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize


n,m = map(int,input().split())

graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1

for a in range(1,n+1):
    for b in range(1, n+1):
        if a ==b :
            graph[a][b] = 0


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1, n+1):
            if graph[a][b] ==1 or (graph[a][k]==1 and graph[k][b]==1):
                graph[a][b] = 1
answer = 0

for a in range(1,n+1):
    result = 0
    for b in range(1, n+1):
        result = result + graph[a][b] + graph[b][a]
    if result == n-1:
        answer = answer + 1
print(answer)
