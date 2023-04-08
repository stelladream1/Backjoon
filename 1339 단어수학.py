import sys

maxi = 100000000000

input = sys.stdin.readline

n = int(input())
array = []
for i in range(n):
    array.append(input().strip())
dic = {}
for i in array:
    root = len(i) -1 
    for j in i:
        if j in dic:
            dic[j] = dic[j] + pow(10, root)
        else:
            dic[j ] = pow(10,root)
        root = root - 1

dic = sorted(dic.values(), reverse=True)

result = 0 
num = 9

for i in dic:
    result = result + num * i
    num = num -1

print(result)
