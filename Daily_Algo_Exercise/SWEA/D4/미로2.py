#1 1
#2 1
#3 1
#4 0
#5 0
#6 1
#7 1
#8 0
#9 1
#10 0

file = open("./SWEA/D4/미로2.txt", "r")

input = file.readline

from collections import deque

def bfs(q) :
	while q : 
		i, j = q.popleft()

		for dx, dy in d : 
			di = i + dx
			dj = j + dy
			if 0 <= di < 100 and 0 <= dj < 100 and not visited[di][dj] and matrix[di][dj] != 1: 
				visited[di][dj] = True
				q.append((di, dj))

for _ in range(10) : 
	tc = int(input())
	matrix = []
	start, end = tuple(), tuple()
	for i in range(100) : 
		line = list(map(int, input().strip()))
		for j in range(100) : 
			if line[j] == 2 : 
				start = (i, j)
			elif line[j] == 3 : 
				end = (i, j)
		matrix.append(line)

	# print(start, end)

	d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

	visited = [[False for _ in range(100)] for _ in range(100)]

	visited[start[0]][start[1]] = True

	bfs(deque([start]))

	if visited[end[0]][end[1]] : 
		print("#%d %d" %(tc, 1))
	else : 
		print("#%d %d" %(tc, 0))

file.close()