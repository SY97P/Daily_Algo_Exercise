file = open("./SWEA/D2/달팽이숫자.txt", "r")

input = file.readline

from itertools import cycle

def make_snail(i, j, value, da) :
	global n

	snail[i][j] = value

	# print(i, j)

	for _ in range(2) :
		dx = da[0] + i
		dy = da[1] + j
		if 0 <= dx < n and 0 <= dy < n and not visited[dx][dy] : 
			visited[dx][dy] = True
			make_snail(dx, dy, value + 1, da)
			break
		else :
			da = next(d)

t = int(input())
for tc in range(1 , t + 1) :
	n = int(input())
	print("#%d" % tc)
	visited = [[False for _ in range(n)] for _ in range(n)]
	visited[0][0] = True
	snail = [[1 for _ in range(n)] for _ in range(n)]
	d = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
	make_snail(0, 0, 1, next(d))

	for i in range(n) :
		for j in range(n) :
			print(snail[i][j], end = " ")
		print()

file.close()