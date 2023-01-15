import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

m = int(input())
count = 0
array.sort()
start = 0
end = n - 1
while start < end:

    mid = array[start] + array[end]

    if mid == m:
        count = count + 1
        start = start + 1
    elif mid > m:
        end = end - 1
    else:
        start = start + 1

print(count)
