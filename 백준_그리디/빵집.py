def checkUpRight(m, v, rows, cols, r, c) : 
	# out of index가 나지 않고
	# 방문한 적이 없어야 하고
	# X가 아니어야 함
	# 방향은 r-1, c+1
	if (r-1) >= 0 and (c+1) < cols :
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
	for _ in range(2, 3) :
		rows, cols = map(int, input().split())
		matrix = [list(input().strip("\n")) for _ in range(rows)]
		
		count = 0
		visited = [[0 for _ in range(cols)] for _ in range(rows)]
		for row in range(rows) :
			if visited[row][0] != 0 :
				continue
			else : 
				path = [(row, 0)]
				r, c= row, 0
				isComp = True
				while c < cols - 1 : 
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
						visited[p[0]][p[1]] = 1
					count += 1
		
		print(count)

def main() :
	file = open("./백준_그리디/빵집tc.txt")
	print("solution : ", solution(file))
	file.close()

main()

