from heapq import heappush, heappop
q = []
N = int(input())
for i in range(N):
    heappush(q, (int(input())))

sum = 0
while len(q) > 1:
    temp1 = heappop(q)
    temp2 = heappop(q)
    heappush(q, (temp1+temp2))

    sum += temp1+temp2
print(sum)
