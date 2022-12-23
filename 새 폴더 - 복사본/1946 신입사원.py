import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    count = 1
    m = int(input())
    array = []
    for _ in range(m):
        array.append(list(map(int,input().split())))

    array.sort()
    first = array[0][1]

    for i in range(1,m):
        if array[i][1] < first:
            first = array[i][1]
            count = count + 1

    print(count)
