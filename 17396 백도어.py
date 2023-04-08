import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())

ward = list(map(int, input().split()))
ward[-1] = 0
graph = [[] for i in range(n)]
distance = [INF] * n
for i in range(m):
    a, b, c = map(int, input().split())

    if ward[a] or ward[b]:
        continue
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstar(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue
        for next_cost, next_node in graph[now]:
            cost = dist + next_node
            if cost < distance[next_cost]:
                distance[next_cost] = cost
                heapq.heappush(q, (cost, next_cost))

dijkstar(0)
if distance[n-1] != INF:
    print(distance[n-1])
else:
    print(-1)