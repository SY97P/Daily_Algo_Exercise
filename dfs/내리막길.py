# 해결방안 3번 : 


# # 해결방안 2번 : 
# # DFS + DP
# file = open("./dfs/내리막길tc.txt", "r")

# def dfs(i, j) : 
# 	global m
# 	global n
	
# 	if i == m - 1 and j == n - 1  :
# 		return 1

# 	for d in dx : 
# 		di = i + d[0]
# 		dj = j + d[1]
# 		if 0 <= di < m and 0 <= dj < n and matrix[i][j] > matrix[di][dj] : 
# 			if dp[di][dj] != 0 : 
# 				dp[di][dj] += 1
# 			else : 
# 				if dfs(di, dj) == 1 : 
# 					dp[di][dj] = 1

# m, n = map(int, file.readline().split())
# matrix = [list(map(int, file.readline().split())) for _ in range(m)]
# answer = int(file.readline())

# print(m, n, answer)
# for mat in matrix : 
# 	print(mat)

# dp = [[0 for _ in range(n)] for _ in range(m)]
# dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# dfs(0, 0)
# maxValue = 0
# for dpr in dp : 
# 	for dpv in dpr :
# 		if dpv > maxValue :
# 			maxValue = dpv
# print(maxValue)

# file.close()

# # 백준 제출용
# # 해결방안 2번 : 
# # DFS + DP
# import sys

# sys.setrecursionlimit(10 ** 9)

# def dfs(i, j) : 
# 	global m
# 	global n
	
# 	if i == m - 1 and j == n - 1  :
# 		return 1

# 	dp[i][j] = 0

# 	for d in dx : 
# 		di = i + d[0]
# 		dj = j + d[1]
# 		if 0 <= di < m and 0 <= dj < n and matrix[i][j] > matrix[di][dj] : 
# 			if dp[di][dj] > 0 : 
# 				dp[di][dj] += 1
# 			else : 
# 				if dfs(di, dj) == 1 : 
# 					dp[di][dj] = 1

# m, n = map(int, sys.stdin.readline().split())
# matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

# dp = [[-1 for _ in range(n)] for _ in range(m)]
# dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# dfs(0, 0)
# maxValue = -1
# for dpr in dp : 
# 	for dpv in dpr :
# 		if dpv > maxValue :
# 			maxValue = dpv
# print(maxValue)

# # # 해결방안 1번 : 시간초과 20%
# # file = open("./dfs/내리막길tc.txt", "r")

# # def dfs(i, j) :
# # 	global count 
# # 	global m
# # 	global n

# # 	if i == m-1 and j == n-1 :
# # 		count += 1
# # 		visited[i][j] = False
# # 		return

# # 	curr = matrix[i][j]

# # 	for d in dx : 
# # 		di = i + d[0]
# # 		dj = j + d[1]
# # 		if 0 <= di < m and 0 <= dj < n and curr > matrix[di][dj] : 
# # 			visited[di][dj] = True
# # 			dfs(di, dj)
# # 			visited[di][dj] = False

# # m, n = map(int, file.readline().split())
# # matrix = [list(map(int, file.readline().split())) for _ in range(m)]
# # answer = int(file.readline())

# # print(m, n, answer)
# # for mat in matrix : 
# # 	print(mat)

# # count = 0
# # visited = [[False for _ in range(n)] for _ in range(m)]
# # dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# # dfs(0, 0)
# # print(count)

# # file.close()

# # # 백준 제출용
# # import sys

# # sys.setrecursionlimit(10 ** 9)

# # # 해결방안 1번 : 
# # def dfs(i, j) :
# # 	global count 
# # 	global m
# # 	global n

# # 	if i == m-1 and j == n-1 :
# # 		count += 1
# # 		visited[i][j] = False
# # 		return

# # 	curr = matrix[i][j]

# # 	for d in dx : 
# # 		di = i + d[0]
# # 		dj = j + d[1]
# # 		if 0 <= di < m and 0 <= dj < n and curr > matrix[di][dj] : 
# # 			visited[di][dj] = True
# # 			dfs(di, dj)
# # 			visited[di][dj] = False

# # m, n = map(int, sys.stdin.readline().split())
# # matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

# # count = 0
# # visited = [[False for _ in range(n)] for _ in range(m)]
# # dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# # dfs(0, 0)
# # print(count)