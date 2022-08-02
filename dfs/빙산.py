
file = open("./dfs/빙산tc.txt", "r")

def dfs(i, j) : 
	visited[i][j] = True
	for d in dx: 
		di = i + d[0]
		dj = j + d[1]
		if matrix[di][dj] != 0 and not visited[di][dj] :
			dfs(di, dj)

for tc in range(3) : 
	n, m = map(int, file.readline().split())
	matrix = [list(map(int, file.readline().split())) for _ in range(n)]
	answer = int(file.readline())
	file.readline()

	print(n, m, answer)

	year = 0 
	dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

	# 미리 빙산 좌표를 구해놓음
	icebug = []
	for i in range(n) : 
		for j in range(m) : 
			if matrix[i][j] != 0 :
				icebug.append((i, j))
	
	while True : 
		visited = [[False for _ in range(m)] for _ in range(n)]

		print("matrix")
		for mat in matrix : 
			print(mat)
			
		ice = 0
		remove = []
		next = []
		
		for i, j in icebug : 
			# 녹이기
			count = 0
			for d in dx : 
				di = i + d[0]
				dj = j + d[1]
				if matrix[di][dj] == 0 :
					count += 1
			# 이번 년도에 사라질 빙산 구하기
			if matrix[i][j] < count :
				remove.append((i, j))
			# 살아남은 애들 내년 값은 next에 저장
			else :
				next.append((i, j, matrix[i][j] - count))
				
			
			# 빙산 개수 구함
			if not visited[i][j] :
				if ice > 1: 
					break
				ice += 1
				visited[i][j] = True
				dfs(i, j)

		if ice < 1 : 
			print(0)
			break
		elif ice > 1 : 
			print(year)
			break

		# icebug 갱신
		for r in remove :
			icebug.remove(r)
			matrix[r[0]][r[1]] = 0
		# matrix 갱신
		for i, j, v in next : 
			matrix[i][j] = v
		# year 증가
		year += 1
		

file.close()

# 백준 제출용
import sys

sys.setrecursionlimit(10 ** 4)

def dfs(i, j) : 
	visited[i][j] = True
	for d in dx: 
		di = i + d[0]
		dj = j + d[1]
		if matrix[di][dj] != 0 and not visited[di][dj] :
			dfs(di, dj)

n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

year = 0 
dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 미리 빙산 좌표를 구해놓음
icebug = []
for i in range(n) : 
	for j in range(m) : 
		if matrix[i][j] != 0 :
			icebug.append((i, j))

while True : 

	if len(icebug) <= 1:
		print(0)
		break
	
	visited = [[False for _ in range(m)] for _ in range(n)]

	ice = 0
	remove = []
	next = []
	
	for i, j in icebug : 
		# 녹이기
		count = 0
		for d in dx : 
			di = i + d[0]
			dj = j + d[1]
			if matrix[di][dj] == 0 :
				count += 1
		# 이번 년도에 사라질 빙산 구하기
		if matrix[i][j] < count :
			remove.append((i, j))
		# 살아남은 애들 내년 값은 next에 저장
		else :
			next.append((i, j, matrix[i][j] - count))
			
		
		# 빙산 개수 구함
		if not visited[i][j] :
			if ice > 1: 
				break
			ice += 1
			visited[i][j] = True
			dfs(i, j)

	if ice < 1 : 
		print(0)
		break
	elif ice > 1 : 
		print(year)
		break

	# icebug 갱신
	for r in remove :
		icebug.remove(r)
		matrix[r[0]][r[1]] = 0
	# matrix 갱신
	for i, j, v in next : 
		matrix[i][j] = v
	# year 증가
	year += 1
	