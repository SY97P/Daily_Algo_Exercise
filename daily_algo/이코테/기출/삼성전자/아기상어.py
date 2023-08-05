file = open("./Daily_Algo_Exercise/이코테/기출/삼성전자/아기상어.txt")

input = file.readline


from collections import deque 

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

answer = 0

si, sj = -1, -1
scale = 2
feed_count = 0

for i in range(n):
	for j in range(n):
		if matrix[i][j] == 9:
			si, sj = i, j
			break
matrix[si][sj] = 0

d = [(-1, 0), (0, -1), (0, 1), (1, 0)]

# def remain():
# 	for i in range(n):
# 		for j in range(n):
# 			if matrix[i][j] != 0 and scale > matrix[i][j]:
# 				return True
# 	return False

def bfs(x, y):
	visited = [[False] * n for _ in range(n)]
	visited[x][y] = True

	q = deque([(0, x, y)])

	result = [1e9, 1e9, 1e9]

	while q: 
		c, i, j = q.popleft()

		if matrix[i][j] != 0 and scale > matrix[i][j]:
			if c == result[0]:
				if i == result[1]:
					if j < result[2]:
						result = [c, i, j]
				elif i < result[1]:
					result = [c, i, j]
			elif c < result[0]:
				result = [c, i, j]

		for dx, dy in d:
			di = i + dx
			dj = j + dy 
			if 0 <= di < n and 0 <= dj < n and not visited[di][dj] and scale >= matrix[di][dj]:
				visited[di][dj] = True
				q.append((c+1, di, dj))

	# 예외처리?
	return result


while True:
	# print(answer, si, sj)
	# if not remain():
	# 	break
	time, si, sj = bfs(si, sj)
	if time == 1e9:
		break
	answer += time
	matrix[si][sj] = 0
	feed_count += 1
	if feed_count >= scale:
		feed_count = 0
		scale += 1


print(answer)


file.close()


# # 스포방지
# * bfs 과정에서 방향우선순위를 주는 방식은 오답처리됨 (4%)
# * 리스트에 있는 모든 먹이를 탐색한 다음 가장 위, 왼쪽에 있는 먹이를 선택해야 함. 