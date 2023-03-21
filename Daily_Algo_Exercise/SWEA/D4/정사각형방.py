#1 6 8
#2 3 2
#3 149 2
#4 2 45
#5 2 23
#6 1 2
#7 1 4
#8 5 17
#9 4 2
#10 1 35
#11 2 2
#12 7 2
#13 45 2
#14 113 2
#15 12 32
#16 6 9
#17 1 4
#18 36 42
#19 204 2
#20 7 14
#21 4 2
#22 8225 2200
#23 35 3
#24 2 2
#25 613 2
#26 33 2
#27 5 5

file = open("./SWEA/D4/정사각형방.txt", "r")

input = file.readline

from collections import deque

def bfs(q) : 
	global n

	result = 0
	
	while q : 
		i, j, dept = q.popleft()

		curr = matrix[i][j]
		result = dept

		for dx, dy in d : 
			di = i + dx
			dj = j + dy
			if 0 <= di < n and 0 <= dj < n and matrix[di][dj] == curr + 1 : 
				if dp[di][dj] == -1 : 
					q.append((di, dj, dept + 1))
				else : 
					result = dp[di][dj] + 1
					

	return result

t = int(input())

for tc in range(1, t + 1) : 
	n = int(input())
	matrix = [list(map(int, input().split())) for _ in range(n)]
	dp = [[-1 for _ in range(n)] for _ in range(n)]

	d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

	max_value, max_long = float('inf'), 1

	for i in range(n) : 
		for j in range(n) :
			if dp[i][j] == -1 : 
				dp[i][j] = bfs(deque([(i, j, 1)]))
			if max_long < dp[i][j] : 
				max_long = dp[i][j]
				max_value = matrix[i][j]
			elif max_long == dp[i][j] : 
				max_value = min(max_value, matrix[i][j])

	print("#%d %d %d" % (tc, max_value, max_long))

file.close()