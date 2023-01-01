import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = list(map(int, sys.stdin.readline().split()))

neg = []
pos = []
maxi = max(abs(min(array)), max(array))
           
for i in array:
    if i > 0:
        pos.append(i)
    else:
        neg.append(abs(i))

pos.sort(reverse=True)
neg.sort(reverse=True)
result = 0

for i in range(len(neg)):
    if i % m == 0:
        result = result + neg[i] * 2

for i in range(len(pos)):
    if i % m == 0:
        result = result + pos[i] * 2


