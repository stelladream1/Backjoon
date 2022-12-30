array = input().split('-')


result = 0
for i in range(len(array)):
    result = 0
    if "+" in array[i]:
        temp = array[i].split("+")
        for j in temp:
            result = result + int(j) 
        array[i] = int(result)
    else:
        array[i] = int(array[i])

result = array[0]
for i in range(1,len(array)):
    result = result - array[i]

print(result)