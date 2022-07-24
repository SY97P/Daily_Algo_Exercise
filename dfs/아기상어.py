# 해결방안 1번 :
# dfs
# 1) 일단 무게는 무시하고 그냥 dfs, bfs 탐색이 잘 되는지부터 확인
# 	1-1) dfs에선 visited 개념이 없어져야 함
# 	1-2) bfs에선 visited 개념이 필요함(bfs 종료 후 유지할 필요 없음)
# 2) 무게 조건 설정 (아기상어 무게, 먹은 물고기 수)
# 	2-1) 우선순위 조정 : 거리 멀지만 먹을 수 있는 물고기 > 이동만 가능한 물고기
# 3) 무게 증가 제어
# 4) 예외처리

from collections import deque

file = open("./dfs/아기상어tc.txt", "r")

def calculate(weight, prey) :
	# 재귀 이전 : prey = prey + 1
	# 재귀 이후 : prey = prey - 1
	if prey == weight : 
		return weight + 1, 0
	elif prey < 0 :
		return weight - 1, weight - 2
	return weight, prey
	

def bfs(queue, matrix, weight) : 
	while queue :
		i, j, visited, count = queue.popleft()

		# 종료조건
		# 해당좌표에 값이 있으면 종료
		# return (좌표, 이동한 거리)
		# 2) 무게 조건 설정 -> 무게가 같아 먹지는 못하고 이동만 가능한 경우에는 종료하지 않음 (먹을 수 있는 경우만 종료)
		if matrix[i][j] != 0 and weight > matrix[i][j] : 
			return (i, j), count

		for d in dx : 
			di = i + d[0]
			dj = j + d[1]

			# 2) 무게조건 설정 -> 이동할 수 있는 경우면 모조리 큐에 추가
			if 0 <= di < n and 0 <= dj < n and not visited[di][dj] and weight >= matrix[di][dj] :
				visited[di][dj] = True
				queue.append((di, dj, visited, count + 1))
				visited[di][dj] = False
	return -1
			

# def dfs(i, j, matrix, visited, fishes) : 
	# print(i, j, matrix[i][j], visited[i][j], fishes)
def dfs(i, j, matrix, fishes, weight, prey) : 
	print(i, j, matrix[i][j], fishes)

	# 종료 조건
	# 더이상 잡을 물고기가 없으면 됨. 
	if fishes <= 0 : 
		# 여기부터 다시 재귀를 되돌아가면서 1씩 증가해서 반환
		return 0

	# 주변에 0인 값이 하나도 없는지
	no_prey = True
	# 사방을 돌아다니면서 0이 아닌 곳을 찾아서 이동함
	for d in dx : 
		di = i + d[0]
		dj = j + d[1]
		
		# 방문한 적 없으면서 0이 아닌 곳
		# 1-1) -> 방문한 곳은 이미 0 (visited 필요 없음)
		# 2) 무게 조건 설정 (아기상어가 해당 물고기 무게보다 크거나 같아야 이동 가능)
		# 2-1) 우선순위 조정
		if 0 <= di < n and 0 <= dj < n and matrix[di][dj] != 0 and weight > matrix[di][dj] :
			
			# 0이 아닌 곳이 하나는 있다.
			# 이동만 했더라도 어쨌든 0을 뛰어넘지는 않아도 됨.
			no_prey = False
			
			# 2-1) 우선순위 조정
			# 이쪽 방향으로 dfs를 수행한다.
			# 해당 물고기를 먹지 못하는 경우 (무게가 같을 때)
			# if weight == matrix[di][dj] : 
			# 	# 해당 물고기를 0으로 만들지 말고, 남은 물고기 개수를 줄이지도 말고
			# 	# 그냥 이동만 함
			# 	return 1 + dfs(di, dj, matrix, fishes)
			
			# 해당 물고기를 먹은 경우
			# 해당 물고기를 0으로 만들어버림
			# else : 
			temp = matrix[di][dj]
			matrix[di][dj] = 0
			# 3) 무게증가
			weight, prey = calculate(weight, prey + 1)
			# return 1 + dfs(di, dj, matrix, visited, fishes - 1)
			return 1 + dfs(di, dj, matrix, fishes - 1, weight, prey)
			# 재귀 복귀 시 원상복구
			matrix[di][dj] = temp
			weight, prey = calculate(weight, prey - 1)

	# 사방에 0뿐이거나 이동만 가능한 녀석들만 있는 경우 (현재 노드에서 먹이를 먹지 못한 경우)
	# bfs 사용
	if no_prey :
		
		# 1-2)
		# 한 번의 bfs에서 다음 좌표를 찾을 수 있다는 보장 가능
		# 따라서 bfs마다 False로 초기화된 (시작좌표 제외) visited 필요
		visited = [[False for _ in range(n)] for _ in range(n)]
		visited[i][j] = True
		
		return_Value = bfs(deque([(i, j, visited, 0)]), matrix, weight)
		
		if return_Value != -1 :
			(next_i, next_j), dist = return_Value
			print("next_i, next_j, dist : ", next_i, next_j, dist)
		else : 
			return 0

		# bfs로 구한 가장 가까운 물고기 위치로 이동
		# 기존 방식으로는 한 칸씩 움직였기 때문에 +1이지만 지금은 +dist 여야 함.
		# 이동할 좌표에서 다시 dfs를 해야 함. 
		# 해당좌표를 이미 진입했다는 가정이므로 visited, matrix, fishes를 조정
		temp = matrix[next_i][next_j]
		matrix[next_i][next_j] = 0
		# visited[next_i][next_j] = True
		# return dist + dfs(next_i, next_j, matrix, visited, fishes - 1)
		# visited[next_i][next_j] = False
		# 3) 무게증가
		weight, prey = calculate(weight, prey + 1)
		return dist + dfs(next_i, next_j, matrix, fishes - 1, weight, prey)
		matrix[next_i][next_j] = temp
		weight, prey = calculate(weight, prey - 1)

for _ in range(6) : 
	n = int(file.readline())
	fishes = 0
	start_i = start_j = 0
	matrix = []
	for i in range(n) : 
		line = list(map(int, file.readline().split()))
		for j, li in enumerate(line) : 
			if li != 0 and li != 9 : 
				fishes += 1
			if li == 9 : 
				start_i, start_j = i, j
		matrix.append(line)
	answer = int(file.readline())
	file.readline()

	print("n, fishes, answer : ", n, fishes, answer)
	print("start_i, start_j : ", start_i, start_j)
	for mat in matrix : 
		print(mat)

	dx = [(-1, 0), (0, -1), (0, 1), (1, 0)]
	# 1-1)
	# visited = [[False for _ in range(n)] for _ in range(n)]
	# visited[start_i][start_j] = True
	matrix[start_i][start_j] = 0
	# result = dfs(start_i, start_j, matrix, visited, fishes)
	# 2) 무게조건 설정
	weight, prey = 2, 0
	result = dfs(start_i, start_j, matrix, fishes, weight, prey)
	print("result : ", result)
		
	print()

file.close()