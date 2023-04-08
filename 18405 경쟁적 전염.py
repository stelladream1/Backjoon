from collections import deque

n , m  =  map(int, input().split(" "))
array = []
temp = []

for i in range(n):
    array.append(list(map(int,input().split(" "))))
    for j in range(n):
        if array[i][j] !=0:
            temp.append((array[i][j], i ,j,0))
temp.sort()

sec ,last_x , last_y= map(int, input().split(" "))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

q = deque(temp)

while q:
    virus, x, y , time = q.popleft()

    if time== sec:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=n:
            continue

        if array[nx][ny] == 0:
            array[nx][ny] = virus
            q.append((virus, nx, ny, time + 1))


print(array[last_x-1][last_y-1])
