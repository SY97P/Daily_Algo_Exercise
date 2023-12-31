file = open("./Daily_Algo_Exercise/이코테/기출/다이나믹/금광.txt")

input = file.readline

t = int(input())
for tc in range(t):
	n, m = map(int, input().split())
	line = list(map(int, input().split()))
	matrix = [[0] * m for _ in range(n)]
	dp = [[0] * m for _ in range(n)]
	for i in range(len(line)):
		matrix[i//m][i%m] = line[i]

	for i in range(n):
		dp[i][0] = matrix[i][0]

	for j in range(1, m):
		for i in range(n):
			for k in range(-1, 2):
				if 0 <= i+k < n:
					dp[i][j] = max(dp[i][j], dp[i+k][j-1] + matrix[i][j])

	answer = 0
	for i in range(n):
		answer = max(answer, dp[i][-1])

	print(answer)


file.close()