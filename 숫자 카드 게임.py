import sys

n,m = list(map(int,input().split())) 
value = 0
for i in range(n):
    temp = list(map(int,input().split())) 
    value = max(min(temp), value)

print(value)
