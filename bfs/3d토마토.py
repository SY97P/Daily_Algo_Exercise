from collections import deque

file = open("./bfs/3d토마토tc.txt", "r")

def bfs(queue) : 
	while queue : 
		k, i, j = queue.popleft()

		for d in dx :
			dk = k + d[0]
			di = i + d[1]
			dj = j + d[2]
			if 0 <= dk < h and 0 <= di < n and 0 <= dj < m and  matrix[dk][di][dj] == 0 :
				matrix[dk][di][dj] = matrix[k][i][j] + 1
				queue.append((dk, di, dj))

for _ in range(6) :
	m, n, h = map(int, file.readline().split())
	matrix = [[list(map(int, file.readline().split())) for _ in range(n)] for _ in range(h)]
	answer = int(file.readline())
	file.readline()

	print("m, n, h : ", m, n, h)
	print("answer : ", answer)
	for i, mat in enumerate(matrix) :
		print(i, "번째 상자")
		for ma in mat :
			print(ma)
	print()

	# 방향 (위, 아래, 앞, 뒤, 왼, 오)
	dx = [
		(-1, 0, 0), (1, 0, 0),
		(0, 1, 0), (0, -1, 0),
		(0, 0, -1), (0, 0, 1)
	]

	# 1인 좌표를 미리 구해놓음
	queue = deque()
	for k in range(h) :
		for i in range(n) :
			for j in range(m) :
				# print(matrix[k][i][j])
				if matrix[k][i][j] == 1 :
				 	queue.append((k, i, j))
	print(queue)

	bfs(queue)

	for mat in matrix :
		print("상자")
		for ma in mat :
			print(ma)
	
	if not all(0 not in ma for ma in  mat for mat in matrix) :
		print("result : ", -1)
	# elif all(-1 in ma for ma in mat for mat in matrix) :
	# 	print(0)
	else : 
		# print("result : ", max(map(max, list(map(max, matrix)))) - 1)
		print(max(map(max, map(max, matrix))) - 1)

	print("------------------------")	
	print()

	

file.close()


# 백준 제출용
# from sys import stdin
# from collections import deque

# def bfs(queue) : 
# 	while queue : 
# 		k, i, j = queue.popleft()

# 		for d in dx :
# 			dk = k + d[0]
# 			di = i + d[1]
# 			dj = j + d[2]
# 			if 0 <= dk < h and 0 <= di < n and 0 <= dj < m and not visited[dk][di][dj] and matrix[dk][di][dj] == 0 :
# 				visited[dk][di][dj] = True
# 				matrix[dk][di][dj] = matrix[k][i][j] + 1
# 				queue.append((dk, di, dj))

# m, n, h = map(int, stdin.readline().split())
# matrix = [[list(map(int, stdin.readline().split())) for _ in range(n)] for _ in range(h)]

# # logic
# visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]

# # 방향 (위, 아래, 앞, 뒤, 왼, 오)
# dx = [
# 	(-1, 0, 0), (1, 0, 0),
# 	(0, 1, 0), (0, -1, 0),
# 	(0, 0, -1), (0, 0, 1)
# ]

# # 1인 좌표를 미리 구해놓음
# queue = deque()
# for k in range(h) :
# 	for i in range(n) :
# 		for j in range(m) :
# 			# print(matrix[k][i][j])
# 			if matrix[k][i][j] == 1 :
# 				queue.append((k, i, j))

# bfs(queue)

# if not all(0 not in ma for ma in (mat for mat in matrix)) :
# 	print(-1)
# else : 
# 	print(max(map(max, list(map(max, matrix)))) - 1)