import sys
days = int(input())
array = list(map(int,input().split()))

min_value = array[0]
result = 0

for i in range(1,days):
    if min_value < array[i]:
        result = max(result, array[i]-min_value)
    else:
        min_value = array[i]
print(result)