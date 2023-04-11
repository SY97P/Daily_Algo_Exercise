file = open('./Daily_Algo_Exercise/이코테/기출/dbfs/연구소.txt')

input = file.readline 

from collections import deque
from copy import deepcopy

def bfs(matrix):
	temp = deepcopy(matrix)
	d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	q = deque([])
	for i in range(n):
		for j in range(m):
			if temp[i][j] == 2:
				q.append((i, j))
	while q: 
		i, j = q.popleft()
		for dx, dy in d:
			di = i + dx
			dj = j + dy
			if 0 <= di < n and 0 <= dj < m and temp[di][dj] == 0:
				temp[di][dj] = 2
				q.append((di, dj))

	count = 0
	for i in range(n):
		for j in range(m):
			if temp[i][j] == 0:
				count += 1
	return count

def dfs(count):
	global answer 
	if count >= 3:
		# for mat in matrix:
		# 	print(mat)
		# print()
		answer = max(answer, bfs(matrix))
		return
	for i in range(n):
		for j in range(m):
			if matrix[i][j] == 0:
				matrix[i][j] = 1
				dfs(count+1)
				matrix[i][j] = 0
	

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

answer = 0

dfs(0)

print(answer)


file.close()