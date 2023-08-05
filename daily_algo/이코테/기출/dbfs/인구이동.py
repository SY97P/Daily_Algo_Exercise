file = open("./Daily_Algo_Exercise/이코테/기출/dbfs/인구이동.txt")

input = file.readline 


n, l, r = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(i, j, union_num):
	for dx, dy in d:
		di = i + dx
		dj = j + dy
		if 0 <= di < n and 0 <= dj < n and union[di][dj] == -1 and l <= abs(matrix[di][dj] - matrix[i][j]) <= r:
			unity[union_num].append((di, dj))
			union[di][dj] = union_num
			dfs(di, dj, union_num)


answer = 0
while True:
	# dfs 하면서 연합 정보 생성
	unity = []
	union = [[-1] * n for _ in range(n)]
	union_num = 0
	for i in range(n):
		for j in range(n):
			if union[i][j] == -1:
				unity.append([(i, j)])
				union[i][j] = union_num
				dfs(i, j, union_num)
				union_num += 1

	# 인구이동 불가? -> break 
	if union_num == n**2:
		break

	# 인구이동 연산
	for uni in unity:
		total = 0
		for i, j in uni:
			total += matrix[i][j]
		for i, j in uni:
			matrix[i][j] = total // len(uni)
			
	answer += 1

print(answer)


file.close()