def checkUpRight(m, v, rows, cols, r, c) : 
	# out of index가 나지 않고
	# 방문한 적이 없어야 하고
	# X가 아니어야 함
	# 방향은 r-1, c+1
	if (r-1) > 0 and (c+1) < cols :
		if v[r-1][c+1] == 0 :
			if m[r-1][c+1] != "x" :
				return True
			else :
				return False
		else :
			return False
	else : 
		return False

def checkJustRight(m, v, rows, cols, r, c) :
	# 방향은 r, c+1
	if (c+1) < cols :
		if v[r][c+1] == 0 :
			if m[r][c+1] != "x" :
				return True
			else : 
				return False
		else :
			return False
	else :
		return False

def checkDownRight(m, v, rows, cols, r, c) : 
	# 방향은 r+1, c+1
	if (r+1) < rows and (c+1) < cols :
		if v[r+1][c+1] == 0 :
			if m[r+1][c+1] != "x" :
				return True
			else :
				return False
		else : 
			return False
	else :
		return False
		

def move(i, j, dir) :
	if dir == "just_right" :
		return (i, j+1)
	elif dir == "up_right" :
		return (i-1, j+1)
	elif dir == "down_right" :
		return (i+1, j+1)

def solution(file) :
	for i in range(2) :
		# input 
		rows, cols = map(int, file.readline().split())
		matrix = [list(file.readline().strip("\n")) for _ in range(rows)]
		answer = int(file.readline())
		file.readline()

		print(rows, cols, answer)
		for m in matrix :
			print(m)

		# logic
		count = 0
		visited = [[0 for _ in range(cols)] for _ in range(rows)]
		for row in range(rows) :
			print("row : ", row)
			# 시작점이라도 방문을 했으면 다음으로 넘어감
			if visited[row][0] != 0 :
				print("방문한 시작점임")
				continue
			else : 
				path = [(row, 0)]
				r, c= row, 0
				isComp = True
				while c < cols : 
					print("r, c : ",r, c)
					# 위 & 오 확인
					if checkUpRight(matrix, visited, rows, cols, r, c) :
						r, c = move(r, c, "up_right")
						path.append((r, c))
					elif checkJustRight(matrix, visited, rows, cols, r, c) :
						r, c = move(r, c, "just_right")
						path.append((r, c))
					elif checkDownRight(matrix, visited, rows, cols, r, c) :
						r, c = move(r, c, "down_right")
						path.append((r, c))
					else : 
						# 여태까지 쌓아온 경로를 모두 날려버림
						isComp = False
						break
				if isComp :
					for p in path : 
						visited[p[0], p[1]] = 1
					count += 1
		print(count)
		print()
		

def main() :
	file = open("./백준_그리디/빵집tc.txt", "r")
	print("solution : ", solution(file))
	file.close()

main()

