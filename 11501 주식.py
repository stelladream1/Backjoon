import heapq
n = int(input())
for j in range(n):
    m = int(input())
    result = 0

    array = list(map(int,input().split()))
    maxi = array[-1]
    temp = []
    for i in range(m-1,-1,-1):
        if array[i] < maxi:
            result = result + (maxi - array[i])
        else:
            maxi = array[i]

    print(result)
