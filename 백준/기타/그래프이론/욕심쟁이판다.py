file = open("./dfs/욕심쟁이판다tc.txt", "r")

n = int(file.readline())
matrix = [list(map(int, file.readline().split())) for _ in range(n)]
answer = int(file.readline())

def dfs(i, j) : 
	if dp[i][j] == -1 :
		dp[i][j] = 0

		for d in dx: 
			di = i + d[0]
			dj = j + d[1]
			if 0 <= di < n and 0 <= dj < n and matrix[di][dj] > matrix[i][j] : 
				dp[i][j] = max(dp[i][j], dfs(di, dj))

	return dp[i][j] + 1

max_room = 0
dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dp = [[-1 for _ in range(n)] for _ in range(n)]
for i in range(n) : 
	for j in range(n) : 
		count = dfs(i, j)
		if max_room < count  :
			max_room = count

print(max_room)

file.close()

# 백준 제출용
# import sys

# sys.setrecursionlimit(10 ** 9)

# n = int(sys.stdin.readline())
# matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# def dfs(i, j) : 
# 	if dp[i][j] == -1 :
# 		dp[i][j] = 0

# 		for d in dx: 
# 			di = i + d[0]
# 			dj = j + d[1]
# 			if 0 <= di < n and 0 <= dj < n and matrix[di][dj] > matrix[i][j] : 
# 				dp[i][j] = max(dp[i][j], dfs(di, dj))

# 	return dp[i][j] + 1

# max_room = 0
# dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# dp = [[-1 for _ in range(n)] for _ in range(n)]
# for i in range(n) : 
# 	for j in range(n) : 
# 		count = dfs(i, j)
# 		if max_room < count  :
# 			max_room = count

# print(max_room)