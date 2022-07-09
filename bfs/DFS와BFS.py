from collections import deque

file = open("./bfs/DFS와BFStc.txt", "r")

def bfs(queue, adj) : 
	while queue : 
		curr = queue.popleft()
		# print(queue)
		bfs_result.append(curr)
		# print(curr, bfs_result)

		# curr랑 겹치는 거 나중에 제거하면 성능 안 좋아질 것 같으니
		# 여기서 조건문으로 거르기
		for ad in adj[curr] :
			if ad not in bfs_result and ad not in queue :
				queue.append(ad)

def dfs(adj, v, queue) : 
	# print("v is ", v)
	
	if len(adj[v]) == 0 :
		return queue

	for ad in adj[v] :
		print(ad)
		if ad not in queue : 
			temp = adj
			temp[v].remove(ad)
			temp[ad].remove(v)
			queue.append(ad)
			dfs(temp, ad, queue)
			
	return queue
	

for _ in range(12) :
	n, m, start_v = map(int, file.readline().split())
	adj = [[] for _ in range(n+1)]
	for _ in range(m) :
		x, y = map(int, file.readline().split())
		adj[x].append(y)
		adj[y].append(x)

	print(n, m, start_v)
	for ad in adj :
		ad.sort()
		# print(ad)
	print()
		
	print("DFS answer : ", file.readline().strip("\n"))
	print("BFS answer : ", file.readline().strip("\n"))
	print()
	file.readline()		

	
	# dfs_result = []
	print("DFS result : ", ' '.join(list(map(str, dfs(adj, start_v, [start_v])))))
	
	bfs_result = []
	bfs(deque([start_v]), adj)
	print("BFS result : ", ' '.join(list(map(str, bfs_result))))
	
	print()
	print()

file.close()


# 백준 제출용
# from collections import deque

# def bfs(queue, adj) : 
# 	while queue : 
# 		curr = queue.popleft()
# 		# print(queue)
# 		bfs_result.append(curr)
# 		# print(curr, bfs_result)

# 		# curr랑 겹치는 거 나중에 제거하면 성능 안 좋아질 것 같으니
# 		# 여기서 조건문으로 거르기
# 		for ad in adj[curr] :
# 			if ad not in bfs_result and ad not in queue :
# 				queue.append(ad)

# def dfs(adj, v, queue) : 
# 	# print("v is ", v)
	
# 	if len(adj[v]) == 0 :
# 		return queue

# 	for ad in adj[v] :
# 		if ad not in queue : 
# 			temp = adj
# 			temp[v].remove(ad)
# 			temp[ad].remove(v)
# 			queue.append(ad)
# 			return dfs(temp, ad, queue)
# 			queue.remove(ad)
			
# 	return queue
	
# n, m, start_v = map(int, input().split())
# adj = [[] for _ in range(n+1)]
# for _ in range(m) :
# 	x, y = map(int, input().split())
# 	adj[x].append(y)
# 	adj[y].append(x)
# for ad in adj :
# 	ad.sort()

# print(' '.join(list(map(str, dfs(adj, start_v, [start_v])))))

# bfs_result = []
# bfs(deque([start_v]), adj)
# print(' '.join(list(map(str, bfs_result))))