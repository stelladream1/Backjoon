import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
m = int(input())
temp = list(map(int, input().split()))
array.sort()


def binary(i):
    first = 0
    end = n - 1

    while first <= end:
        mid = (first + end) // 2
        if array[mid] == i:
            return True
        if i < array[mid]:
            end = mid - 1
        elif i > array[mid]:
            first = mid + 1


for i in range(m):
    if binary(temp[i]):
        print(1)
    else:
        print(0)