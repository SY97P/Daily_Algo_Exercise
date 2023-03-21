

file = open("./dfs/연결요소의개수tc.txt", "r")

def dfs(node) : 
	print("node : ",node, count)
	visited[node] = True

	for e in edges[node] : 
		if not visited[e] :
			dfs(e)

for _ in range(5) : 
	n, v = map(int, file.readline().split())
	edges = [[] for _ in range(n+1)]
	for _ in range(v) : 
		x, y = map(int, file.readline().split())
		edges[x].append(y)
		edges[y].append(x)
	answer = int(file.readline())
	file.readline()

	print(n, v, answer)
	for ed in edges : 
		print(ed)

	visited = [False for _ in range(n+1)]
	count = 0
	
	for i in range(1, n+1) :
		if not visited[i] :
			count += 1
			dfs(i)
			
	print(count)
		

file.close()

# # 백준 제출용
# import sys

# sys.setrecursionlimit(10**9)

# def dfs(node) : 
# 	visited[node] = True

# 	for e in edges[node] : 
# 		if not visited[e] :
# 			dfs(e)
			
# n, v = map(int, sys.stdin.readline().split())
# edges = [[] for _ in range(n+1)]
# for _ in range(v) : 
# 	x, y = map(int, sys.stdin.readline().split())
# 	edges[x].append(y)
# 	edges[y].append(x)

# visited = [False for _ in range(n+1)]
# count = 0

# for i in range(1, n+1) :
# 	if not visited[i] :
# 		count += 1
# 		dfs(i)
		
# print(count)