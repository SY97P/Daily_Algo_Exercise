#1 1990
#2 1574
#3 1252
#4 1080
#5 7645
#6 6378
#7 5073
#8 4093
#9 17111
#10 14683
#11 11693
#12 9135
#13 30616
#14 26184
#15 20124
#16 15225
#17 48378
#18 39769
#19 31522
#20 24196

file = open("./SWEA/D4/파핑파핑지뢰찾기.txt", "r")
# wfile = open("./SWEA/D4/파핑파핑지뢰찾기res.txt", "w")

input = file.readline

from collections import deque

t = int(input())

def setValue(i, j) : 
	global n
	
	count = 0
	for dx, dy in d : 
		di = i + dx
		dj = j + dy
		if 0 <= di < n and 0 <= dj < n and matrix[di][dj] == "*" : 
			count += 1
	matrix[i][j] = str(count)
	return matrix[i][j]

def bfs(q) : 
	global n
	
	while q : 
		i, j = q.popleft()

		# print(i, j)

		# 현재 위치를 기준으로 주변 3 ~ 8칸의 값을 구함.
		# 0이 될 좌표는 큐에 넣고 아닌 곳은 값만 갱신해줌.
		for dx, dy in d : 
			di = i + dx 
			dj = j + dy
			if 0 <= di < n and 0 <= dj < n and matrix[di][dj] != "0" :
				if setValue(di, dj) == "0" : 
					q.append((di, dj))
				

for tc in range(1, t + 1) : 
	n = int(input())
	matrix = [list(input().strip()) for _ in range(n)]

	# c = 10
	
	# if tc != 1:
	# 	continue

	d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

	count = 0

	# 먼저 0인 친구들을 먼저 BFS로 넣어서 우선순위 처리해줌. 
	for i in range(n) :
		for j in range(n) :
			if matrix[i][j] != "*" : 
				isClear = True
				for dx, dy in d : 
					di = dx + i
					dj = dy + j
					if 0 <= di < n and 0 <= dj < n and matrix[di][dj] == "*" :
						isClear = False
						break
				# 주변에 지뢰가 없고, 이미 와본 곳이 아니라면
				# count를 증가시키고 BFS에 넣어서 주변을 정리해야 함.
				if isClear and matrix[i][j] != "0" : 
					count += 1
					matrix[i][j] = "0"
					# print(i, j)
					bfs(deque([(i, j)]))

	# for mat in matrix : 
	# 	print(mat)
	# 	wfile.write(''.join(mat))
	# 	wfile.write('\n')

	# 이제 남은 "." 인 개수를 count에 더해주면 됨. 
	for i in range(n) :
		for j in range(n) : 
			if matrix[i][j] == "." : 
				count += 1

	print("#%d %d" %(tc, count))

file.close()
# wfile.close()