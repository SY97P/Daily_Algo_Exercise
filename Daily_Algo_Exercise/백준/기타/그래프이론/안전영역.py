

file = open("./dfs/안전영역tc.txt", "r")

def dfs(i, j, l) :
	for d in dx :
		di = i + d[0]
		dj = j + d[1]
		if 0 <= di < n and 0 <= dj < n and not visited[di][dj] and matrix[di][dj] > l :
			visited[di][dj] = True
			dfs(di, dj, l)

for _ in range(2) :
	n = int(file.readline())
	matrix = [list(map(int, file.readline().split())) for _ in range(n)]
	answer = int(file.readline())
	file.readline()

	print("n , answer : ", n, answer)
	for mat in matrix : 
		print(mat)

	# logic
	max_level = max(map(max, matrix))
	min_level = min(map(min, matrix))
	max_count = 0
	dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

	for l in range(min_level, max_level) :
		visited = [[False for _ in range(n)] for _ in range(n)]
		count = 0
		
		for i in range(n) : 
			for j in range(n) : 
				if not visited[i][j] and matrix[i][j] > l :
					count += 1
					dfs(i, j, l)

		# print(count)
		max_count = max(max_count, count)
		
	print(max_count)
	print()

file.close()

# 백준 제출용
import sys

def dfs(i, j, l) :
	for d in dx :
		di = i + d[0]
		dj = j + d[1]
		if 0 <= di < n and 0 <= dj < n and not visited[di][dj] and matrix[di][dj] > l :
			visited[di][dj] = True
			dfs(di, dj, l)

n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# logic
max_level = max(map(max, matrix))
min_level = min(map(min, matrix))
max_count = 1
dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for l in range(min_level, max_level) :
	visited = [[False for _ in range(n)] for _ in range(n)]
	count = 0
	
	for i in range(n) : 
		for j in range(n) : 
			if not visited[i][j] and matrix[i][j] > l :
				count += 1
				dfs(i, j, l)

	# print(count)
	max_count = max(max_count, count)
	
print(max_count)