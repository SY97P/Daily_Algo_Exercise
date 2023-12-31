# 1
# 3
# 0
# 13

file = open('./백준/알분류/dp/파이프옮기기1.txt')

input = file.readline 


def solve():
	for i in range(1, n):
		for j in range(1, n):
			if 0 <= i-1 < n and 0 <= j-1 < n and matrix[i][j-1] == 0 and matrix[i-1][j] == 0 and matrix[i-1][j-1] == 0:
				dp[i][j][2] = sum(dp[i-1][j-1])
			if 0 <= j-1 < n and matrix[i][j-1] == 0:
				dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
			if 0 <= i-1 < n and matrix[i-1][j] == 0:
				dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
	print(sum(dp[-1][-1]))


for _ in range(4):
	n = int(input())
	matrix = [list(map(int, input().split())) for _ in range(n)]

	if matrix[-1][-1] == 1:
		print(0)
	else:
		# 0 - 가로 / 1 - 세로 / 2 - 대각
		dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
		dp[0][1][0] = 1
		for i in range(2, n):
			if matrix[0][i] == 0:
				dp[0][i][0] = dp[0][i-1][0]

		solve()


file.close()