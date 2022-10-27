# 해결방안 3번 : 
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

	print(r, c, answer)

	result = 0
	alpha = [False for _ in range(26)]
	dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	dfs(0, 0, alpha)
	print(result)
file.close()

# 백준 제출용
# 해결방안 3번 : 
# DFS
# 시간초과 해결을 위해 Bool list(26)을 만들 예정
import sys

sys.setrecursionlimit(10 ** 9)

def dfs(i, j, visited) : 
	global result
	result = max(result, visited.count(True))
	for d in dx : 
		di = i + d[0]
		dj = j + d[1]
		# 방문할 알파벳이 방문한 적이 없어야 함.
		if 0 <= di < r and 0 <= dj < c and not visited[ord(matrix[di][dj]) - 65] :
			visited[ord(matrix[di][dj]) - 65] = True
			dfs(di, dj, visited)
			visited[ord(matrix[di][dj]) - 65] = False
			

r, c = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().strip("\n")) for _ in range(r)]

dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [False for _ in range(26)]
visited[ord(matrix[0][0]) - 65] = True
result = 0
dfs(0, 0, visited)
print(result)

# # 해결방안 2번 :
# # BFS
# # 큐에서 제거되는 가장 마지막 tuple이 가진 count값이 result
# from collections import deque

# file = open("./dfs/알파벳tc.txt", "r")

# def bfs(queue) : 
# 	final_count = 0
# 	while queue : 
# 		i, j, dic, count = queue.popleft()

# 		final_count = count

# 		for d in dx : 
# 			di = i + d[0]
# 			dj = j + d[1]
# 			if 0 <= di < r and 0 <= dj < c and not dic[ord(matrix[di][dj])] :
# 				temp = dic
# 				temp[ord(matrix[di][dj])] = True
# 				queue.append((di, dj, temp, count + 1))
# 	return final_count
	

# for _ in range(3) :
# 	r,c = map(int, file.readline().split())
# 	matrix = [list(file.readline().strip("\n")) for _ in range(r)]
# 	answer = int(file.readline())
# 	file.readline()

# 	print(r, c, answer)
# 	for mat in matrix : 
# 		print(mat)

# 	dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 	di = {i+65 : False for i in range(26)}
# 	di[ord(matrix[0][0])] = True

# 	for key in di.keys() :
# 		print(key, di[key])
		
# 	result = bfs(deque([(0, 0, di, 1)]))
# 	print(result)
# 	print()

# file.close()

# # 백준 제출용
# # from sys import stdin
# # from collections import deque

# # def bfs(queue) : 
# # 	final_count = 0
# # 	while queue : 
# # 		i, j, dictionary, count = queue.popleft()

# # 		final_count = count

# # 		for d in dx : 
# # 			di = i + d[0]
# # 			dj = j + d[1]
# # 			# not in list : 이 부분이 시간초과 원인이지 않을까?
# # 			# 해결방안 2-1 
# # 			# list -> dictionary로 변경
# # 			if 0 <= di < r and 0 <= dj < c and not dictionary[ord(matrix[di][dj] - 65)] :
# # 				dictionary[matrix[di][dj]] = True
# # 				queue.append((di, dj, dictionary, count + 1))
# # 				dictionary[matrix[di][dj]] = False
# # 	return final_count

# # r,c = map(int, stdin.readline().split())
# # matrix = [list(stdin.readline().strip("\n")) for _ in range(r)]
# # answer = int(file.readline())
# # file.readline()

# # print(r, c, answer)
# # for mat in matrix : 
# # 	print(mat)

# # dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# # index = 0
# # dic = {i : False for i in range(26)}
# # dic[ord(matrix[0][0]) - 65] = True
# # result = bfs(deque([(0, 0, dic, 1)]))
# # print(result)

# # # 해결방안 1번 :
# # # DFS
# # file = open("./dfs/알파벳tc.txt", "r")

# # def dfs(i, j, path) :
# # 	global result
# # 	# print(i, j, path)
# # 	for d in dx : 
# # 		di = i + d[0]
# # 		dj = j + d[1]
# # 		if 0 <= di < r and 0 <= dj < c and matrix[di][dj] not in path :
# # 			dfs(di, dj, path + [matrix[di][dj]])
# # 	result = max(result, len(path))

# # for _ in range(3) : 
# # 	r, c = map(int, file.readline().split())
# # 	matrix = [list(file.readline().strip("\n")) for _ in range(r)]
# # 	answer = int(file.readline())
# # 	file.readline()

# # 	print(r,c , answer)
# # 	for mat in matrix :
# # 		print(mat)

# # 	result = 0
# # 	dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# # 	dfs(0, 0, [matrix[0][0]])
# # 	print(result)

# # 	print()

# # file.close()

# # # 백준 제출용
# # import sys 

# # sys.setrecursionlimit(10 ** 9)

# # def dfs(i, j, path) :
# # 	global result
# # 	# print(i, j, path)
# # 	for d in dx : 
# # 		di = i + d[0]
# # 		dj = j + d[1]
# # 		if 0 <= di < r and 0 <= dj < c and matrix[di][dj] not in path :
# # 			dfs(di, dj, path + [matrix[di][dj]])
# # 	result = max(result, len(path))

# # r, c = map(int, sys.stdin.readline().split())
# # matrix = [list(sys.stdin.readline().strip("\n")) for _ in range(r)]
# # answer = int(file.readline())
# # file.readline()

# # print(r,c , answer)
# # for mat in matrix :
# # 	print(mat)

# file.close()

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
