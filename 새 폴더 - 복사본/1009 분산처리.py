array = [[10], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6],
              [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]

def func(a,b):
    a = a % 10
    b = b % len(array[a])
    return array[a][b-1]

for i in range(int(input())):
    a,b = map(int,input().split())

    print(func(a,b))