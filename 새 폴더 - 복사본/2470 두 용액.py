import sys

maxi = 100000000000

input = sys.stdin.readline

n = int(input())

array = list(map(int, sys.stdin.readline().split()))
array.sort()
start = 0
end = n-1

while start < end:
    mid = (array[start] + array[end])
    if abs(mid) < maxi:
        maxi = abs(mid)
        result = [array[start], array[end]]
    if mid < 0 :
        start = start + 1
    elif mid > 0:
        end = end - 1
    else:
        break

print(result[0], result[1])