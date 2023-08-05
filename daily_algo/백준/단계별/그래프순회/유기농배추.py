file = open("./dfs/유기농배추tc.txt", "r")

def dfs(coordi, visited) : 
	i, j = coordi
	# 종료조건 필요 없엉

	# 재귀
	for d in dx : 
		di, dj = d
		if 0 <= i+di < n and 0 <= j+dj < m and matrix[i+di][j+dj] != 0 and not visited[i+di][j+dj] :
			visited[i+di][j+dj] = True
			dfs((i+di, j+dj), visited)

tcs = int(file.readline())
for tc in range(tcs) : 
	print(tc + 1, "번째 테스트 케이스")

	# 가로, 세로, 배추 개수
	m, n, k = map(int, file.readline().split())
	matrix = [[0 for _ in range(m)] for _ in range(n)]
	for _ in range(k) : 
		x, y = map(int, file.readline().split())
		matrix[y][x] = 1

	print(m, n, k)
	for mat in matrix : 
		print(mat)

	visited = [[False for _ in range(m)] for _ in range(n)]
	dx = [(1, 0), (-1, 0), (0, -1), (0, 1)]
	count = 0 
	
	for i in range(n) : 
		for j in range(m) : 
			if matrix[i][j] != 0 and not visited[i][j] :
				visited[i][j] = True
				dfs((i, j), visited)
				count += 1

	print(count)
	print()

print()
for tc in range(tcs) : 
	print(tc + 1, "번째 테스트 케이스 정답 : ", file.readline())

file.close()

# 백준 제출용
# import sys

# sys.setrecursionlimit(10**9)

# def dfs(coordi, visited) : 
# 	i, j = coordi
# 	# 종료조건 필요 없엉

# 	# 재귀
# 	for d in dx : 
# 		di, dj = d
# 		if 0 <= i+di < n and 0 <= j+dj < m and matrix[i+di][j+dj] != 0 and not visited[i+di][j+dj] :
# 			visited[i+di][j+dj] = True
# 			dfs((i+di, j+dj), visited)

# tcs = int(sys.stdin.readline())
# for tc in range(tcs) : 
# 	# 가로, 세로, 배추 개수
# 	m, n, k = map(int, sys.stdin.readline().split())
# 	matrix = [[0 for _ in range(m)] for _ in range(n)]
# 	for _ in range(k) : 
# 		x, y = map(int, sys.stdin.readline().split())
# 		matrix[y][x] = 1

# 	visited = [[False for _ in range(m)] for _ in range(n)]
# 	dx = [(1, 0), (-1, 0), (0, -1), (0, 1)]
# 	count = 0 
	
# 	for i in range(n) : 
# 		for j in range(m) : 
# 			if matrix[i][j] != 0 and not visited[i][j] :
# 				visited[i][j] = True
# 				dfs((i, j), visited)
# 				count += 1

# 	print(count)