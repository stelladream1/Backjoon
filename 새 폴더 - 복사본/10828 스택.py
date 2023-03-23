import sys
n = int(sys.stdin.readline())
stack = []
for i in range(n):
    cmd = sys.stdin.readline().split()
    run = cmd[0]

    if run == 'push':
        stack.append(cmd[1])

    elif run == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

    elif run == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif run == 'size':
        print(len(stack))

    elif run == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
