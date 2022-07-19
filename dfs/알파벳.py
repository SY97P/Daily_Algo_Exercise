# 해결방안 1번 :
# DFS
from collections import deque


file = open("./dfs/알파벳tc.txt", "r")

def dfs(i, j, alpha) :
	global result
	for d in dx : 
		di = i + d[0]
		dj = j + d[1]
		if 0 <= di < r and 0 <= dj < c and not alpha[ord(matrix[di][dj]) - 65] :
			alpha[ord(matrix[di][dj]) - 65] = True
			dfs(di, dj, alpha)
			alpha[ord(matrix[di][dj]) - 65] = False
	print(result, alpha.count(True))
	if alpha.count(True)== 4:
		print(alpha)
	result = max(result, alpha.count(True))

for _ in range(3) : 
	r, c = map(int, file.readline().split())
	matrix = [list(file.readline().strip("\n")) for _ in range(r)]
	answer = int(file.readline())
	file.readline()

	print(r,c , answer)
	for mat in matrix :
		print(mat)

	result = 0
	alpha = [False for _ in range(26)]
	dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	dfs(0, 0, alpha)
	print(result)

	print()

file.close()

# 백준 제출용
# import sys
# from collections import deque

# sys.setrecursionlimit(10 ** 9)

# def dfs(i, j, path) :
# 	global result
# 	for d in dx : 
# 		di = i + d[0]
# 		dj = j + d[1]
# 		if 0 <= di < r and 0 <= dj < c and not alpha[ord(matrix[di][dj]) - 65] :
# 			alpha[ord(matrix[di][dj])] = True
# 			dfs(di, dj, path)
# 			alpha[ord(matrix[di][dj])] = False
# 	result = max(result, len(path))

# r, c = map(int, stdin.readline().split())
# matrix = [list(stdin.readline().strip("\n")) for _ in range(r)]

# result = 0
# alpha = [False for _ in range(26)]
# dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# dfs(0, 0, alpha)
# print(result)