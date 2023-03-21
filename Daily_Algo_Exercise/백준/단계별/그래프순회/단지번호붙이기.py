from collections import deque

def bfs(queue, visited) : 
	count = 1
	while queue : 
		i, j = queue.popleft()
		print("i, j : ", i, j)

		# 종료조건 필요없음

		# 재귀
		# 현재 노드에서 인접한 애들로 채움
		for d in dx : 
			di, dj = d
			if 0 <= i+di < n and 0 <= j+dj < n and matrix[i+di][j+dj] != "0" and not visited[i+di][j+dj] :
				visited[i+di][j+dj] = True
				count += 1
				queue.append((i+di, j+dj))
	return count

file = open("./bfs/단지번호붙이기tc.txt","r")

for _ in range(1) : 
	n = int(file.readline())
	matrix = [list(file.readline().strip("\n")) for _ in range(n)]
	answer = []
	for _ in range(int(file.readline())) :
		answer.append(int(file.readline()))

	print(n, "/",len(answer), answer)
	for mat in matrix : 
		print(mat)

	visited = [[False for _ in range(n)] for _ in range(n)]
	partition = []
	# 상하좌우
	dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	for i in range(n) : 
		for j in range(n) : 
			if matrix[i][j] != "0" and not visited[i][j] :
				visited[i][j] = True
				partition.append(bfs(deque([(i, j)]), visited))
				print(partition)

	print(len(partition))
	partition.sort()
	for p in partition: 
		print(p)
	
	
file.close()

# 백준 제출용
import sys
from collections import deque

def bfs(queue, visited) : 
	count = 1
	while queue : 
		i, j = queue.popleft()

		# 종료조건 필요없음

		# 재귀
		# 현재 노드에서 인접한 애들로 채움
		for d in dx : 
			di, dj = d
			if 0 <= i+di < n and 0 <= j+dj < n and matrix[i+di][j+dj] != "0" and not visited[i+di][j+dj] :
				visited[i+di][j+dj] = True
				count += 1
				queue.append((i+di, j+dj))
	return count

n = int(sys.stdin.readline())
matrix = [list(sys.stdin.readline().strip("\n")) for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]
partition = []
# 상하좌우
dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(n) : 
	for j in range(n) : 
		if matrix[i][j] != "0" and not visited[i][j] :
			visited[i][j] = True
			partition.append(bfs(deque([(i, j)]), visited))

print(len(partition))
partition.sort()
for p in partition: 
	print(p)