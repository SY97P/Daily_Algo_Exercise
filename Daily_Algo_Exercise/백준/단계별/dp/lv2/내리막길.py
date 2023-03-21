# 해결방안 3번 : 
# DFS + DP (bot top)
file = open("./dfs/내리막길tc.txt", "r")

def dfs(i, j) : 
	# 종료조건
	if i == m - 1 and j == n - 1:
		return 1

	# dp값 존재
	if dp[i][j] != -1 : 
		return dp[i][j]

	# 현재노드에서 상하좌우로 목적지까지 갈 수 있는 총 경우의 수
	ways = 0
	for d in dx : 
		di = i + d[0]
		dj = j + d[1]
		if 0 <= di < m and 0 <= dj < n and matrix[i][j] > matrix[di][dj] :
			ways += dfs(di, dj)

	# 모든 방향 탐색 후 현재 노드 dp값 갱신
	dp[i][j] = ways
	return dp[i][j]
	

m, n = map(int, file.readline().split())
matrix = [list(map(int, file.readline().split())) for _ in range(m)]
answer = int(file.readline())

print(m, n, answer)
for mat in matrix : 
	print(mat)

# -1로 초기화해야 메모그레이션 제대로 쓰는 것
dp = [[-1 for _ in range(n)] for _ in range(m)]
dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
print(dfs(0, 0))

file.close()

# 백준 제출용
# 해결방안 3번 : 
# DFS + DP (bot top)
import sys

sys.setrecursionlimit(10 ** 9)

def dfs(i, j) : 
	# 종료조건
	if i == m - 1 and j == n - 1:
		return 1

	# dp값 존재
	if dp[i][j] != -1 : 
		return dp[i][j]

	# 현재노드에서 상하좌우로 목적지까지 갈 수 있는 총 경우의 수
	ways = 0
	for d in dx : 
		di = i + d[0]
		dj = j + d[1]
		if 0 <= di < m and 0 <= dj < n and matrix[i][j] > matrix[di][dj] :
			ways += dfs(di, dj)

	# 모든 방향 탐색 후 현재 노드 dp값 갱신
	dp[i][j] = ways
	return dp[i][j]
	

m, n = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

# -1로 초기화해야 메모그레이션 제대로 쓰는 것
dp = [[-1 for _ in range(n)] for _ in range(m)]
dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
print(dfs(0, 0))

# # 해결방안 2번 : 시간초과 20%
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