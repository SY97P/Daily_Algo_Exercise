# 96
# 31
# 90 

file = open("./백준/dp/lv2/행렬곱셈순서.txt", "r")

input = file.readline

def solve(n) : 
	for d in range(1, n) : 
		for i in range(n - d) : 
			# 0 < j < n
			# 0 < i + d < n
			# -d (0) < i < n - d
			j = i + d
			dp[i][j] = min([dp[i][k] + dp[k+1][j] + mat[i][0] * mat[k][1] * mat[j][1] for k in range(i, j)])

	return dp[0][-1]

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

print(solve(n))

file.close()