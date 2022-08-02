 

# 해결방안 2번 : 
# # 녹이기 + 덩어리 세기 => dfs
# file = open("./dfs/빙산tc.txt", "r")

# def meltAll() : 
# 	for i in range(n) : 
# 		for j in range(m) :
# 			if matrix[i][j] != 0 :
# 				return False
# 	return True

# def dfs(i, j) : 
# 	dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 	# 녹이기
# 	if matrix[i][j] != 0 :
# 		count = 0
# 		for d in dx :
# 			di = i + d[0]
# 			dj = j + d[1]
# 			if matrix[di][dj] == 0 : 
# 				count += 1
# 		next[i][j] = count

# 	# 덩어리 세기
# 	for d in dx : 
# 		di = i + d[0]
# 		dj = j + d[1]
# 		if not visited[di][dj] and matrix[di][dj] != 0 :
# 			visited[di][dj] = True
# 			dfs(di, dj)

# n, m = map(int, file.readline().split())
# matrix = [list(map(int, file.readline().split())) for _ in range(n)]
# answer = int(file.readline())

# print(n, m, answer)


# year = 0
# while True :
	
# 	icebug = 0
# 	visited = [[False for _ in range(m)] for _ in range(n)]
# 	next = [[0 for _ in range(m)] for _ in range(n)]
	
# 	if year > 5 : 
# 		break
# 	print("matrix ")
# 	for mat in matrix : 
# 		print(mat)

# 	# 모든 빙산이 녹았는가?
# 	if meltAll() : 
# 		print(0)
# 		break

# 	# 녹이기 + 덩어리 세기 => dfs
# 	for i in range(1, n-1) : 
# 		for j in range(1, m-1) : 
# 			if matrix[i][j] != 0 and not visited[i][j] :
# 				if icebug > 1 : 
# 					print(icebug)
# 					break
# 				icebug += 1
# 				dfs(i, j)

# 	print("icebug : ", icebug)
# 	if icebug > 1 :
# 		print(year)
# 		break

# 	# 현재 년도에서 녹인 애들을 다음 matrix로 갱신
# 	for i in range(n) : 
# 		for j in range(m) : 
# 			matrix[i][j] -= next[i][j]
# 			if matrix[i][j] < 0 :
# 				matrix[i][j] = 0

# 	year += 1

# file.close()

# # 백준 제출용
# # 해결방안 2번 : 
# # 녹이기 + 덩어리 세기 => dfs
# import sys

# sys.setrecursionlimit(10 ** 9)

# def meltAll() : 
# 	for i in range(n) : 
# 		for j in range(m) :
# 			if matrix[i][j] != 0 :
# 				return False
# 	return True

# def dfs(i, j) : 
# 	dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 	# 녹이기
# 	if matrix[i][j] != 0 :
# 		count = 0
# 		for d in dx :
# 			di = i + d[0]
# 			dj = j + d[1]
# 			if matrix[di][dj] == 0 : 
# 				count += 1
# 		next[i][j] = count

# 	# 덩어리 세기
# 	for d in dx : 
# 		di = i + d[0]
# 		dj = j + d[1]
# 		if not visited[di][dj] and matrix[di][dj] != 0 :
# 			visited[di][dj] = True
# 			dfs(di, dj)

# n, m = map(int, sys.stdin.readline().split())
# matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# year = 0
# while True :
	
# 	icebug = 0
# 	visited = [[False for _ in range(m)] for _ in range(n)]
# 	next = [[0 for _ in range(m)] for _ in range(n)]

# 	# 모든 빙산이 녹았는가?
# 	if meltAll() : 
# 		print(0)
# 		break

# 	# 녹이기 + 덩어리 세기 => dfs
# 	for i in range(1, n-1) : 
# 		for j in range(1, m-1) : 
# 			if matrix[i][j] != 0 and not visited[i][j] :
# 				if icebug > 1 : 
# 					break
# 				icebug += 1
# 				dfs(i, j)

# 	if icebug > 1 :
# 		print(year)
# 		break

# 	# 현재 년도에서 녹인 애들을 다음 matrix로 갱신
# 	for i in range(n) : 
# 		for j in range(m) : 
# 			matrix[i][j] -= next[i][j]
# 			if matrix[i][j] < 0 :
# 				matrix[i][j] = 0

# 	year += 1


# # # 해결방안 1번 : 
# # # 단순 반복 + DFS
# # # 녹이기.  + 덩어리 세기
# # import copy 

# # file = open("./dfs/빙산tc.txt", "r")

# # # 다 녹았도다 -> True
# # # 아직이도다. -> False
# # def meltAll() : 
# # 	for mat in matrix : 
# # 		for ma in mat :
# # 			if ma != 0 :
# # 				return False
# # 	return True

# # # 녹이거라
# # def melt() :
# # 	next = copy.deepcopy(matrix)
# # 	for i in range(1, n-1) : 
# # 		for j in range(1, m-1) : 
# # 			# 얼음인 애들 차례가 되면
# # 			if matrix[i][j] != 0 :
# # 				# 상하좌우에서 0인 개수를 찾아
# # 				count = 0
# # 				for d in dx :
# # 					di = i + d[0]
# # 					dj = j + d[1]
# # 					if matrix[di][dj] == 0 :
# # 						count += 1
# # 				# 구한 개수만큼을 현재 값에서 빼서 next에 저장
# # 				next[i][j] = matrix[i][j] - count
# # 				if next[i][j] < 0 : 
# # 					next[i][j] = 0
# # 	return next

# # def dfs(i, j, visited) : 
# # 	for d in dx: 
# # 		di = i + d[0]
# # 		dj = j + d[1]
# # 		if 0 <= di < n and 0 <= dj < m and not visited[di][dj] and matrix[di][dj] != 0 :
# # 			visited[di][dj] = True
# # 			dfs(di, dj, visited)

# # n, m = map(int, file.readline().split())
# # matrix = [list(map(int, file.readline().split())) for _ in range(n)]
# # answer = int(file.readline())

# # print(n, m, answer)
# # for mat in matrix : 
# # 	print(mat)

# # year = 0
# # dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# # while True :
# # 	year += 1

# # 	# 모든 얼음 녹았는고?
# # 	if meltAll() :
# # 		print(0)
# # 		break

# # 	# 같은 년도 영향 배타적으로
# # 	matrix = melt()

# # 	print("after melt")
# # 	for mat in matrix : 
# # 		print(mat)

# # 	# 다 녹였으니 덩어리 세기
# # 	# 개수 안 세도 됨 (1개 넘어가면 바로 return 때리기)
# # 	visited = [[False for _ in range(m)] for _ in range(n)]
# # 	count = 0
# # 	for i in range(n) : 
# # 		for j in range(m) : 
# # 			if matrix[i][j] != 0 and not visited[i][j] :
# # 				if count > 1 :
# # 					break
# # 				count += 1
# # 				dfs(i, j, visited)

# # 	if count > 1 :
# # 		print(year)
# # 		break


# # file.close()

# # # 백준 제출용
# # # # 해결방안 1번 : 
# # # # 단순 반복 + DFS
# # # # 녹이기.  + 덩어리 세기
# # # import sys
# # # import copy

# # # sys.setrecursionlimit(10 ** 9)

# # # # 다 녹았도다 -> True
# # # # 아직이도다. -> False
# # # def meltAll() : 
# # # 	for mat in matrix : 
# # # 		for ma in mat :
# # # 			if ma != 0 :
# # # 				return False
# # # 	return True

# # # # 녹이거라
# # # def melt() :
# # # 	next = copy.deepcopy(matrix)
# # # 	for i in range(1, n-1) : 
# # # 		for j in range(1, m-1) : 
# # # 			# 얼음인 애들 차례가 되면
# # # 			if matrix[i][j] != 0 :
# # # 				# 상하좌우에서 0인 개수를 찾아
# # # 				count = 0
# # # 				for d in dx :
# # # 					di = i + d[0]
# # # 					dj = j + d[1]
# # # 					if matrix[di][dj] == 0 :
# # # 						count += 1
# # # 				# 구한 개수만큼을 현재 값에서 빼서 next에 저장
# # # 				next[i][j] = matrix[i][j] - count
# # # 				if next[i][j] < 0 : 
# # # 					next[i][j] = 0
# # # 	return next

# # # def dfs(i, j, visited) : 
# # # 	for d in dx: 
# # # 		di = i + d[0]
# # # 		dj = j + d[1]
# # # 		if 0 <= di < n and 0 <= dj < m and not visited[di][dj] and matrix[di][dj] != 0 :
# # # 			visited[di][dj] = True
# # # 			dfs(di, dj, visited)

# # # n, m = map(int, sys.stdin.readline().split())
# # # matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# # # year = 0
# # # dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# # # while True :
# # # 	# 모든 얼음 녹았는고?
# # # 	if meltAll() :
# # # 		print(0)
# # # 		break

	
# # # 	# 다 녹이기 전에 덩어리 세기
# # # 	# 개수 안 세도 됨 (1개 넘어가면 바로 return 때리기)
# # # 	visited = [[False for _ in range(m)] for _ in range(n)]
# # # 	count = 0
# # # 	for i in range(n) : 
# # # 		for j in range(m) : 
# # # 			if matrix[i][j] != 0 and not visited[i][j] :
# # # 				if count > 1 :
# # # 					break
# # # 				count += 1
# # # 				dfs(i, j, visited)

# # # 	if count > 1 :
# # # 		print(year)
# # # 		break

# # # 	# 같은 년도 영향 배타적으로
# # # 	matrix = melt()

# # # 	year += 1