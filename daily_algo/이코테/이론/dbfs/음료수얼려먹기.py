def dfs(i, j):
	if i < 0 or i >= n or j < 0 or j >= m:
		return False
	if matrix[i][j] == 0:
		matrix[i][j] = 1
		dfs(i-1, j)
		dfs(i+1, j)
		dfs(i, j-1)
		dfs(i, j+1)
		return True
	return False
	

n, m = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]

result = 0

for i in range(n):
	for j in range(m):
		if dfs(i, j):
			result += 1

print(result)