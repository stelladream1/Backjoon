from collections import deque

import sys

input = sys.stdin.readline


def bfs():
    queue = deque([(home_x, home_y)])

    while queue:
        x, y = queue.popleft()

        if abs(x - fes_x) + abs(y - fes_y) <= 1000:
            return True
        for i in range(gs_n):
            if not visited[i]:
                gs_x, gs_y = gs[i]
                if abs(x - gs_x) + abs(y - gs_y) <= 1000:
                    queue.append([gs_x, gs_y])
                    visited[i] = True

    return False


N = int(input())

for _ in range(N):
    gs_n = int(input())
    gs = []
    home_x, home_y = map(int, input().split())
    for _ in range(gs_n):
        x, y = map(int, input().split())
        gs.append([x, y])

    visited = [False] * gs_n
    fes_x, fes_y = map(int, input().split())
    if bfs() == True:
        print('happy')
    else:
        print('sad')