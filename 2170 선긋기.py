import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())

array= list(tuple(map(int, input().split())) for _ in range(n))

array.sort()
start = array[0][0]
end = array[0][1]
result = 0

for i in range(1,n):
    now_start , now_end = array[i][0] , array[i][1]
    if end >= now_start:
        end = max(end, now_end)

    else:

        result = result + (end-start)
        start, end = now_start , now_end

print(result + (end-start))
