file = open("./Daily_Algo_Exercise/이코테/기출/최단경로/플로이드.txt")

input = file.readline 

n = int(input())
m = int(input())
matrix = [[1e9 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
	a, b, c = map(int, input().split())
	matrix[a][b] = min(matrix[a][b], c)

for i in range(1, n + 1):
	for j in range(1, n + 1):
		if i == j:
			matrix[i][i] = 0

for k in range(1, n + 1):
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

for i in range(1, n + 1):
	for j in range(1, n + 1):
		if matrix[i][j] == 1e9:
			matrix[i][j] = 0
		print(matrix[i][j], end=" ")
	print()



file.close()