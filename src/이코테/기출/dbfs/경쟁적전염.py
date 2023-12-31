file = open("./Daily_Algo_Exercise/이코테/기출/dbfs/경쟁적전염.txt")

input = file.readline 


from collections import deque


n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

virus = []
for i in range(n):
	for j in range(n):
		if matrix[i][j] != 0:
			virus.append((matrix[i][j], i, j))
virus.sort()

q = deque()
for v, i, j in virus:
	q.append((0, i, j))

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while q: 
	c, i, j = q.popleft()

	if c >= s:
		break

	for dx, dy in d:
		di = i + dx
		dj = j + dy 
		if 0 <= di < n and 0 <= dj < n and matrix[di][dj] == 0:
			matrix[di][dj] = matrix[i][j]
			q.append((c + 1, di, dj))

# for mat in matrix:
# 	print(mat)

print(matrix[x-1][y-1])


file.close()