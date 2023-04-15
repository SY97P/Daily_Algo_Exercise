file = open("./Daily_Algo_Exercise/이코테/기출/최단경로/화성탐사.txt")

input = file.readline 


import heapq

t = int(input())
for tc in range(t):
	n = int(input())
	matrix = [list(map(int, input().split())) for _ in range(n)]

	dp = [[1e9] * n for _ in range(n)]
	dp[0][0] = matrix[0][0]

	d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

	q = [(dp[0][0], 0, 0)]
	heapq.heapify(q)

	while q:
		c, i, j = heapq.heappop(q)

		if c > dp[i][j]:
			continue

		for dx, dy in d:
			di = i + dx
			dj = j + dy 
			if 0 <= di < n and 0 <= dj < n and c + matrix[di][dj] < dp[di][dj]:
				dp[di][dj] = c + matrix[di][dj]
				heapq.heappush(q, (dp[di][dj], di, dj))
	
	print(dp[-1][-1])


file.close()