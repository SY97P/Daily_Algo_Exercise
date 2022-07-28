# 해결방안 1번 : 
# BFS
from collections import deque

file = open("./bfs/인구이동tc.txt", "r")

# union = [(i, j)]
def movement(union) :
	# 평균값 구하기
	sum = 0
	for nation in union : 
		i, j = nation
		sum += matrix[i][j]
	sum //= len(union)

	# 구해진 평균값을 matrix에 갱신해주기
	for nation in union : 
		i, j = nation
		matrix[i][j] = sum
		united[i][j] = True

# 연합 만들어주기
def bfs(queue) : 
	while queue : 
		i, j = queue.popleft()

		# print(i, j, matrix[i][j])

		# 상하좌우로 이동하되, l이상 r이하인 것만
		for d in dx : 
			di = i + d[0]
			dj = j + d[1]
			if 0 <= di < n and 0 <= dj < n and not united[di][dj] and not visited[di][dj] and l <= abs(matrix[di][dj] - matrix[i][j]) <= r :
				visited[di][dj] = True
				unions[index].append((di, dj))
				queue.append((di, dj))
				

for tc in range(5) : 
	n, l, r = map(int, file.readline().split())
	matrix = [list(map(int, file.readline().split())) for _ in range(n)]
	answer = int(file.readline())
	file.readline()

	# if tc >= 3 : 
	# 	continue

	print(n,l, r)
	for mat in matrix :
		print(mat)

	days = 0
	united = [[False for _ in range(n)] for _ in range(n)]
	while True :
		# 연합 list
		unions = []
		index = 0

		# 연합 만들기용 visited 2차원
		visited = [[False for _ in range(n)] for _ in range(n)]

		dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

		for i in range(n) :
			for j in range(n) : 
				if not visited[i][j] : 
					# bfs 내에서 연합을 만들어서 unions에 append
					visited[i][j] = True
					unions.append([(i, j)])
					bfs(deque([(i,j)]))
					index += 1

		print(unions, index)
		print(len(unions), index)

		# 종료조건
		# 만들어진 연합의 개수가 모든 나라의 수와 같으면 인구이동이 앞으로 더 없다는 뜻
		if len(unions) >= n * n :
			break

		# 인구이동 logic
		days += 1
		# 연합마다 인구이동을 해줘야 함.
		# 연합원이 1인 것은 안 함
		for union in unions : 
			if len(union) > 1 :
				movement(union)

		for mat in matrix :
			print(mat)
	
	
	print(days)
	print()


file.close()

# 백준 제출용
# 해결방안 1번 : 
# BFS
from collections import deque
from sys import stdin

# union = [(i, j)]
def movement(union) :
	# 평균값 구하기
	sum = 0
	for nation in union : 
		i, j = nation
		sum += matrix[i][j]
	sum //= len(union)

	# 구해진 평균값을 matrix에 갱신해주기
	for nation in union : 
		i, j = nation
		matrix[i][j] = sum

# 연합 만들어주기
def bfs(queue) : 
	while queue : 
		i, j = queue.popleft()

		# print(i, j, matrix[i][j])

		# 상하좌우로 이동하되, l이상 r이하인 것만
		for d in dx : 
			di = i + d[0]
			dj = j + d[1]
			if 0 <= di < n and 0 <= dj < n and not visited[di][dj] and l <= abs(matrix[di][dj] - matrix[i][j]) <= r :
				visited[di][dj] = True
				unions[index].append((di, dj))
				queue.append((di, dj))
				

n, l, r = map(int, stdin.readline().split())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]

days = 0
while True :
	# 연합 list
	unions = []
	index = 0

	# 연합 만들기용 visited 2차원
	visited = [[False for _ in range(n)] for _ in range(n)]

	dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

	for i in range(n) :
		for j in range(n) : 
			if not visited[i][j] : 
				# bfs 내에서 연합을 만들어서 unions에 append
				visited[i][j] = True
				unions.append([(i, j)])
				bfs(deque([(i,j)]))
				index += 1

	# 종료조건
	# 만들어진 연합의 개수가 모든 나라의 수와 같으면 인구이동이 앞으로 더 없다는 뜻
	if len(unions) >= n * n :
		break

	# 인구이동 logic
	days += 1
	# 연합마다 인구이동을 해줘야 함.
	# 연합원이 1인 것은 안 함
	for union in unions : 
		if len(union) > 1 :
			movement(union)


print(days)