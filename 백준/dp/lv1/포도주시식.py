# 33

file = open("./백준/dp/포도주시식.txt", "r")

input = file.readline

n = int(input())

wine = [0] + [int(input()) for _ in range(n)]

dp = [[0, 0, 0], [wine[1], wine[1], wine[1]]] + [[0, 0, 0] for _ in range(n-1)]

for i in range(2, n + 1) :
	dp[i][1] = wine[i] + dp[i-2][0]
	dp[i][2] = wine[i] + dp[i-1][1]
	dp[i][0] = max(dp[i][1], dp[i][2], dp[i-1][0])

print(max(dp[n][0], dp[n-1][0]))

file.close()