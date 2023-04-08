import sys

x = int(input())


dp = [[0] * 15 for _ in range(15)]


for i in range(15):
    dp[0][i] = i+1

for i in range(1,15):
    for j in range(15):
        dp[i][j] =sum(dp[i-1][:j+1])

for _ in range(x):
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    print(dp[n][m-1])