# 해결방안 1, 2 망함
# 짜증나서 지워버림
# 3트 가즈아
import copy
from collections import deque

file = open("./bfs/연구소tc.txt", "r")

def bfs() :
	visited = [[False for _ in range(n)] for _ in range(m)]

	# copy 
	worldmap = copy.copy(world)
	queue = deque()
	for i in range(n) :
		for j in range(m) : 
			if worldmap[i][j] == 2  :
				queue.append((i, j))
	
	while queue : 
		i, j = queue.popleft()
	
		for d in dx : 
			di = i + d[0]
			dj = j + d[1]
			if 0 <= di < n and 0 <= dj < m and not visited[di][dj] and worldmap[di][dj] == 0 :
				visited[di][dj] = True
				worldmap[di][dj] = 2
				queue.append((di, dj))

def dfs(count) : 
	if count == 3 :
		bfs()
		return

	for i in range(n) : 
		for j in range(m) : 
			if world[i][j] == 0 :
				world[i][j] = 1
				dfs(count + 1)
				world[i][j] = 0
	

for _ in range(3) : 
	n, m = map(int, file.readline().split())
	world = [list(map(int, file.readline().split())) for _ in range(n)]
	answer = int(file.readline())
	file.readline()

	print(n, m, answer)
	for w in world : 
		print(w)

	max_safe = 0
	dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	lst = deque([])
	for i in range(n) : 
		for j in range(m) : 
			if world[i][j] == 2 : 
				lst.append((i, j))
				
	dfs(0)

	print(max_safe)

	print()


file.close()