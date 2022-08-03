file = open("./dfs/빙산tc.txt", "r")

from collections import deque

# 녹이면서 해야할 것
# 1. 빙하 리스트 (icebug) 중 녹은 거 제거
# 2. 수정된 빙
def melt(icebug) : 
	# 녹이고
	for idx, ice in enumerate(icebug) : 
		i, j, h = ice
		count = 0 
		for d in dx :
			di = i + d[0]
			dj = j + d[1]
			if matrix[di][dj] == 0 :
				count += 1
		print("melt idx / count : ", idx, " / ", count)
		# 주변 물의 개수를 모두 셈
		# 높이가 0이하가 되면 0으로 하드코딩
		if h < count :
			icebug[idx] = (i, j, 0)
		# 높이가 1 이상이면 icebug에 높이 갱신
		else : 
			icebug[idx] = (i, j, h - count)
		print(icebug[i])

	print("after melting")
	print(icebug)
	
	# matrix 갱신하고
	result = []
	for ice in icebug :
		i, j, h = ice
		matrix[i][j] = h
		if h > 0 :
			result.append(ice)

	return result

def bfs(queue) : 
	while queue : 
		i, j = queue.popleft()

		# print(i, j)

		for d in dx : 
			di = i + d[0]
			dj = j + d[1]
			# 0이 아닌 곳만 가야 함
			if not visited[di][dj] and matrix[di][dj] != 0 :
				visited[di][dj] = True
				queue.append((di, dj))
	

for tc in range(3) : 
	n, m = map(int, file.readline().split())
	matrix = []
	icebug = []
	for i in range(n) : 
		line = list(map(int, file.readline().split()))
		for j, li in enumerate(line) : 
			if li != 0 :
				icebug.append((i, j, li))
		matrix.append(line)

	answer = int(file.readline())
	file.readline()

	print(n, m, answer)

	# 미리 빙하 위치 구하기
	print(icebug)

	year = 0 
	dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	while True : 
		
		# 빙산이 다 녹았는지
		if len(icebug) < 2: 
			print(0)
			break 
			
		# 덩어리 세기 BFS
		ice_count = 0
		visited = [[False for _ in range(m)] for _ in range(n)]
		for ice in icebug :
			i, j, h = ice
			if not visited[i][j] and matrix[i][j] != 0 :
				if ice_count > 1 :
					break
				ice_count += 1
				visited[i][j] = True
				bfs(deque([(i, j)]))

		# 두 덩어리인지 확인
		print(ice_count)
		if ice_count > 1 : 
			print(year)
			break

		# 녹이기
		icebug = melt(icebug)

		# year 증가
		year += 1
		
file.close()

# 백준 제출용
# from sys import stdin
# from collections import deque

# # 녹이면서 해야할 것
# # 1. 빙하 리스트 (icebug) 중 녹은 거 제거
# # 2. 수정된 빙
# def melt(icebug) : 
# 	# 녹이고
# 	for idx, ice in enumerate(icebug) : 
# 		i, j, h = ice
# 		count = 0 
# 		for d in dx :
# 			di = i + d[0]
# 			dj = j + d[1]
# 			if matrix[di][dj] == 0 :
# 				count += 1
# 		# print("melt idx / count : ", idx, " / ", count)
# 		# 주변 물의 개수를 모두 셈
# 		# 높이가 0이하가 되면 0으로 하드코딩
# 		if h < count :
# 			icebug[idx] = (i, j, 0)
# 		# 높이가 1 이상이면 icebug에 높이 갱신
# 		else : 
# 			icebug[idx] = (i, j, h - count)
# 		# print(icebug[i])

# 	# print("after melting")
# 	# print(icebug)
	
# 	# matrix 갱신하고
# 	result = []
# 	for ice in icebug :
# 		i, j, h = ice
# 		matrix[i][j] = h
# 		if h > 0 :
# 			result.append(ice)

# 	return result

# def bfs(queue) : 
# 	while queue : 
# 		i, j = queue.popleft()

# 		# print(i, j)

# 		for d in dx : 
# 			di = i + d[0]
# 			dj = j + d[1]
# 			# 0이 아닌 곳만 가야 함
# 			if not visited[di][dj] and matrix[di][dj] != 0 :
# 				visited[di][dj] = True
# 				queue.append((di, dj))
	

# n, m = map(int, stdin.readline().split())
# matrix = []
# icebug = []
# for i in range(n) : 
# 	line = list(map(int, stdin.readline().split()))
# 	for j, li in enumerate(line) : 
# 		if li != 0 :
# 			icebug.append((i, j, li))
# 	matrix.append(line)
# # answer = int(file.readline())
# # file.readline()

# # print(n, m, answer)

# # 미리 빙하 위치 구하기
# # print(icebug)

# year = 0 
# dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# while True : 
	
# 	# 빙산이 다 녹았는지
# 	if len(icebug) < 2: 
# 		print(0)
# 		break 
		
# 	# 덩어리 세기 BFS
# 	ice_count = 0
# 	visited = [[False for _ in range(m)] for _ in range(n)]
# 	for ice in icebug :
# 		i, j, h = ice
# 		if not visited[i][j] and matrix[i][j] != 0 :
# 			if ice_count > 1 :
# 				break
# 			ice_count += 1
# 			visited[i][j] = True
# 			bfs(deque([(i, j)]))

# 	# 두 덩어리인지 확인
# 	# print(ice_count)
# 	if ice_count > 1 : 
# 		print(year)
# 		break

# 	# 녹이기
# 	icebug = melt(icebug)

# 	# year 증가
# 	year += 1
