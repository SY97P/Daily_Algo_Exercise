# from collections import deque

# file = open("./bfs/DFS와BFStc.txt", "r")

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

# def dfs(v) :
# 	print(v, end = " ")
# 	visited[v] = True
# 	for ad in adj[v] :
# 		if not visited[ad] :
# 			dfs(ad)
# 			visited[ad] = True
			
	

# for _ in range(12) :
# 	n, m, start_v = map(int, file.readline().split())
# 	adj = [[] for _ in range(n+1)]
# 	for _ in range(m) :
# 		x, y = map(int, file.readline().split())
# 		adj[x].append(y)
# 		adj[y].append(x)

# 	print(n, m, start_v)
# 	for ad in adj :
# 		ad.sort()
# 		# print(ad)
# 	print()
		
# 	print("DFS answer : ", file.readline().strip("\n"))
# 	print("BFS answer : ", file.readline().strip("\n"))
# 	print()
# 	file.readline()		

	
# 	visited = [False for _ in range(n+1)]
# 	print("DFS result : ", end = "")
# 	dfs(start_v)
# 	print()
	
# 	bfs_result = []
# 	bfs(deque([start_v]), adj)
# 	print("BFS result : ", ' '.join(list(map(str, bfs_result))))
	
# 	print()
# 	print()

# file.close()


# 백준 제출용
import sys
from collections import deque

read = sys.stdin.readline


def dfs(v) : 
	print(v, end = " ")
	visited = True
	for ad in adj[v] : 
		if not visited[ad] : 
			dfs(ad)

def bfs(queue) : 
	while queue : 
		curr = queue.popleft()
		bfs_result.append(curr)
		for ad in adj[curr] : 
			if ad not in queue and ad not in bfs_result : 
				queue.append(ad)

				
# n, m, start_v = map(int, read().split())
file = open("./bfs/DFS와BFStc.txt", "r")
n, m, start_v = map(int, file.readline().split())
adj = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m) :
	# x, y = map(int, read().split())
	x, y = map(int, file.readline().split())
	adj[x].append(y)
	adj[y].append(x)
for i in range(len(adj)) : 
	adj[i].sort()

dfs(start_v)
print()
bfs_result = []
bfs(deque([start_v]))
print(' '.join(list(map(str, bfs_result))))
file.close()