file = open("./dfs/바이러스tc.txt", "r")

def dfs(node, visited) : 
	# 종료조건 없어도 될 것 같음

	# 재귀
	# 연결되어 있으면서 방문하지 않은 곳으로 이동
	for ed in edges[node] : 
		if not visited[ed] :
			visited[ed] = True
			dfs(ed, visited)

for _ in range(1) : 
	v = int(file.readline())
	e = int(file.readline())
	edges = [[] for _ in range(v+1)]
	for _ in range(e) : 
		x, y = map(int, file.readline().split())
		edges[x].append(y)
		edges[y].append(x)
	answer = int(file.readline())
	file.readline()

	print("v, e, answer : ", v, e, answer)
	for edg in edges : print(edg)
	print()

	visited = [False for _ in range(v+1)]
	visited[0] = visited[1] = True

	dfs(1, visited)

	print(visited)

	print(visited.count(True) - 2)
	

file.close()

# 백준 제출용
# import sys

# def dfs(node, visited) : 
# 	# 종료조건 필요 없어

# 	# 재귀
# 	for ed in edges[node] : 
# 		if not visited[ed] :
# 			visited[ed] = True
# 			dfs(ed, visited)

# v = int(sys.stdin.readline())
# e = int(sys.stdin.readline())
# edges = [[] for _ in range(v+1)]
# for _ in range(e) : 
# 	x, y = map(int, sys.stdin.readline().split())
# 	edges[x].append(y)
# 	edges[y].append(x)
# visited = [False for _ in range(v+1)]
# visited[0] = visited[1] = True

# dfs(1, visited)

# print(visited.count(True) - 2)