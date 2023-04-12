file = open("./Daily_Algo_Exercise/이코테/기출/dbfs/인구이동.txt")

input = file.readline 

from collections import deque

n, l, r = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(i, j, index):
	q = deque([(i, j)])
	united = [(i, j)]
	summary = matrix[i][j]
	count = 1
	union[i][j] = index
	while q:
		i, j = q.popleft()
		for dx, dy in d:
			di = i + dx 
			dj = j + dy 
			if 0 <= di < n and 0 <= dj < n and union[di][dj] == -1:
				if l <= abs(matrix[di][dj] - matrix[i][j]) <= r:
					union[di][dj] = index
					united.append((di, dj))
					summary += matrix[di][dj]
					count += 1
					q.append((di, dj))
	for x, y in united:
		matrix[x][y] = summary // count
	return count

answer = 0
while True:
	union = [[-1] * n for _ in range(n)]
	index = 0
	for i in range(n):
		for j in range(n):
			if union[i][j] == -1:
				bfs(i, j, index)
				index += 1
	if index == n*n:
		break
	answer += 1

print(answer)

file.close()