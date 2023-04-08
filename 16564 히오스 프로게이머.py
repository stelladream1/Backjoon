import sys
from collections import Counter
input = sys.stdin.readline

n,m = map(int,input().split())
array = []
for i in range(n):
    array.append(int(input()))
result = 0
start = min(array)
end = min(array) + m
while start <=end:
    mid = (start + end ) // 2
    total = 0
    for i in array:
        if i < mid:
            total = total + (mid-i)

    if total <= m:
        start = mid + 1
        result = max(result,mid)
    else:
        end = mid - 1

print(result)