file = open("./dfs/미로탐색tc.txt", "r")

def dfs(i, j) :
	# 첫 시작과 마지막 목적지 모두 카운트함
	global count
	count += 1

	print("i, j, count : ", i, j, count)

	# 종료조건
	if i == n and j == m :
		return

	# 재귀
	# 상우하좌 순서로 탐색을 함
	# out of index 검사와 유효한 index인지 검사 필요
	if (i-1 >= 0) and matrix[i-1][j] != 0 :
		dfs(i-1, j)
	elif (j+1 < m) and matrix[i][j+1] != 0 :
		dfs(i, j+1)
	elif (i+1 < n) and matrix[i+1][j] != 0 :
		dfs(i+1, j)
	elif (j-1 >= 0) and matrix[i][j-1] != 0 :
		dfs(i, j-1)
	else :
		return
	

for tc in range(4) : 
	print(tc + 1, "번째 테스트 케이스")
	n, m = map(int, file.readline().split())
	matrix = [list(map(int, file.readline().strip("\n"))) for _ in range(n)]
	answer = int(file.readline())
	file.readline()

	print(n,m, answer)
	for mat in matrix : 
		print(mat)

	count = 0 
	dfs(0, 0)
	print(count)
	
	print()

file.close()