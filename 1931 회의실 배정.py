N = int(input())
array = []
for i in range(N):
    array.append(list(map(int,input().split())))
array = sorted(array, key= lambda x: [x[1],x[0]])
count = 1
end = array[0][1]
for i in range(1,N):
    if end <= array[i][0]:
        count = count + 1
        end = array[i][1]

print(count)