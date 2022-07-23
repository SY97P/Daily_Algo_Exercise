
# 1번 : dfs로 이동만해서 몇번 움직이는지 반환하도록 함
# 2번 : weight가 어떻게 변화하는지 따옴
file = open("./dfs/아기상어tc.txt", "r")

def dfs(i, j, visited, minimap, fishes, weight, habitat) : 
	print(i, j, visited[i][j], minimap[i][j], fishes, weight)
	if fishes <= 0 : 
		return 1

	# 주변에 0이 아닌게 있긴 함
	only0 = True
	for d in dx : 
		di = i + d[0]
		dj = j + d[1]
		if 0 <= di < n and 0 <= dj < n and not visited[di][dj] and matrix[di][dj] != 0 and matrix[di][dj] <= weight :
			only0 = False
			temp = minimap[di][dj]
			minimap[di][dj] = 0
			visited[di][dj] = True
			return 1 + dfs(di, dj, visited, minimap, fishes - 1, weight, habitat + 1)
			visited[di][dj] = False
			minimap[di][dj] = temp

	# 주변에 모두 0임
	if only0 :
		for d in dx : 
			di = i + d[0]
			dj = j + d[1]
			if 0 <= di < n and 0 <= dj < n and not visited[di][dj] :
				visited[di][dj] = True
				return 1 + dfs(di, dj, visited,  minimap, fishes, weight, habitat)
				visited[di][dj] = False

for tc in range(6) : 
	n = int(file.readline())
	start_i = start_j = 0
	fishes = 0
	matrix = []
	for i in range(n) : 
		line = list(map(int, file.readline().split()))
		for idx, li in enumerate(line) : 
			if li != 0 and li != 9 : 
				fishes += 1
			if li == 9 :
				start_i = i
				start_j = idx
		matrix.append(line)
	answer = int(file.readline())
	file.readline()

	print("n, fishes, answer : ", n, fishes, answer)
	print("start_i, start_j : ", start_i, start_j)
	for mat in matrix : 
		print(mat)

	if fishes > 0 :
		weight = 9
		dx = [(-1, 0), (0, -1), (0, 1), (1, 0)]
		visited = [[False for _ in range(n)] for _ in range(n)]
		visited[start_i][start_j] = True
		result = dfs(start_i, start_j, visited, matrix, fishes, weight, 0)
		print(result)
	else : 
		print(0)


	print()

file.close()