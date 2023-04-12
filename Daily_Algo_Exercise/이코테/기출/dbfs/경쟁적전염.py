file = open("./Daily_Algo_Exercise/이코테/기출/dbfs/경쟁적전염.txt")

input = file.readline 

from collections import deque

n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

def bfs():
	d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	q = deque([])

	for l in range(1, k+1):
		for i in range(n):
			for j in range(n):
				if matrix[i][j] == l:
					q.append((i, j, l, 0))

	while q:
		i, j, vir, sec = q.popleft()
		if sec >= s:
			break

		for dx, dy in d:
			di = i + dx
			dj = j + dy
			if 0 <= di < n and 0 <= dj < n and matrix[di][dj] == 0:
				matrix[di][dj] = vir
				q.append((di, dj, vir, sec+1))

	return matrix[x-1][y-1]
	

answer = bfs()
print(answer)


file.close()