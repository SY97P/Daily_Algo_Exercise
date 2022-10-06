#1 23

file = open("./SWEA/D4/격자판의숫자이어붙이기.txt", "r")

input = file.readline

t = int(input())

def dfs(i, j, q) :
	if len(q) == 7 : 
		candi.add(''.join(map(str, q)))
		return

	for dx, dy in d : 
		dx += i
		dy += j
		if 0 <= dx < 4 and 0 <= dy < 4 :
			dfs(dx, dy, q + [matrix[dx][dy]])

for tc in range(1, t + 1) : 
	matrix = [list(map(int, input().split())) for _ in range(4)]

	d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

	candi = set()

	temp = [1, 2, 3, 4, 5]

	for i in range(4) : 
		for j in range(4) : 
			dfs(i, j, [matrix[i][j]])

	print("#%d %d" %(tc, len(candi)))
	# print(candi)

file.close()