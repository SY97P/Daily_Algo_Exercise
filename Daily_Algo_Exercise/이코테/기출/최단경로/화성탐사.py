file = open("./Daily_Algo_Exercise/이코테/기출/최단경로/화성탐사.txt")

input = file.readline 

import heapq

t = int(input())
for tc in range(t):
	n = int(input())
	matrix = [list(map(int, input().split())) for _ in range(n)]
	dp = [[int(1e9)] * n for _ in range(n)]
	d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

	def bfs():
		dp[0][0] = matrix[0][0]
		q = [(dp[0][0], 0, 0)]
		heapq.heapify(q)

		while q:
			cost, i, j = heapq.heappop(q)

			if cost > dp[i][j]:
				continue

			for dx, dy in d:
				di = i + dx
				dj = j + dy 
				if 0 <= di < n and 0 <= dj < n and dp[i][j] + matrix[di][dj] < dp[di][dj]:
					dp[di][dj] = dp[i][j] + matrix[di][dj]
					heapq.heappush(q, (dp[dx][dy], di, dj))
					
		return dp[-1][-1]

	answer = bfs()
	print(answer)

file.close()