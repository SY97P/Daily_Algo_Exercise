# 해결방안 5번 : 


# # 해결방안 4번 : 시간초과
# # BFS
# 
# from collections import deque

# file = open("./dfs/벽부수고이동하기tc.txt", "r")

# def bfs(queue) : 
# 	while queue :
# 		i, j, count = queue.popleft()

# 		if i == n - 1 and j == m - 1 :
# 			return count

# 		for d in dx : 
# 			di = i + d[0]
# 			dj = j + d[1]
# 			if 0 <= di < n and 0 <= dj < m and not visited[di][dj] and matrix[di][dj] != 1 :
# 				visited[di][dj] = True
# 				queue.append((di, dj, count + 1))

# for tc in range(7) :
# 	n, m = map(int, file.readline().split())
# 	matrix = [list(map(int, file.readline().strip("\n"))) for _ in range(n)]
# 	answer = int(file.readline())
# 	file.readline()

# 	print(n, m, answer)
# 	for mat in matrix : 
# 		print(mat)

# 	if matrix[0][0] == matrix[n-1][m-1] == 1 :
# 		print(-1)
# 		print()
# 	else :
# 		count_list = []
# 		dx = [(1,0), (0,1), (0, -1), (-1, 0)]
# 		for i in range(n) : 
# 			for j in range(m) :
# 				if matrix[i][j] == 1 or (i == j == 0): 
# 					matrix[i][j] = 0
# 					visited = [[False for _ in range(m)] for _ in range(n)]
# 					visited[0][0] = True
# 					result = bfs(deque([(0, 0, 1)]))
# 					if not result is None : 
# 						count_list.append(result)
# 					matrix[i][j] = 1
	
# 		print(count_list)
# 		print(-1 if not count_list else min(count_list))
# 		print()

# file.close()

# # 백준 제출용
# from sys import stdin
# from collections import deque

# def bfs(queue) : 
# 	while queue :
# 		i, j, count = queue.popleft()

# 		if i == n - 1 and j == m - 1 :
# 			return count

# 		for d in dx : 
# 			di = i + d[0]
# 			dj = j + d[1]
# 			if 0 <= di < n and 0 <= dj < m and not visited[di][dj] and matrix[di][dj] != 1 :
# 				visited[di][dj] = True
# 				queue.append((di, dj, count + 1))

# n, m = map(int, stdin.readline().split())
# matrix = [list(map(int, stdin.readline().strip("\n"))) for _ in range(n)]

# if matrix[0][0] == matrix[n-1][m-1] == 1 :
# 	print(-1)
# else :
# 	count_list = []
# 	dx = [(1,0), (0,1), (0, -1), (-1, 0)]
# 	for i in range(n) : 
# 		for j in range(m) :
# 			if matrix[i][j] == 1 or (i == j == 0):
# 				# 현재 노드가 벽일 때, 주변에 1이 세 개 이상 있는 경우는 논외
# 				if 0 < i < n-1 and 0 < j < m-1 and [matrix[i-1+x][j-1+y] for x in range(2) for y in range(2)].count(1) >= 3 :
# 					matrix[i][j] = 0
# 					visited = [[False for _ in range(m)] for _ in range(n)]
# 					visited[0][0] = True
# 					result = bfs(deque([(0, 0, 1)]))
# 					if not result is None : 
# 						count_list.append(result)
# 					matrix[i][j] = 1

# 	print(-1 if not count_list else min(count_list))


# # # 해결방안 3번 :
# # # BFS
# # from collections import deque

# # file = open("./dfs/벽부수고이동하기tc.txt", "r")

# # def bfs(queue) :
# # 	global check
# # 	while queue : 
# # 		i, j, wall, count = queue.popleft()

# # 		print(i, j, wall, count)

# # 		if i == n-1 and j == m-1 :
# # 			check = True
# # 			return count

# # 		if matrix[i][j] == 1 : 
# # 			wall += 1

# # 		for d in dx : 
# # 			di = i + d[0]
# # 			dj = j + d[1]
# # 			if 0 <= di < n and 0 <= dj < m :
# # 				# 그래도 부신 벽이 있음에도 새로 1인 값은 안 됨
# # 				if not (wall > 0 and matrix[di][dj] == 1) :
# # 					queue.append((di, dj, wall, count + 1))
		

# # for tc in range(7) : 
# # 	n , m = map(int, file.readline().split())
# # 	matrix = [list(map(int, file.readline().strip("\n"))) for _ in range(n)]
# # 	answer = int(file.readline())
# # 	file.readline()

# # 	if tc != 5 : 
# # 		continue

# # 	print(n, m, answer)
# # 	for mat in matrix : 
# # 		print(mat)

# # 	check = False
# # 	dx = [(1, 0), (0, 1), (0, -1), (-1, 0)]
# # 	record = [[-1 for _ in range(m)] for _ in range(n)]
# # 	record[0][0] = 1
# # 	result = bfs(deque([(0,0,0,1)]))
# # 	if check :
# # 		print(result)
# # 	else : 
# # 		print(-1)

# # file.close()

# # # 백준 제출용
# # # from sys import stdin
# # # from collections import deque

# # # n, m = map(int, stdin.readline().split())
# # # matrix = [list(map(int, stdin.readline().strip("\n"))) for _ in range(n)]

# # # def bfs(queue) :
# # # 	global check
# # # 	while queue : 
# # # 		i, j, wall, count = queue.popleft()

# # # 		if i == n-1 and j == m-1 :
# # # 			check = True
# # # 			return count

# # # 		if matrix[i][j] == 1 : 
# # # 			wall += 1

# # # 		for d in dx : 
# # # 			di = i + d[0]
# # # 			dj = j + d[1]
# # # 			if 0 <= di < n and 0 <= dj < m  :
# # # 				# 그래도 부신 벽이 있음에도 새로 1인 값은 안 됨
# # # 				if not (wall > 0 and matrix[di][dj] == 1) :
# # # 					queue.append((di, dj, wall, count + 1))
		
# # # check = False
# # # dx = [(1, 0), (0, 1), (0, -1), (-1, 0)]
# # # record = [[-1 for _ in range(m)] for _ in range(n)]
# # # record[0][0] = 1
# # # result = bfs(deque([(0,0,0,1)]))
# # # if check :
# # # 	print(result)
# # # else : 
# # # 	print(-1)


# # # # 해결방안 2번 : 오류
# # # # BFS
# # # from collections import deque

# # # file = open("./dfs/벽부수고이동하기tc.txt", "r")

# # # def bfs(queue) : 
# # # 	global result
# # # 	while queue : 
# # # 		i, j, wall, count = queue.popleft()

# # # 		# print(i, j, wall, count)

# # # 		if i == n - 1 and j == m - 1 :
# # # 			result = count if (count < result) or (result == -1) else result
# # # 			visited[i][j] = False
# # # 			# print("result : ", result)

# # # 		if matrix[i][j] == 1 : 
# # # 			wall += 1

# # # 		for d in dx : 
# # # 			di = i + d[0]
# # # 			dj = j + d[1]
# # # 			if 0 <= di < n and 0 <= dj < m and not visited[di][dj] and not (wall > 0 and matrix[di][dj] == 1) :
# # # 				# 해결방안 3번 (n log n)
# # # 				#
# # # 				visited[di][dj] = False
# # # 				queue.append((di, dj, wall, count + 1))
	

# # # for tc in range(7) :
	
# # # 	n, m = map(int, file.readline().split())
# # # 	matrix = [list(map(int, file.readline().strip("\n"))) for _ in range(n)]
# # # 	answer = int(file.readline())
# # # 	file.readline()

# # # 	if tc < 6 :
# # # 		continue

# # # 	print(n, m, answer)
# # # 	for mat in matrix : 
# # # 		print(mat)

# # # 	dx = [(1, 0), (0, 1), (0, -1), (-1, 0)]
# # # 	visited = [[False for _ in range(m)] for _ in range(n)]
# # # 	result = -1
# # # 	visited[0][0] = True
# # # 	bfs(deque([(0, 0, 0, 1)]))
# # # 	print(result)

# # # file.close()

# # # # 백준 제출용
# # # # from sys import stdin
# # # # from collections import deque

# # # # n, m = map(int, stdin.readline().split())
# # # # matrix = [list(map(int, stdin.readline().strip("\n"))) for _ in range(n)]

# # # # def bfs(queue) : 
# # # # 	global result
# # # # 	while queue : 
# # # # 		i, j, wall, count = queue.popleft()

# # # # 		if i == n - 1 and j == m - 1 :
# # # # 			result = min(result, count) if result != -1 else count
# # # # 			visited[i][j] = False

# # # # 		if matrix[i][j] == 1: 
# # # # 			wall += 1

# # # # 		for d in dx : 
# # # # 			di = i + d[0]
# # # # 			dj = j + d[1]
# # # # 			if 0 <= di < n and 0 <= dj < m and not visited[di][dj] and not (wall > 0 and matrix[di][dj] == 1) :
# # # # 				visited[di][dj] = True
# # # # 				queue.append((di, dj, wall, count + 1))

# # # # dx = [(1, 0), (0, 1), (0, -1), (-1, 0)]
# # # # visited = [[False for _ in range(m)] for _ in range(n)]
# # # # result = -1
# # # # visited[0][0] = True
# # # # bfs(deque([(0, 0, 0, 1)]))
# # # # print(result)


# # # # 해결방안 1번 : 시간초과
# # # # DFS 한계로 추정됨 (모든 경로 탐색으로는 안 되지 않을까)
# # # # file = open("./dfs/벽부수고이동하기tc.txt", "r")

# # # # def dfs(coordi, wall, count, visited) :
# # # # 	i, j = coordi

# # # # 	print(i, j, matrix[i][j], wall, count)
	
# # # # 	if wall > 1 : 
# # # # 		print("more than one wall destroyed")
# # # # 		return

# # # # 	if i == n-1 and j == m-1 :
# # # # 		count_list.append(count)
# # # # 		visited[i][j] = False
# # # # 		print("Arrived at the destination")
# # # # 		return

# # # # 	# 재귀
# # # # 	for d in dx :
# # # # 		di = i + d[0]
# # # # 		dj = j + d[1]
# # # # 		# 시간초과 방지용 테스트
# # # # 		if 0 <= di < n and 0 <= dj < m and not visited[di][dj] and not (wall > 0 and matrix[di][dj] == 1) :
# # # # 			visited[di][dj] = True
# # # # 			if matrix[di][dj] != 1 : 
# # # # 				dfs((di, dj), wall, count + 1, visited)
# # # # 			else : 
# # # # 				dfs((di, dj), wall+1, count + 1, visited)
# # # # 			visited[di][dj] = False
		

# # # # for _ in range(2) :
# # # # 	n, m = map(int, file.readline().split())
# # # # 	matrix = [list(map(int, file.readline().strip("\n"))) for _ in range(n)]
# # # # 	answer = int(file.readline())
# # # # 	file.readline()

# # # # 	print(n, m, answer)
# # # # 	for mat in matrix : 
# # # # 		print(mat)

# # # # 	# logic
# # # # 	visited = [[False for _ in range(m)] for _ in range(n)]
# # # # 	count_list = []
# # # # 	# 아래 방향 (하우좌상)
# # # # 	dx = [(1, 0), (0, 1), (0, -1), (-1, 0)]

# # # # 	visited[0][0] = True
# # # # 	dfs((0, 0), 0, 1, visited)

# # # # 	print(count_list)

# # # # 	if not count_list : 
# # # # 		print(-1)
# # # # 	else : 
# # # # 		print(min(count_list))

# # # # 	print()

# # # # file.close()

# # # # # 백준 제출용
# # # # import sys

# # # # def dfs(coordi, wall, count, visited) :
# # # # 	i, j = coordi
	
# # # # 	if wall > 1 : 
# # # # 		return

# # # # 	if i == n-1 and j == m-1 :
# # # # 		count_list.append(count)
# # # # 		visited[i][j] = False
# # # # 		return

# # # # 	# 재귀
# # # # 	for d in dx :
# # # # 		di = i + d[0]
# # # # 		dj = j + d[1]
# # # # 		# 시간초과 방지용 테스트
# # # # 		if 0 <= di < n and 0 <= dj < m and not visited[di][dj] and not (wall > 0 and matrix[di][dj] == 1) :
# # # # 			visited[di][dj] = True
# # # # 			if matrix[di][dj] != 1 : 
# # # # 				dfs((di, dj), wall, count + 1, visited)
# # # # 			else : 
# # # # 				dfs((di, dj), wall+1, count + 1, visited)
# # # # 			visited[di][dj] = False
		
# # # # n, m = map(int, file.readline().split())
# # # # matrix = [list(map(int, file.readline().strip("\n"))) for _ in range(n)]

# # # # # logic
# # # # visited = [[False for _ in range(m)] for _ in range(n)]
# # # # count_list = []
# # # # # 아래 방향 (하우좌상)
# # # # dx = [(1, 0), (0, 1), (0, -1), (-1, 0)]

# # # # visited[0][0] = True
# # # # dfs((0, 0), 0, 1, visited)

# # # # if not count_list : 
# # # # 	print(-1)
# # # # else : 
# # # # 	print(min(count_list))