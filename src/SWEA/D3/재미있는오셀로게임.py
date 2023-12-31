file = open("./SWEA/D3/재미있는오셀로게임.txt", "r")

input = file.readline

t = int(input())

def effect(i, j, c, dir, rev) :
	global count_b, count_w
	
	di, dj = i, j
	if dir == 0 : 
		di -= 1
	elif dir == 1 : 
		di -= 1
		dj += 1
	elif dir == 2 : 
		dj += 1
	elif dir == 3 :
		di +=1 
		dj += 1
	elif dir == 4 : 
		di += 1
	elif dir == 5 : 
		di += 1
		dj -= 1
	elif dir == 6 : 
		dj -= 1
	elif dir == 7 : 
		di -= 1
		dj -= 1

	if 0 <= di < n and 0 <= dj < n and matrix[di][dj] != 0 : 
		if not rev : # 아직 전환된 돌이 없는 상태
			# 다른 색깔 돌이면 rev = True
			if matrix[di][dj] != c : 
				rev = True
			# 같은 색깔 돌이면 ㅌㅌ
			else : 
				return False
		else : # 돌 색깔이 전환된 상태
			# 다른 색깔 돌이면 그냥 DFS 진행 -> 결과가 True일 때만 색깔 c로 변경
			
			# 같은 색깔 돌이면 true 반환
			if matrix[di][dj] == c : 
				return True
		temp = effect(di, dj, c, dir, rev)
		if temp : # 참말이면 바꿔줌
			matrix[di][dj] = c
			if c == 1 : # 흑돌로 바꾸면 -> 흑 증가, 백 감소
				count_b += 1
				count_w -= 1
			else : 
				count_b -= 1
				count_w += 1
			# if count_b < 0 or count_w < 0 : 
			# 	print("abnormal error")
		return temp
			
	else : 
		return False

for tc in range(1, t + 1) : 
	n, m = map(int, input().split())

	matrix = [[0 for _ in range(n)] for _ in range(n)]
	matrix[n//2][n//2] = matrix[n//2-1][n//2-1] = 2
	matrix[n//2-1][n//2] = matrix[n//2][n//2-1] = 1

	count_b = count_w = 2

	for _ in range(m) : 
		j, i, c = map(int, input().split())
		j -= 1
		i -= 1

		dir_val = []
		for dir in range(8) : 
			dir_val.append(effect(i, j, c, dir, False))

		if True in dir_val : 		
			matrix[i][j] = c
			if c == 1: 
				count_b += 1
			else : 
				count_w += 1
			# print("matrix : ", i, j, "흑" if c == 1 else "백")
			# for mat in matrix : 
			# 	print(mat)
			# print("흑 / 백 : ", count_b, " / ", count_w)
		# else : 
			# print("흑" if c == 1 else "백", " 건너뜀")

	print("#%d %d %d" % (tc, count_b, count_w))

file.close()