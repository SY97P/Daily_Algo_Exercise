#4 -> 5

n = int(input())
# n = 4

dp = [1, 1]

for i in range(2, n + 1) : 
	dp.append((dp[i-2] + dp[i-1])%15746)

print(dp[n])