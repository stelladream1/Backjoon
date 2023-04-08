n = int(input())
sum = 0
for i in range(1,n):
    sum = sum + i
    if sum > n:
        print(i-1)
        break
