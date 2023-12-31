file = open("./SWEA/D3/Knapsack01.txt", "r")

input = file.readline

t = int(input())

for tc in range(1, t + 1) : 
	n, k = map(int, input().split())
	items = [list(map(int, input().split())) for _ in range(n)]

	dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

	for i in range(1, n + 1) : 
		for j in range(1, k + 1) : 
			if items[i-1][0] <= j : 
				dp[i][j] = max(dp[i-1][j], items[i-1][1] + dp[i-1][j-items[i-1][0]])
			else : 
				dp[i][j] = dp[i-1][j]

	# for i in range(n + 1) : 
	# 	for j in range(k + 1) : 
	# 		print(dp[i][j], end = " ")
	# 	print()

	print("#%d %d" %(tc, dp[n][k]))

	
file.close()