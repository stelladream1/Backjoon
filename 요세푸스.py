n = int(input())
k = int(input())
q = [i for i in range(1, n+1)]
while len(q) > 1:
    for j in range(1,k+1):
        friend = q.pop(0)
        if j !=k:
            q.append(friend)
        print(q)

n = int(input())
k = int(input())
q = [i for i in range(1, n+1)]
j = 0

s = 1

for i in range(1, n+1):
    s = ((s + k -1) % n ) + 1

    n = int(input())
k = int(input())
q = [i for i in range(1, n+1)]
j = 0

def find_the_winner(n,k):
        if n == 1:
                return 1
        return ((find_the_winner(n-1, k) + k -1 ) % n ) + 1

print(find_the_winner(6,2))


n = int(input())
k = int(input())
q = [i for i in range(1, n+1)]
j = 0
while len(q) > 1:
        j = (j + k -1) % len(q)
        q.pop(j)
        print(q)
print(q[0])