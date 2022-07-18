# 해결방안 1번 :
# DFS
file = open("./dfs/알파벳tc.txt", "r")

def dfs(i, j, path) :
	global result
	print(i, j, path)
	for d in dx : 
		di = i + d[0]
		dj = j + d[1]
		if 0 <= di < r and 0 <= dj < c and matrix[di][dj] not in path :
			path += matrix[di][dj]
			dfs(di, dj, path)
			path = path[:len(path)-1]
	result = max(result, len(path))

for _ in range(3) : 
	r, c = map(int, file.readline().split())
	matrix = [list(file.readline().strip("\n")) for _ in range(r)]
	answer = int(file.readline())
	file.readline()

	print(r,c , answer)
	for mat in matrix :
		print(mat)

	result = 0
	dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	dfs(0, 0, [matrix[0][0]])
	print(result)

	print()

file.close()