import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    result = 0
    m = int(input())
    array = list(map(int, input().split()))
    array.sort()

    for i in range(2, m):
        result = max(result , abs(array[i] - array[i-2]))

    print(result)
