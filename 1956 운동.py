import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize


n,m = map(int,input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])
answer = INF

for i in range(1,n+1):
    answer = min(answer, graph[i][i])
if answer !=INF:
    print(answer)
else:
    print(-1)
