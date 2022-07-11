file = open("./dfs/미로탐색tc.txt", "r")

def dfs(i, j, count, visited) :
	print("i, j, count : ", i, j, count)

	visited[i][j] = True
	# proceed = False

	# 종료조건 1 (목적지 도착)
	if i == n-1 and j == m-1 :
		count_list.append(count)
		visited[i][j] = False
		return

	# 재귀
	# 우하좌상 순서로 탐색을 함
	# out of index 검사와 유효한 index인지 검사 필요
	if (j+1 < m) and matrix[i][j+1] != 0 and not visited[i][j+1]:
		# proceed = True
		dfs(i, j+1, count + 1, visited)
	if (i+1 < n) and matrix[i+1][j] != 0 and not visited[i+1][j] :
		# proceed = True
		dfs(i+1, j, count + 1, visited)
	if (j-1 >= 0) and matrix[i][j-1] != 0 and not visited[i][j-1] :
		# proceed = True
		dfs(i, j-1, count + 1, visited)
	if (i-1 >= 0) and matrix[i-1][j] != 0 and not visited[i-1][j]:
		# proceed = True
		dfs(i-1, j, count + 1, visited)

	
	# # 종료조건 2 (막다른 길)
	# # 방문하지 않은 인접 인덱스 중 1이 없을때
	# if not proceed : 
	# 	count -= 1
	# 	return

for tc in range(4) : 
	print(tc + 1, "번째 테스트 케이스")
	n, m = map(int, file.readline().split())
	matrix = [list(map(int, file.readline().strip("\n"))) for _ in range(n)]
	visited = [[False for _ in range(m)] for _ in range(n)]
	answer = int(file.readline())
	file.readline()

	print(n,m, answer)
	for mat in matrix : 
		print(mat)

	count_list = [] 
	dfs(0, 0, 1, visited)
	print(count_list)
	print(min(count_list))
	
	print()

file.close()

# 백준 제출용
# import sys

# read = sys.stdin.readline

# def dfs(i, j, count, visited) :
# 	visited[i][j] = True

# 	if i == n-1 and j == m-1 : 
# 		visited[i][j] = False
# 		count_list.append(count)
# 		return

# 	if (j+1 < m) and matrix[i][j+1] != 0 and not visited[i][j+1]:
# 		dfs(i, j+1, count + 1, visited)
# 	if (i+1 < n) and matrix[i+1][j] != 0 and not visited[i+1][j] :
# 		dfs(i+1, j, count + 1, visited)
# 	if (j-1 >= 0) and matrix[i][j-1] != 0 and not visited[i][j-1] :
# 		dfs(i, j-1, count + 1, visited)
# 	if (i-1 >= 0) and matrix[i-1][j] != 0 and not visited[i-1][j]:
# 		dfs(i-1, j, count + 1, visited)

# n, m = map(int, read().split())
# matrix = [list(map(int, read().strip("\n"))) for _ in range(n)]
# visited = [[False for _ in range(m)] for _ in range(n)]

# count_list = []
# dfs(0, 0, 1, visited)
# print(min(count_list))