n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]


def check(q):
	for x, y, a in q:
		# 기둥
		if a == 0:
			if y == 0 or [x-1, y, 1] in q or [x, y, 1] in q or [x, y-1, 0] in q:
				continue
			else:
				return False
		elif a == 1:
			if [x, y-1, 0] in q or [x+1, y-1, 0] in q or ([x-1, y, 1] in q and [x+1, y, 1] in q):
				continue
			else:
				return False
	return True

q = []

for build in build_frame:
	x, y, a, b = build

	# data = [x, y, a]
	# 삭제
	if b == 0:
		q.remove([x, y, a])
		if not check(q):
			q.append([x, y, a])
	elif b == 1:
		q.append([x, y, a])
		if not check(q):
			q.remove([x, y, a])

q = list(q)
q.sort()
print(q)
		