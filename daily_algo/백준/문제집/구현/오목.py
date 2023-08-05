# 1
# 3 2

file = open("./Daily_Algo_Exercise/백준/문제집/구현/오목.txt")

input = file.readline

matrix = [list(map(int, input().split())) for _ in range(19)]

end_game = False
result_i, result_j = -1, -1

d = [(0, 1), (1, 0), (1, 1), (-1, 1)]

for i in range(19):
	for j in range(19):
		if matrix[i][j] != 0:
			curr = matrix[i][j]
	
			for dx, dy in d:
				count = 1
				di = i + dx
				dj = j + dy
	
				while 0 <= di < 19 and 0 <= dj < 19 and matrix[di][dj] == curr:
					count += 1
					di += dx
					dj += dy
	
				if count == 5: 
					ri, rj = i - dx, j - dy
					if 0 <= ri < 19 and 0 <= rj < 19 and matrix[ri][rj] == curr:
						continue
					end_game = True
					result_i, result_j = i, j
					break
	if end_game:
		break
			

if not end_game:
	print(0)
else:
	print(matrix[result_i][result_j])
	print(result_i+1, result_j+1)
				

file.close()