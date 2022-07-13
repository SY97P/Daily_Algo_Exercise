# 해결방안 3 : 아몰라악
from collections import deque

file = open("./bfs/토마토tc.txt", "r")

def bfs() :
	queue = deque()

	# 시작할 곳 (1인 값)을 queue에 넣어줌
	for i in range(n) : 
		for j in range(m) : 
			if matrix[i][j] == 1 : 
				queue.append((i, j))

	# bfs 시작
	while queue : 
		i, j = queue.popleft()

		for d in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
			di = i + d[0]
			dj = j + d[1]
			if 0 <= di < n and 0 <= dj < m and matrix[di][dj] == 0 :
				matrix[di][dj] = matrix[i][j] + 1
				queue.append((di, dj))
	

for _ in range(7) : 
	m, n = map(int, file.readline().split())
	matrix = [list(map(int, file.readline().split())) for  _ in range(n)]
	answer = int(file.readline())
	print("answer : ", answer)
	file.readline()

	bfs()

	if any(0 in mat for mat in matrix) :
		print(-1)
	else :
		print(max(max(matrix)) - 1)


file.close()

# 백준 제출용
import sys
from collections import deque

def bfs() :
	queue = deque()

	# 시작할 곳 (1인 값)을 queue에 넣어줌
	for i in range(n) : 
		for j in range(m) : 
			if matrix[i][j] == 1 : 
				queue.append((i, j))

	# bfs 시작
	while queue : 
		i, j = queue.popleft()

		for d in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
			di = i + d[0]
			dj = j + d[1]
			if 0 <= di < n and 0 <= dj < m and matrix[di][dj] == 0 :
				matrix[di][dj] = matrix[i][j] + 1
				queue.append((di, dj))

m, n = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

bfs()

if any(0 in mat for mat in matrix) :
	print(-1)
else :
	print(max(max(matrix)) - 1)


# # 해결방법 2 : 시간초과 개선안 -> 최소보장을 못함
# # 0인 칸만 연산하도록 수정
# from collections import deque

# file = open("./bfs/토마토tc.txt", "r")

# def bfs(queue, visited) : 
# 	while queue : 
# 		i, j = queue.popleft()

# 		# 사방으로 갈 수 있는 거 찾기
# 		for d in dx : 
# 			di, dj = d
# 			di += i
# 			dj += j
# 			# 0일 때만 진행 -> 아래 확인을 모두 해주기로 변경
# 			# -1(없을 때), 1(이후로는 최소가 아님이 보장됨)
# 			if 0 <= di < n and 0 <= dj < m and matrix[di][dj] != 1 and matrix[di][dj] != 1 : 
# 				print(di, dj)
# 				matrix[di][dj] = matrix[i][j] + 1 if matrix[di][dj] == 0 else min(matrix[di][dj], matrix[i][j] + 1)
# 				queue.append((di, dj))

# for _ in range(8) : 
# 	m, n = map(int, file.readline().split())
# 	matrix = [list(map(int, file.readline().split())) for _ in range(n)]
# 	answer = int(file.readline())
# 	file.readline()

# 	print(n, m, answer)
# 	for mat in matrix : 
# 		print(mat)

# 	if all(0 not in mat for mat in matrix) : 
# 		print(0)
# 	else :
	
# 		dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	
# 		# logic 
# 		for i in range(n) : 
# 			for j in range(m) : 
# 				if matrix[i][j] == 1 : 
# 					bfs(deque([(i, j)]))
	
# 		print()
# 		for mat in matrix : 
# 			print(mat)
	
		
# 		# 모두 익힐 수 없을 때 = 0이 남아있음
# 		if any(0 in matr for matr in matrix) : 
# 			print(-1)
# 		# 모두 익어 있는 상태 = 1이랑 -1만 있음 -> 초기 처리
		 
# 		# 그 외엔 matrix에서 최대값 선택
# 		else : 
# 			print(max(max(matrix))-1)
	
# 		print()
	
# file.close()

# 백준 제출용
# import sys
# from collections import deque

# def bfs(queue) : 
# 	while queue : 
# 		i, j = queue.popleft()

# 		# 사방으로 갈 수 있는 거 찾기
# 		for d in dx : 
# 			di, dj = d
# 			di += i
# 			dj += j
# 			# 0일 때만 진행
# 			# -1(없을 때), 1(이후로는 최소가 아님이 보장됨)
# 			if 0 <= di < n and 0 <= dj < m and matrix[di][dj] == 0 : 
# 				matrix[di][dj] = matrix[i][j] + 1
# 				queue.append((di, dj))
				
# m, n = map(int, sys.stdin.readline().split())
# matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# if all(0 not in mat for mat in matrix) : 
# 	print(0)
# else :
# 	dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 	# logic 
# 	for i in range(n) : 
# 		for j in range(m) : 
# 			if matrix[i][j] == 1 : 
# 				bfs(deque([(i, j)]))
	
# 	# 모두 익힐 수 없을 때 = 0이 남아있음
# 	if any(0 in matr for matr in matrix) : 
# 		print(-1)
# 	# 모두 익어 있는 상태 = 1이랑 -1만 있음 -> 초기 처리
	 
# 	# 그 외엔 matrix에서 최대값 선택
# 	else : 
# 		print(max(max(matrix))-1)

# 해결방법 1 : 시간초과 (수정하기 귀찮아서 다시 쓰려함)
# 1인 칸에서 시작함
# 다른 1인 칸도 무시하고 계속 연산
# from collections import deque

# def bfs(queue, visited) :
# 	while queue : 
# 		(i, j), count = queue.popleft()

# 		# count_list 초기값은 -1
# 		# 초기값인 경우엔 그냥 count를 해주고 
# 		# 초기값이 아닌 경우엔 기존값 / count 중 min을 선택
# 		count_list[i][j] = min(count, count_list[i][j]) if count_list[i][j] != -1 else count

# 		# 인접한 노드로 이동
# 		for d in dx : 
# 			di, dj = d
# 			if 0 <= i+di < n and 0 <= j+dj < m and matrix[i+di][j+dj] != -1 and not visited[i+di][j+dj] :
# 				visited[i+di][j+dj] = True
# 				queue.append(((i+di, j+dj), count + 1))
		

# file = open("./bfs/토마토tc.txt", "r")

# for _ in range(5) : 
# 	m, n = map(int, file.readline().split())
# 	matrix = [list(map(int, file.readline().split())) for _ in range(n)]
# 	answer = int(file.readline())
# 	file.readline()

# 	print(n, m, answer)
# 	for mat in matrix : 
# 		print(mat)
# 	print()

# 	if all(0 not in ma for ma in matrix) : 
# 		# print("0 exception")
# 		print(0)
# 	elif all(1 not in ma for ma in matrix) :
# 		# print("-1 exception")
# 		print(-1)
# 	else :
# 		count_list = [[-1 for _ in range(m)] for _ in range(n)]
# 		dx = [(1, 0), (-1, 0), (0, -1), (0, 1)]

# 		for i in range(n) : 
# 			for j in range(m) : 
# 				if matrix[i][j] == 1 :
# 					# 매 bfs마다 visited 초기화
# 					visited = [[False for _ in range(m)] for _ in range(n)]
# 					visited[i][j] = True
# 					bfs(deque([((i,j), 0)]), visited)


# 		# 구해진 count 에서 최대값을 구하면 된다.
# 		print("count_list")
# 		for c in count_list :
# 			print(c)

# 		print("result ")
# 		# matrix가 0이면서 count_list가 -1인 값이 있으면 -1 출력
# 		is_exception = False
# 		for i in range(n) : 
# 			for j in range(m) : 
# 				if matrix[i][j] == 0 and count_list[i][j] == -1 : 
# 					is_exception = True
# 					break
# 		if is_exception : 
# 			print(-1)
# 		else : 
# 			maxValue = max(co for co in count_list)
# 			print(max(maxValue))
		

# 	print()

# file.close()

# # 백준 제출용
# import sys
# from collections import deque

# def bfs(queue, visited) :
# 	while queue : 
# 		(i, j), count = queue.popleft()

# 		# count_list 초기값은 -1
# 		# 초기값인 경우엔 그냥 count를 해주고 
# 		# 초기값이 아닌 경우엔 기존값 / count 중 min을 선택
# 		count_list[i][j] = min(count, count_list[i][j]) if count_list[i][j] != -1 else count

# 		# 인접한 노드로 이동
# 		for d in dx : 
# 			di, dj = d
# 			if 0 <= i+di < n and 0 <= j+dj < m and matrix[i+di][j+dj] == 0 and not visited[i+di][j+dj] :
# 				visited[i+di][j+dj] = True
# 				queue.append(((i+di, j+dj), count + 1))
		
# m, n = map(int, sys.stdin.readline().split())
# matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# count_list = [[-1 for _ in range(m)] for _ in range(n)]
# dx = [(1, 0), (-1, 0), (0, -1), (0, 1)]

# for i in range(n) : 
# 	for j in range(m) : 
# 		if matrix[i][j] == 1 :
# 			# 매 bfs마다 visited 초기화
# 			visited = [[False for _ in range(m)] for _ in range(n)]
# 			visited[i][j] = True
# 			bfs(deque([((i,j), 0)]), visited)

# # matrix가 0이면서 count_list가 -1인 값이 있으면 -1 출력
# is_exception = False
# for i in range(n) : 
# 	for j in range(m) : 
# 		if matrix[i][j] == 0 and count_list[i][j] == -1 : 
# 			is_exception = True
# 			break
# if is_exception : 
# 	print(-1)
# else : 
# 	# 구해진 count 에서 최대값을 구하면 된다.
# 	maxValue = max(co for co in count_list)
# 	print(max(maxValue))