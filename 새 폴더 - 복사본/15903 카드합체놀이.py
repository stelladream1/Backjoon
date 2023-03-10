import heapq
n,m = map(int,input().split())

array = []
array = list(map(int, input().split()))

heapq.heapify(array)

for i in range(m):
    one = heapq.heappop(array)
    two = heapq.heappop(array)
    
    heapq.heappush(array, one+ two)
    heapq.heappush(array, one + two)
    
print(sum(array))