# 14

file = open("./백준/dp/lv1/평범한배낭.txt", "r")

input = file.readline

def knapsack() : 
	for i in range(1, n + 1) :
		for j in range(1, k + 1) : 
			if items[i][0] <= j : 
				dp[i][j] = max(dp[i-1][j], items[i][1] + dp[i-1][j-items[i][0]])
			else : 
				dp[i][j] = dp[i-1][j]

	return dp[-1][-1]

n, k = map(int, input().split())

items = [[]] + [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

print(knapsack())

file.close()