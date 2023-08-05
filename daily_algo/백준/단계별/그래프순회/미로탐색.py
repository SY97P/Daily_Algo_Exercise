from collections import deque

# BFS로 풀이
file = open("./bfs/미로탐색tc.txt", "r")

def bfs(queue, visited) : 
	
	while queue : 
		# print(queue.popleft())
		(i, j), count = queue.popleft()

		# # 현재 노드 방문처리
		# visited[i][j] = True

		# count += 1

		print("i, j, count : ", i, j, count)

		if i == n-1 and j == m-1 : 
			return count

		# 현재 노드 인접한 접근가능 노드 선택
		# 우하좌상 순서
		for d in dx : 
			di, dj = d
			if 0 <= i + di < n and 0 <= j + dj < m and matrix[i+di][j+dj] != "0" and not visited[i+di][j+dj] :
				visited[i+di][j+dj] = True
				queue.append(((i+di, j+dj), count + 1))
		

for tc in range(8) :
	print(tc + 1, "번째 테스트 케이스 : ")
	n, m = map(int, file.readline().split())
	matrix = [list(file.readline().strip("\n")) for _ in range(n)]
	answer = int(file.readline())
	file.readline()

	print("n, m, answer : ", n, m, answer)
	# for mat in matrix : 
	# 	print(mat)

	# 우하좌상 순서
	dx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	queue = deque([((0, 0), 1)])
	visited = [[False for _ in range(m)] for _ in range(n)]
	answer = bfs(queue, visited)

	print(answer)
	print()

file.close()

# 백준 제출용
import sys
from collections import deque

def bfs(queue, visited) : 
	while queue : 
		(i, j), count = queue.popleft()

		if i == n-1 and j == m-1 : 
			return count

		# 현재 노드 인접한 접근가능 노드 선택
		# 우하좌상 순서
		for d in dx : 
			di, dj = d
			if 0 <= i + di < n and 0 <= j + dj < m and matrix[i+di][j+dj] != "0" and not visited[i+di][j+dj] :
				visited[i+di][j+dj] = True
				queue.append(((i+di, j+dj), count + 1))

n, m = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().strip("\n")) for _ in range(n)]

# 우하좌상 순서
dx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
queue = deque([((0, 0), 1)])
visited = [[False for _ in range(m)] for _ in range(n)]
answer = bfs(queue, visited)

print(answer)
	



# DFS로는 못 푸는 문제인 것 같음
# file = open("./dfs/미로탐색tc.txt", "r")

# def dfs(i, j, count, visited) :
# 	print("i, j, count : ", i, j, count)

# 	visited[i][j] = True
# 	# proceed = False

# 	# 종료조건 1 (목적지 도착)
# 	if i == n-1 and j == m-1 :
# 		count_list.append(count)
# 		visited[i][j] = False
# 		return

# 	# 재귀
# 	# 우하좌상 순서로 탐색을 함
# 	# out of index 검사와 유효한 index인지 검사 필요
# 	if (j+1 < m) and matrix[i][j+1] != 0 and not visited[i][j+1]:
# 		# proceed = True
# 		dfs(i, j+1, count + 1, visited)
# 	if (i+1 < n) and matrix[i+1][j] != 0 and not visited[i+1][j] :
# 		# proceed = True
# 		dfs(i+1, j, count + 1, visited)
# 	if (j-1 >= 0) and matrix[i][j-1] != 0 and not visited[i][j-1] :
# 		# proceed = True
# 		dfs(i, j-1, count + 1, visited)
# 	if (i-1 >= 0) and matrix[i-1][j] != 0 and not visited[i-1][j]:
# 		# proceed = True
# 		dfs(i-1, j, count + 1, visited)

	
# 	# # 종료조건 2 (막다른 길)
# 	# # 방문하지 않은 인접 인덱스 중 1이 없을때
# 	# if not proceed : 
# 	# 	count -= 1
# 	# 	return

# for tc in range(6) : 
# 	print(tc + 1, "번째 테스트 케이스")
# 	n, m = map(int, file.readline().split())
# 	matrix = [list(map(int,ㅁ file.readline().strip("\n"))) for _ in range(n)]
# 	visited = [[False for _ in range(m)] for _ in range(n)]
# 	answer = int(file.readline())
# 	file.readline()

# 	print(n,m, answer)
# 	for mat in matrix : 
# 		print(mat)

# 	count_list = [] 
# 	dfs(0, 0, 1, visited)
# 	print(count_list)
# 	print(min(count_list))
	
# 	print()

# file.close()

# # 백준 제출용
# # import sys

# # read = sys.stdin.readline

# # def dfs(i, j, count, visited) :
# # 	visited[i][j] = True

# # 	if i == n-1 and j == m-1 : 
# # 		visited[i][j] = False
# # 		count_list.append(count)
# # 		return

# # 	if (j+1 < m) and matrix[i][j+1] != 0 and not visited[i][j+1]:
# # 		dfs(i, j+1, count + 1, visited)
# # 	if (i+1 < n) and matrix[i+1][j] != 0 and not visited[i+1][j] :
# # 		dfs(i+1, j, count + 1, visited)
# # 	if (j-1 >= 0) and matrix[i][j-1] != 0 and not visited[i][j-1] :
# # 		dfs(i, j-1, count + 1, visited)
# # 	if (i-1 >= 0) and matrix[i-1][j] != 0 and not visited[i-1][j]:
# # 		dfs(i-1, j, count + 1, visited)

# # n, m = map(int, read().split())
# # matrix = [list(map(int, read().strip("\n"))) for _ in range(n)]
# # visited = [[False for _ in range(m)] for _ in range(n)]

# # count_list = []
# # dfs(0, 0, 1, visited)
# # print(min(count_list))