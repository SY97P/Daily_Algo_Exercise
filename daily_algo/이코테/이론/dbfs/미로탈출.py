from collections import deque

n, m = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(n)]

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs():
	q = deque([(0, 0)])

	while q:
		i, j = q.popleft()

		for dx, dy in d:
			di = i + dx
			dj = j + dy
			if 0 <= di < n and 0 <= dj < m and matrix[di][dj] == 1:
				matrix[di][dj] = matrix[i][j] + 1
				q.append((di, dj))

bfs()

print(matrix[n-1][m-1])