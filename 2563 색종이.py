num = int(input())
array = []
temp = [[0] * 100 for _ in range(100)]
for i in range(num):
    a ,b = (map(int, input().split(" ")))
    for j in range(10):
        for k in range(10):
            temp[a+j][b+k] = 1

result = 0
for i in temp:
    result = result + i.count(1)
print(result)
