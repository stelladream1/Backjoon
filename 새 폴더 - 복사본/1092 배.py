import sys
num = int(input())
crain = []
crane = list((map(int, input().split(" "))))
crane.sort(reverse= True)
count = 0
box = int(input())
box = list((map(int, input().split(" "))))
box.sort(reverse=True)

if max(crane) < max(box):
    print(-1)
else:
    while True:
        if len(box) == 0:
            break
        for i in range(len(crane)):
            for j in range(len(box)):
                if crane[i] >= box[j]:
                    del box[j]
                    break
        count = count + 1
    print(count)
