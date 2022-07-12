from collections import deque

def bfs(coordi, visited) : 
	i, j = coordi
	

file = open("./bfs/토마토tc.txt", "r")

for _ in range(5) : 
	m, n = map(int, file.readline().split())
	matrix = [list(file.readline().split()) for _ in range(n)]
	answer = int(file.readline())
	file.readline()

	print(n, m, answer)
	for mat in matrix : 
		print(mat)

	if "0" not in matrix : 
		print(0)
	elif "1" not in matrix : 
		print(-1)
	else :
		count = [[0 for _ in range(m)] for _ in range(n)]

		for i in range(n) : 
			for j in range(m) : 
				if matrix[i][j] == "1" :
			# 매 bfs마다 visited 초기화
					visited = [[False for _ in range(m)] for _ in range(n)]
					visited[i][j] = True
					bfs(deque([(i,j)]), visited)

		# 구해진 count 에서 최대값을 구하면 된다.
		print(max(count))

	print()

file.close()