file = open("./Daily_Algo_Exercise/SWEA/D3/오목판정.txt")

input = file.readline

dlist = [(0, 1), (1, 0), (1, 1), (1, -1)]
t = int(input())
for tc in range(1, t+1):
	n = int(input())
	matrix = [input().strip() for _ in range(n)]

	def check(matrix):
		for i in range(n):
			for j in range(n):
				if matrix[i][j] == "o":
					for dx, dy in dlist:
						di, dj = i, j
						cnt = 0
						while 0 <= di < n and 0 <= dj < n and matrix[di][dj] == "o":
							cnt += 1
							di += dx
							dj += dy
						if cnt >= 5:
							pi, pj = i-dx, j-dy
							if 0 <= pi < n and 0 <= pj < n and matrix[pi][pj] == "o":
								continue
							else:
								return "YES"
		return "NO"

	print(f'#{tc} {check(matrix)}')

file.close()