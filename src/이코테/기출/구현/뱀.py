file = open("./Daily_Algo_Exercise/이코테/기출/구현/뱀.txt")

input = file.readline

from collections import deque


n = int(input())
matrix = [[0] * n for _ in range(n)]

k = int(input())
for _ in range(k):
	a, b = map(int, input().split())
	matrix[a-1][b-1] = 1

l = int(input())
event = [input().split() for _ in range(l)]

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir = 0
idx = 0

q = deque([(0, 0)])

timer = 0
while True:
	i, j = q[0]
	# 가고
	di, dj = i + d[dir][0], j + d[dir][1]
	
	# 벽인지 확인
	if di < 0 or di >= n or dj < 0 or dj >= n:
		timer += 1
		break

	# 내 몸통인지 확인
	if (di, dj) in q:
		timer += 1
		break

	# 사과 아니면 꼬리 자르고
	# 사과면 꼬리 자르지 말고
	if matrix[di][dj] != 1:
		q.pop()
	matrix[di][dj] = 0
	q.appendleft((di, dj))

	timer += 1

	# 방향바꾸고
	if idx < l and int(event[idx][0]) == timer:
		if event[idx][1] == "D":
			dir = dir + 1 if dir < 3 else 0
		else:
			dir = dir - 1 if dir > 0 else 3
		idx += 1

print(timer)

file.close()