n, m = map(int, input().split())
x, y, dir = map(int, input().split())

visited = [[0 for i in range(m)] for _ in range(n)]
visited[x][y] = 1

matrix = [list(map(int, input().split())) for _ in range(n)]

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

result = 1

# for mat in matrix:
# 	print(mat)

def turn_left():
	global dir
	dir -= 1
	if dir < 0:
		dir = 3

turn_count = 0
while True:
	turn_left()
	di = x + d[dir][0]
	dj = y + d[dir][1]
	if matrix[di][dj] == 0 and not visited[di][dj]:
		visited[di][dj] = 1
		x, y = di, dj
		result += 1
		turn_count = 0
		continue
	else:
		turn_count += 1
	if turn_count == 4:
		di = x - d[dir][0]
		dj = y - d[dir][1]
		if matrix[di][dj] == 0:
			x, y = di, dj
		else:
			break
		turn_count = 0

print(result)
			