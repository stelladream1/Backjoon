n = int(input())
array = [300,60,10]

temp = []
i = 0

for i in array:
    temp.append(n//i)
    n = n % i

if n == 0:
    print(*temp)
else:
    print(-1)