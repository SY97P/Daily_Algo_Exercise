# 11 2 1 4 3 
# 6 12 7 8 10 
# 21 17 13 9 5 
# 16 18 19 14 20 
# 23 22 25 24 15 
# 3 2 5 4 15 
# 6 8 9 14 10 
# 1 7 13 19 25 
# 16 12 17 18 20 
# 11 22 21 24 23 
# 23 2 21 4 11 
# 6 18 17 12 10 
# 25 19 13 7 1 
# 16 14 9 8 20 
# 15 22 5 24 3 
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15 
# 16 17 18 19 20
# 21 22 23 24 25

file = open('./Daily_Algo_Exercise/백준/문제집/구현/배열돌리기.txt')

input = file.readline 

t = int(input())

for tc in range(t):
	n, d = map(int, input().split())
	matrix = [list(map(int, input().split())) for _ in range(n)]

	main, sub, vert, hori = [], [], [], []

	for i in range(n):
		for j in range(n):
			if i == j:
				main.append(matrix[i][j])
			if j == (n-1)//2:
				vert.append(matrix[i][j])
			if i == (n-1)//2:
				hori.append(matrix[i][j])
			if i + j == n-1:
				sub.append(matrix[i][j])

	
	is_clock = True if d > 0 else False
	for _ in range(abs(d) // 45):
		temp_main, temp_sub, temp_vert, temp_hori = main, sub, vert, hori
		if is_clock:
			vert = temp_main
			hori = list(reversed(temp_sub))
			sub = temp_vert
			main = temp_hori
		else:
			hori = temp_main
			vert = temp_sub
			main = temp_vert
			sub = list(reversed(temp_hori)) 

	# print(vert)
	# print(main)
	# print(hori)
	# print(sub)

	main_idx, sub_idx, vert_idx, hori_idx = 0, 0, 0, 0
	for i in range(n):
		for j in range(n):
			if i == j:
				matrix[i][j] = main[main_idx]
				main_idx += 1
			if j == (n-1) // 2:
				matrix[i][j] = vert[vert_idx]
				vert_idx += 1
			if i == (n-1) // 2:
				matrix[i][j] = hori[hori_idx]
				hori_idx += 1
			if i + j == n - 1:
				matrix[i][j] = sub[sub_idx]
				sub_idx += 1

	for mat in matrix:
		print(* mat)

		

file.close()