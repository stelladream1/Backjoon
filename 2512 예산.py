import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
array = list(map(int,input().split()))
m =  int(input())

start = 0
end = max(array)
while start <=end:
    mid = (start + end ) // 2
    total = 0
    for i in array:
        if i > mid:
            total = total + mid
        else:
            total = total + i

    if total <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
#print(min(start, mid, end))