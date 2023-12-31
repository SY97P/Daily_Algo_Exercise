n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (i+1) for i in range(n)]
dp[0][0] = matrix[0][0]

for i in range(n-1):
	for j in range(i+1):
		dp[i+1][j] = max(dp[i+1][j], dp[i][j] + matrix[i+1][j])
		dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + matrix[i+1][j+1])

print(max(dp[-1]))