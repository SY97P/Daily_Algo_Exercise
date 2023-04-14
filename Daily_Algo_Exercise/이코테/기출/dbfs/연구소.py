file = open("./Daily_Algo_Exercise/이코테/기출/dbfs/연구소.txt")

input = file.readline


n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
temp = [[0] * m for _ in range(n)]

answer = 0

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def get_score(temp):
	result = 0
	for i in range(n):
		for j in range(m):
			if temp[i][j] == 0:
				result += 1
	return result 

def virus(i, j):
	for dx, dy in d:
		di = i + dx 
		dj = j + dy 
		if 0 <= di < n and 0 <= dj < m and temp[di][dj] == 0:
			temp[di][dj] = 2
			virus(di, dj)

def dfs(count):
	global answer
	
	if count == 3:
		for i in range(n):
			for j in range(m):
				temp[i][j] = int(matrix[i][j])
		for i in range(n):
			for j in range(m):
				if temp[i][j] == 2:
					virus(i, j)
		answer = max(answer, get_score(temp))
		return
	for i in range(n):
		for j in range(m):
			if matrix[i][j] == 0:
				matrix[i][j] = 1
				dfs(count + 1)
				matrix[i][j] = 0


dfs(0)

print(answer)


file.close()