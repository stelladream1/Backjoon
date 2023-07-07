import heapq

INF = int(1e9)

n, m = map(int, input().split())
graph = [ [] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n + 1 )
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append( (b,c) )
    graph[b].append( (a, c))


def dijkstra(start):
    q = []
    visited[start] = True
    distance[start] = 0

    heapq.heappush(q, (0,start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, ( cost, i[0]))
dijkstra(1)
print(distance[n])