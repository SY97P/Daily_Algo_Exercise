
# 이유는 모르겠으나 안 풀림 -> 새로 풀어보자
# import sys
# from collections import deque

# file = open("./bfs/연구소tc.txt", "r")

# # 방 개수 구해
# def bfs() : 
# 	# 바이러스 있는 방의 좌표부터 큐에 넣어두셈
# 	queue = deque()
# 	for i in range(n) : 
# 		for j in range(m) : 
# 			if matrix[i][j] == 2 :
# 				queue.append((i, j))

# 	temp = matrix

# 	while queue :
# 		i, j = queue.popleft()

# 		for d in dx : 
# 			di = i + d[0]
# 			dj = j + d[1]
# 			if 0 <= di < n and 0 <= dj < m and temp[di][dj] == 0 : 
# 				temp[di][dj] = 2
# 				queue.append((di, dj))

# 	result = 0
# 	for i in range(n) : 
# 		for j in range(m) : 
# 			if temp[i][j] == 0 : 
# 				result += 1
# 	count_list.add(result)


# # 벽을 세워
# def buildWall(wall_count) : 
# 	# 3개 다 세웠으면 안전한 방의 개수를 구하러 가셈
# 	if wall_count == 3: 
# 		# 방 개수 구해
# 		bfs()
# 		return

# 	# 벽을 세우는 모든 경우의 수를 구해야 함. 
# 	for i in range(n) : 
# 		for j in range(m) : 
# 			# 0인 값의 방이면 다 됨
# 			if matrix[i][j] == 0 : 
# 				matrix[i][j] = 1
# 				buildWall(wall_count + 1)
# 				matrix[i][j] = 0

# for _ in range(1) : 
# 	n, m = map(int, file.readline().split())
# 	matrix = [list(map(int, file.readline().split())) for _ in range(n)]
# 	answer = int(file.readline())
# 	file.readline()

# 	print(n, m, answer)
# 	for mat in matrix : 
# 		print(mat)

# 	# 벽을 먼저 세워
# 	dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 	count_list = set()
# 	buildWall(0)
# 	print(count_list)
# 	print(max(count_list))

# file.close()