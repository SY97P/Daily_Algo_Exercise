from collections import deque

file = open("./bfs/적록색약tc.txt", "r")

def bfs(queue) :
	while queue : 
		i, j = queue.popleft()

		for d in dx : 
			di = i + d[0]
			dj = j + d[1]
			if 0 <= di < n and 0 <= dj < n and not visited[di][dj] and matrix[i][j] == matrix[di][dj] :
				visited[di][dj] = True
				queue.append((di, dj))
				

n = int(file.readline())
matrix = [list(file.readline().strip("\n")) for _ in range(n)]
answer = list(map(int, file.readline().split()))

print("n , answer : ", n, answer)
for mat in matrix :
	print(mat)

dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for k in range(2) : 
	count = 0
	visited = [[False for _ in range(n)] for _ in range(n)]
	
	if k > 0 :
		for i in range(n) : 
			for j in range(n) : 
				if matrix[i][j] == "G" :
					matrix[i][j] = "R"
	for i in range(n) : 
		for j in range(n) : 
			if not visited[i][j] :
				visited[i][j] = True
				count += 1
				bfs(deque([(i, j)]))
	print(count, end = " ")
print()

file.close()

# 백준 제출용
from collections import deque
import sys

def bfs(queue) :
	while queue : 
		i, j = queue.popleft()

		for d in dx : 
			di = i + d[0]
			dj = j + d[1]
			if 0 <= di < n and 0 <= dj < n and not visited[di][dj] and matrix[i][j] == matrix[di][dj] :
				visited[di][dj] = True
				queue.append((di, dj))
				

n = int(sys.stdin.readline())
matrix = [list(sys.stdin.readline().strip("\n")) for _ in range(n)]

dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for k in range(2) : 
	count = 0
	visited = [[False for _ in range(n)] for _ in range(n)]
	
	if k > 0 :
		for i in range(n) : 
			for j in range(n) : 
				if matrix[i][j] == "G" :
					matrix[i][j] = "R"
	for i in range(n) : 
		for j in range(n) : 
			if not visited[i][j] :
				visited[i][j] = True
				count += 1
				bfs(deque([(i, j)]))
	print(count, end = " ")