# 해결방안 2번 : 
# DFS + DP

# # 해결방안 1번 : 시간초과 20%
# file = open("./dfs/내리막길tc.txt", "r")

# def dfs(i, j) :
# 	global count 
# 	global m
# 	global n

# 	if i == m-1 and j == n-1 :
# 		count += 1
# 		visited[i][j] = False
# 		return

# 	curr = matrix[i][j]

# 	for d in dx : 
# 		di = i + d[0]
# 		dj = j + d[1]
# 		if 0 <= di < m and 0 <= dj < n and curr > matrix[di][dj] : 
# 			visited[di][dj] = True
# 			dfs(di, dj)
# 			visited[di][dj] = False

# m, n = map(int, file.readline().split())
# matrix = [list(map(int, file.readline().split())) for _ in range(m)]
# answer = int(file.readline())

# print(m, n, answer)
# for mat in matrix : 
# 	print(mat)

# count = 0
# visited = [[False for _ in range(n)] for _ in range(m)]
# dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# dfs(0, 0)
# print(count)

# file.close()

# # 백준 제출용
# import sys

# sys.setrecursionlimit(10 ** 9)

# # 해결방안 1번 : 
# def dfs(i, j) :
# 	global count 
# 	global m
# 	global n

# 	if i == m-1 and j == n-1 :
# 		count += 1
# 		visited[i][j] = False
# 		return

# 	curr = matrix[i][j]

# 	for d in dx : 
# 		di = i + d[0]
# 		dj = j + d[1]
# 		if 0 <= di < m and 0 <= dj < n and curr > matrix[di][dj] : 
# 			visited[di][dj] = True
# 			dfs(di, dj)
# 			visited[di][dj] = False

# m, n = map(int, sys.stdin.readline().split())
# matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

# count = 0
# visited = [[False for _ in range(n)] for _ in range(m)]
# dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# dfs(0, 0)
# print(count)