n,m = map(int,input().split())

array = []
array = list(map(int, input().split()))
array.sort()

temp = []
count = 0
for i in array:
    if i not in temp:
        count = count + 1
        for j in range(i, i+m):
            if j not in temp:
                temp.append(j)

print(count)