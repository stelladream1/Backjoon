import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize


n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][b]!=0 or (graph[a][k] !=0 and graph[k][b]!=0) :
                graph[a][b] = 1

for i in graph:
    print(*i)