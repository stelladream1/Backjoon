import sys

input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    a = input().strip()
    if a not in array:
        array.append(a)

array.sort()
array.sort(key=lambda x: len(x))

for i in array:
    print(i)