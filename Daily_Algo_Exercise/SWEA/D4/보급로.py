#1 2
#2 2
#3 8
#4 57
#5 151
#6 257
#7 18
#8 160
#9 414
#10 395

file = open("./SWEA/D4/보급로.txt", "r")

input = file.readline

from collections import deque

t = int(input())

def bfs(n) : 
	q = deque([(0, 0, 0, 0)])

	min_cost = float("inf")

	while q : 
		cost, i, j, dir = q.popleft()

		# print(cost, i, j, dir)

		if i == n - 1 and j == n - 1 and cost < min_cost : 
			min_cost = cost
			continue

		temp = []
		for idx, (dx, dy) in enumerate(d) : 
			dx += i
			dy += j
			if 0 <= dx < n and 0 <= dy < n and (dir + 2)%4 != idx : 
				new_cost = cost + matrix[dx][dy]
				# if i == 0 and j == 0 :
				# 	print(idx)
				# 	continue
				if dp[dx][dy] > new_cost and new_cost < min_cost : 
					# temp.append((new_cost, dx, dy, idx))
					dp[dx][dy] = new_cost
					q.append((new_cost, dx, dy, idx))

		# temp.sort()
		# print(temp)
		# for t in temp : 
		# 	dp[t[1]][t[2]] = t[0]
		# 	q.append(t)

	return min_cost

for tc in range(1, t + 1) : 
	n = int(input())
	matrix = [list(map(int, input().strip())) for _ in range(n)]
	dp = [[float("inf") for _ in range(n)] for _ in range(n)]
	dp[0][0] = 0
	
	# r, b, l, t
	d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

	# if tc != 2 : 
	# 	continue

	print("#%d %d" %(tc, bfs(n)))

	# for dpp in dp : 
	# 	print(dpp)

file.close()