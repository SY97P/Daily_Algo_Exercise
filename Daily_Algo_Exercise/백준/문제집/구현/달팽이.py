# 49 26 27 28 29 30 31
# 48 25 10 11 12 13 32
# 47 24 9 2 3 14 33
# 46 23 8 1 4 15 34
# 45 22 7 6 5 16 35
# 44 21 20 19 18 17 36
# 43 42 41 40 39 38 37
# 5 7

file = open("./Daily_Algo_Exercise/백준/문제집/구현/달팽이.txt")

input = file.readline

n = int(input())
target = int(input())

matrix = [[0 for _ in range(n)] for _ in range(n)]

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

flag = n*n
i, j = 0, 0
x, y = -1, -1
d = 0
while flag > 0:
	if flag == target:
		x, y = i, j
	matrix[i][j] = flag
	di, dj = i + dir[d][0], j + dir[d][1]
	if 0 <= di < n and 0 <= dj < n and matrix[di][dj] == 0:
		i, j = di, dj
	else:
		d = (d+1)%4
		i, j = i + dir[d][0], j + dir[d][1]
	flag -= 1

for mat in matrix:
	print(* mat)
print(x + 1, y + 1)
	

file.close()