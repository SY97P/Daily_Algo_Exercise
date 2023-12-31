#1 471
#2 446
#3 469
#4 481
#5 481
#6 501
#7 488
#8 476
#9 464
#10 490

file = open("./SWEA/D3/magnetic.txt", "r")

input = file.readline

from collections import deque

def bfs(j, col) : 
	count = 0
	
	q = deque([])

	for i, c in enumerate(col) : 
		# 1은 n 자성 -> 아래 방향 이동
		# 2는 s 자성 -> 위쪽 방향 이동
		if c == 1 or c == 2: 
			q.append((i, c))

	while q : 
		i, mag = q.popleft()

		# 아래 방향 이동
		if mag == 1 : 
			# out of index가 되면 무사히 테이블 밖으로 나간거
			if i + 1 >= n :
				matrix[i][j] = 0
				continue
			# 0이면 그냥 이동
			if matrix[i + 1][j] == 0 : 
				matrix[i+1][j] = mag
				matrix[i][j] = 0
				q.append((i+1, mag))
			# 0이 아니면 교착상태
			elif matrix[i + 1][j] == 2 : 
				count += 1
		elif mag == 2 : 
			if i - 1 < 0 :
				matrix[i][j] = 0
				continue
			if matrix[i-1][j] == 0 :
				matrix[i-1][j] = mag
				matrix[i][j] = 0
				q.append((i-1, mag))
			elif matrix[i-1][j] == 1 : 
				count += 1

	# for k in range(100) : 
	# 	print(matrix[k][j], end = " ")
	# print()
	
	return count // 2

for tc in range(1, 11) : 
	n = int(input())
	matrix = [list(map(int, input().split())) for _ in range(100)]

	# if tc != 1 : 
	# 	continue

	# 교착상태
	count = 0

	# 각 열마다 연산해야 함. 
	for j in range(100) : 
		col = [matrix[i][j] for i in range(100)]
		count += bfs(j, col)

	print("#%d %d" %(tc, count))

file.close()