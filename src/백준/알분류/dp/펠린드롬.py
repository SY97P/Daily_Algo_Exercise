# 1
# 0
# 1
# 1

file = open("./펠린드롬.txt")

input = file.readline

n = int(input())
a = [0] + list(map(int, input().split()))
m = int(input())

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][i] = 1
    dp[i-1][i] = 1 if a[i-1] == a[i] else 0

for i in range(n-1, 0, -1):
    for j in range(i+2, n+1):
        dp[i][j] = 1 if a[i] == a[j] and dp[i+1][j-1] else 0

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s][e])

file.close()