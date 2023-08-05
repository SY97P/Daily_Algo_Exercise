# 10

file = open("./백준/dp/lv2/동전1.txt", "r")

input = file.readline

def solve(k) : 
	for coin in coins : 
		if coin > k : 
			break
		dp[coin] += 1
		for i in range(coin + 1, k + 1) :
			dp[i] += dp[i - coin]
		# print(dp)

	return dp[k]

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()

dp = [0 for _ in range(k + 1)]
dp[0] = 1

print(solve(k))

file.close()