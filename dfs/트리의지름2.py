# 트리 지름 구하는 방법 이용

file = open("./dfs/트리의지름2tc.txt", "r")

def dfs(node, sumof) : 
	global far_node
	global far_weight
	
	visited[node] = True

	for ad in adj[node] :
		n, w = ad
		if not visited[n] :
			dfs(n, sumof + w)

	if sumof > far_weight : 
		far_weight = sumof
		far_node = node

for tc in range(8) :
	v = int(file.readline())
	adj = [[] for _ in range(v+1)]
	for _ in range(v) :
		line = list(map(int, file.readline().split()))
		print(line)
		node = line[0]
		for i in range(1, len(line)-1, 2) :
			adj[node].append((line[i], line[i+1]))
	answer = int(file.readline())
	file.readline()
	
	print(v, answer)
	for ad in adj : 
		print(ad)
	
	# 트리에서 가장 먼 노드 t 구하기
	visited = [False for _ in range(v + 1)]
	far_node = 0
	far_weight = 0
	dfs(1, 0)
	print(far_node, far_weight)
	
	visited = [False for _ in range(v + 1)]
	t_node = far_node
	far_node, far_weight = 0, 0
	dfs(t_node, 0)
	
	print(far_weight)

file.close()

# 백준 제출용
# # 트리 지름 구하는 방법 이용
# import sys

# sys.setrecursionlimit(10 ** 5)

# def dfs(node, sumof) : 
# 	global far_node
# 	global far_weight
	
# 	visited[node] = True

# 	for ad in adj[node] :
# 		n, w = ad
# 		if not visited[n] :
# 			dfs(n, sumof + w)

# 	if sumof > far_weight : 
# 		far_weight = sumof
# 		far_node = node

# v = int(sys.stdin.readline())
# adj = [[] for _ in range(v+1)]
# for node in range(v) :
# 	line = list(map(int, sys.stdin.readline().split()))
# 	node = line[0]
# 	for i in range(1, len(line)-1, 2) :
# 		adj[node].append((line[i], line[i+1]))

# # 트리에서 가장 먼 노드 t 구하기
# visited = [False for _ in range(v + 1)]
# far_node = 0
# far_weight = 0
# dfs(1, 0)

# visited = [False for _ in range(v + 1)]
# t_node = far_node
# far_node, far_weight = 0, 0
# dfs(t_node, 0)

# print(far_weight)
