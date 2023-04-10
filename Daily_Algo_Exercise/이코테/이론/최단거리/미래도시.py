n, m = map(int, input().split())

matrix = [[1e9] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
	for j in range(1, n+1):
		if i == j:
			matrix[i][j] = 0

for _ in range(m):
	a, b = map(int, input().split())
	matrix[a][b] = 1
	matrix[b][a] = 1

for k in range(1, n+1):
	for i in range(1, n+1):
		for j in range(1, n+1):
			matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

x, k = map(int, input().split())

result = matrix[1][k] + matrix[k][x]
if result >= 1e9:
	print(-1)
else:
	print(result)