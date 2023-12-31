#1 1
#2 1
#3 1
#4 0
#5 1
#6 1
#7 0
#8 1
#9 1
#10 1

file = open("./SWEA/D4/미로1.txt", "r")

input = file.readline

def dfs(i, j) : 
	global reachibility, end

	# print(i, j)
	
	for dx, dy in d : 
		di = dx + i 
		dj = dy + j
		if 0 <= di < 16 and 0 <= dj < 16 and not visited[di][dj] and (matrix[di][dj] == 0 or matrix[di][dj] == 3) : 
			if matrix[di][dj] == 3 : 
				reachibility = True
				return True
			visited[di][dj] = True
			if dfs(di, dj) : 
				return True
			visited[di][dj] = False
			

for _ in range(10) : 
	tc = int(input())
	matrix = []
	start = end = tuple()
	for i in range(16) : 
		line = list(map(int, list(input().strip())))
		for j, li in enumerate(line) : 
			if li == 2 : 
				start = (i, j)
			elif li == 3 :
				end = (i, j)
		matrix.append(line)

	# if tc != 1: 
	# 	continue
	# print(tc, start, end)

	reachibility = False
	d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	visited = [[False for _ in range(16)] for _ in range(16)]
	visited[start[0]][start[1]] = True

	dfs(start[0], start[1])

	print("#%d %d" % (tc, 1 if reachibility else 0))

file.close()