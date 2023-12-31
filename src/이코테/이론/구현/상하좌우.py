n = int(input())
command = input().strip().split()

d = [(0, -1), (0, 1), (-1, 0), (1, 0)]
move_type = ['L', 'R', 'U', 'D']

result = 0

x, y = 1, 1

for comm in command:
	# di, dj = 0, 0
	for i, move in enumerate(move_type):
		if move == comm:
			di = x + d[i][0]
			dj = y + d[i][1]
	if 0 < di < n and 0 < dj < n:
		x, y = di, dj

print(x, y)