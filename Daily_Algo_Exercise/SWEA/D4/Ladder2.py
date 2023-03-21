#1 18
#2 96
#3 16
#4 5
#5 99
#6 0
#7 97
#8 0
#9 62
#10 3

file = open("./SWEA/D4/Ladder2.txt", "r")

input = file.readline

def dfs(i, j, depth) :
	if i == 99 : 
		return depth

	for dx, dy in d : 
		di = i + dx
		dj = j + dy
		if 0 <= di < 100 and 0 <= dj < 100 and matrix[di][dj] == 1 and not visited[di][dj] : 
			visited[di][dj] = True
			return dfs(di, dj, depth + 1)

for _ in range(10) : 
	tc = int(input())
	matrix = [list(map(int, input().split())) for _ in range(100)]

	start_list = []

	d = [(0, -1), (0, 1), (1, 0)]

	for idx, val in enumerate(matrix[0]) :
		if val == 1 : 
			start_list.append(idx)

	# print(start_list)

	min_start = -1
	min_count = float('inf')

	for start in start_list : 
		visited = [[False for _ in range(100)] for _ in range(100)]
		visited[0][start] = True
		count = dfs(0, start, 1)
		# print(start, count)
		if count < min_count :
			min_start = start
			min_count = count

	print("#%d %d" % (tc, min_start))

file.close()