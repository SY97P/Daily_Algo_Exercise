file = open("./Daily_Algo_Exercise/이코테/기출/다이나믹/금광.txt")

input = file.readline

t = int(input())
for tc in range(t):
	n, m = map(int, input().split())
	matrix = [[0] * m for _ in range(n)]
	line = list(map(int, input().split()))
	for i in range(len(line)):
		matrix[i//m][i%m] = line[i]

	dp = [[0] * m for _ in range(n)]
	for i in range(n):
		dp[i][0] = matrix[i][0]

	d = [(-1, 1), (0, 1), (1, 1)]

	for j in range(m-1):
		for i in range(n):
			for dx, dy in d:
				di = i + dx
				dj = j + dy
				if 0 <= di < n and dp[di][dj] < dp[i][j] + matrix[di][dj]:
					dp[di][dj] = dp[i][j] + matrix[di][dj]

	answer = 0
	for i in range(n):
		answer = max(answer, dp[i][-1])
	print(answer)
	
file.close()