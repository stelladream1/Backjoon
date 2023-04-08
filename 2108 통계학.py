import sys
from collections import Counter
input = sys.stdin.readline

array = []
n = int(input())

for i in range(n):
    array.append(int(input()))

array.sort()
temp = []
result = 0

print(round(sum(array) / n))

print(array[n // 2])

cnt = Counter(array).most_common(2)

if n> 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])

else:
    print(cnt[0][0])
print(max(array) - min(array))
