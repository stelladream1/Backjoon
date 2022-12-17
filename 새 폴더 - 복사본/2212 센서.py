import heapq
n = int(input())
k = int(input())

array = list(map(int,input().split()))
temp = []
array.sort()
for i in range(1,n):
    temp.append(array[i]- array[i-1])

temp.sort(reverse=True)
count = 0
for i in temp[:]:
    count = count + 1
    if count == k:
        break
    else:
        temp.remove(i)
  
print(sum(temp))
