loc = input().strip()

row = int(loc[1])
col = ord(loc[0]) - ord('a') + 1

steps = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]

result = 0

for dx, dy in steps:
	di = dx + row
	dj = dy + col
	if 0 < di <= 8 and 0 < dj <= 8:
		result += 1

print(result)