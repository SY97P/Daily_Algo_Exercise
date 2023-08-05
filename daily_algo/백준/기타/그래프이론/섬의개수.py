
file = open("./dfs/섬의개수tc.txt", "r")

def dfs(i, j) : 
	visited[i][j] = True

	for d in dx : 
		di = i + d[0]
		dj = j + d[1]
		if 0 <= di < h and 0 <= dj < w and matrix[di][dj] != 0 and not visited[di][dj] :
			dfs(di, dj)

line = map(int, file.readline().split())
tc_number = 0
count_list = []
while line != (0,0) :
	tc_number += 1
	print(tc_number, "번째 테스트 케이스")
	w, h = line
	matrix = [list(map(int, file.readline().split())) for _ in range(h)]

	print(w, h)
	for mat in matrix : 
		print(mat)

	# logic
	count = 0
	dx = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
	visited = [[False for _ in range(w)] for _ in range(h)]
	for i in range(h) : 
		for j in range(w) : 
			if not visited[i][j] and matrix[i][j] != 0 : 
				count += 1
				dfs(i, j)
	count_list.append(count)

	print()
	line = tuple(map(int, file.readline().split()))

file.readline()

for tc in range(tc_number) : 
	print(tc + 1, "번째 테스트 케이스 정답 : ", int(file.readline()))
	print(tc + 1, "번째 연산 결과.         : ", count_list[tc])
file.close()

# 백준 제출용
import sys

def dfs(i, j) : 
	visited[i][j] = True

	for d in dx : 
		di = i + d[0]
		dj = j + d[1]
		if 0 <= di < h and 0 <= dj < w and matrix[di][dj] != 0 and not visited[di][dj] :
			dfs(di, dj)

line = tuple(map(int, sys.stdin.readline().split()))
count_list = []
while line != (0, 0) :
	w, h = line
	matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

	count = 0
	dx = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
	visited = [[False for _ in range(w)] for _ in range(h)]
	for i in range(h) : 
		for j in range(w) : 
			if not visited[i][j] and matrix[i][j] != 0 : 
				count += 1
				dfs(i, j)
	count_list.append(count)

	line = tuple(map(int, sys.stdin.readline().split()))
	
for c in count_list : 
	print(c)