import sys
from collections import Counter
input = sys.stdin.readline

n,m = map(int,input().split())
tree = list(map(int,input().split()))

start = 0
end = max(tree)
while start <=end:
    mid = (start + end) // 2

    total = 0

    for i in tree:
        if i > mid:
            total = total + ( i-mid)
    
    if total < m:
        end = mid-1
    
    else:
        start = mid + 1
        result = mid

print(result)
