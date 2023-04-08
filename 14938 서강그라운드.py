import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize


n,m,r = map(int, input().split())

temp = list(map(int, input().split()))
graph = [[INF] * (n+1) for i in range(n+1)]

for _ in range(r):
    a,b,c =map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c


for a in range(1,n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
result = 0


for j in range(1,n+1):
    array = graph[j][1:]
    answer = 0
    for i in range(n):
        if array[i] <=m :
            answer = answer + temp[i]
    result = max(result, answer)
print(result)