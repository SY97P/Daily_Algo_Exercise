file = open("./dfs/트리의지름tc.txt", "r")

# 트리 지름 구하는 법 
# 1. root에서 가장 먼 노드 t 찾기
# 2. t에서 가장 먼 노드 u 찾기
# 3. t - u 거리 구하기
def dfs(node, sumof) : 
	global node_result
	global weight_result
	
	visited[node] = True
	for ad in adj[node] : 
		if not visited[ad[0]] :
			dfs(ad[0], ad[1] + sumof)
	if weight_result < sumof :
		weight_result = sumof
		node_result = node

for tc in range(8) : 
	n = int(file.readline())
	adj = [[] for _ in range(n+1)]
	for _ in range(n-1) :
		p, c, w = map(int, file.readline().split())
		adj[p].append((c, w))
		adj[c].append((p, w))

	answer = int(file.readline())
	file.readline()

	print(n, answer)

	# 1번 
	visited = [False for _ in range(n+1)]
	node_result, weight_result = 0, 0
	dfs(1, 0)
	print(node_result, weight_result)

	visited = [False for _ in range(n+1)]
	node_t = node_result
	node_result, weight_result = 0, 0
	dfs(node_t, 0)
	print(node_result, weight_result)

	print()
	

file.close()

# 백준 제출용
# import sys


# sys.setrecursionlimit(10 ** 5)

# # 트리 지름 구하는 법 
# # 1. root에서 가장 먼 노드 t 찾기
# # 2. t에서 가장 먼 노드 u 찾기
# # 3. t - u 거리 구하기
# def dfs(node, sumof) : 
# 	global node_result
# 	global weight_result
	
# 	visited[node] = True
# 	for ad in adj[node] : 
# 		if not visited[ad[0]] :
# 			dfs(ad[0], ad[1] + sumof)
# 	if weight_result < sumof :
# 		weight_result = sumof
# 		node_result = node
	

# n = int(sys.stdin.readline())
# adj = [[] for _ in range(n+1)]
# for _ in range(n-1) :
# 	p, c, w = map(int, sys.stdin.readline().split())
# 	adj[p].append((c, w))
# 	adj[c].append((p, w))


# # 1번 
# visited = [False for _ in range(n+1)]
# node_result, weight_result = 0, 0
# dfs(1, 0)

# visited = [False for _ in range(n+1)]
# node_t = node_result
# node_result, weight_result = 0, 0
# dfs(node_t, 0)
# print(node_result, weight_result)