# 1 -> 9
# 2 -> 17

n = int(input())

# n = 4

dp = [[0 for _ in range(10)] for _ in range(n + 1)]

dp[1] = [0] + [1] * 9

for i in range(2, n + 1) : 
	for j in range(10) :
		if j != 0 : 
			dp[i][j] += dp[i-1][j-1]
		if j != 9 : 
			dp[i][j] += dp[i-1][j+1]
		dp[i][j] %= 1000000000

# for d in dp : 
# 	print(d, sum(d))

print(sum(dp[n])%1000000000)