#1 67
#2 45
#3 39
#4 24
#5 91
#6 93
#7 90
#8 4
#9 99
#10 35

file = open("./SWEA/D4/Ladder1.txt", "r")

input = file.readline

from collections import deque

# def bfs(q) :
# 	global r, c

# 	d = [(0, -1), (0, 1), (-1, 0)]

# 	result = 0

# 	while q : 
# 		i, j = q.popleft()

# 		print(i, j)

# 		if i == 0 : 
# 			result = j
# 			break

# 		for dx, dy in d : 
# 			di = i + dx
# 			dj = j + dy
# 			if 0 <= di < r and 0 <= dj < c and not visited[di][dj] and matrix[di][dj] == 1 : 
# 				if di != i : 
# 					visited[di][dj] = True
# 					q.append((di, dj))
# 				else :
# 					k = 0
# 					while 0 <= dj + k < c and matrix[di][dj+k] == 1: 
# 						visited[di][dj+k] = True
# 						if dj < j : 
# 							k -= 1
# 						else :
# 							k += 1
# 					if dj < j :
# 						q.append((di, dj+k+1))
# 					else: 
# 						q.append((di, dj+k-1))

# 	return result

def dfs(i, j, r, c) : 
	if i == 0 : 
		return j

	for dx, dy in d : 
		di = i + dx
		dj = j + dy
		if 0 <= di < r and 0 <= dj < c and not visited[di][dj] and matrix[di][dj] == 1 :
			visited[di][dj] = True
			return dfs(di, dj, r, c)
	
	
for _ in range(10) : 
	tc = int(input())
	
	matrix = [list(map(int, input().split())) for _ in range(100)]

	# if tc != 1 : 
	# 	continue

	end_point = 0

	for i in range(len(matrix[-1])) :
		if matrix[-1][i] == 2 : 
			end_point = i
			break
	
	r, c = len(matrix), len(matrix[0])

	d = [(0, -1), (0, 1), (-1, 0)]

	visited = [[False for _ in range(c)] for _ in range(r)]
	visited[r-1][end_point] = True
	
	# start_point = bfs(deque([(r - 1, end_point)]))
	start_point = dfs(r - 1, end_point, r, c)

	print("#%d %d" % (tc, start_point))

file.close()