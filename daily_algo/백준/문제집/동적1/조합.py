# 1192052400

file = open("./조합.txt")

input = file.readline

n, m = map(int, input().split())

dp = [[1 for _ in range(n+1)] for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(i+1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

print(dp[-1][-1])

file.close()