file = open("./Daily_Algo_Exercise/이코테/기출/최단경로/정확한순위.txt")

input = file.readline

n, m = map(int, input().split())
matrix = [[1e9] * (n+1) for _ in range(n+1)]

for _ in range(m):
	a, b = map(int, input().split())
	matrix[a][b] = 1

for i in range(1, n+1):
	matrix[i][i] = 0

for k in range(1, n + 1):
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

answer = 0
for i in range(1, n +1):
	count = 0
	for j in range(1, n + 1):
		if matrix[i][j] != 1e9 or matrix[j][i] != 1e9:
			count += 1
	if count == n:
		answer += 1
print(answer)

# # i번 학생이 진 애들 모음
# winner_list = [set() for _ in range(n+1)]
# # i번 학생이 이긴 애들 모음
# loser_list = [set() for _ in range(n+1)]
# for _ in range(m):
# 	a, b = map(int, input().split())
# 	winner_list[a].add(b)
# 	loser_list[b].add(a)

# for i in range(1, n + 1):
# 	# i번 학생이 진 애들은
# 	for winner in winner_list[i]:
# 		# i번 학생을 이긴 애들한테도 진 거임
# 		for loser in loser_list[i]:
# 			loser_list[winner].add(loser)
# 	for lose in loser_list[i]:
# 		for winner in winner_list[i]:
# 			winner_list[loser].add(winner)

# answer = 0
# for i in range(1, n + 1):
# 	if len(winner_list[i]) + len(loser_list[i]) == n-1:
# 		answer += 1

# print(answer)


file.close()