file = open("./Daily_Algo_Exercise/이코테/기출/구현/뱀.txt")

input = file.readline

from collections import deque

n = int(input())
matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
matrix[1][1] = -1

k = int(input())
for _ in range(k):
	x, y = map(int, input().split())
	matrix[x][y] = 1

l = int(input())
command = deque([])
for _ in range(l):
	t, c = input().strip().split()
	command.append((int(t), c))

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def simulation():
	time = 0
	q = deque([(1, 1)])
	dir = 1
	hi, hj = 1, 1
	while True:
		if command and time == command[0][0]:
			_, c = command.popleft()
			if c == "D":
				dir += 1
				if dir > 3: dir = 0
			else:
				dir -= 1
				if dir < 0: dir = 3
		hi += d[dir][0]
		hj += d[dir][1]

		# 타당한 위치인지 확인
		if hi <= 0 or hi > n or hj <= 0 or hj > n or matrix[hi][hj] == -1:
			time += 1
			break

		# 이제 사과위치인지에 따라 꼬리를 옮길지 아닐지
		if matrix[hi][hj] != 1:
			ti, tj = q.pop()
			matrix[ti][tj] = 0
		matrix[hi][hj] = -1
		q.appendleft((hi, hj))
		
		time += 1

	return time


answer = simulation()
print(answer)


file.close()