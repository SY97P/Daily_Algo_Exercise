file = open("./bfs/중량제한tc.txt", "r")

import heapq

def bfs(start, end) : 
	queue = [(0, start)]
	heapq.heapify(queue)

	step = 1

	while queue : 
		weight, node = heapq.heappop(queue)
		weight = -1 * weight

		print("step ", step, "weight, node : ", weight, node)
		print(queue)

		if node == end :
			print(weight) 
			break

		# 갱신을 할 필요가 없다
		if dp[node] > weight : 
			continue

		for wt, nd in adj[node] : 
			# start node 일 때
			if weight == 0 :
				dp[nd] = wt
				heapq.heappush(queue, (-1 * wt, nd))
			elif dp[nd] < weight and dp[nd] < wt : 
				dp[nd] = min(weight, wt)
				heapq.heappush(queue, (-1 * dp[nd], nd))
	

for tc in range(2) :
	n, m = map(int,file.readline().split())
	adj = [[] for _ in range(n + 1)]
	for _ in range(m) :
		a, b, c = map(int, file.readline().split())
		adj[a].append((c, b))
		adj[b].append((c, a))
	start, end = map(int, file.readline().split())
	answer = int(file.readline())
	file.readline()

	for i in range(1, n+1) :
		adj[i].sort(reverse = True)

	print(n, m, answer)
	print(start, end)
	print(adj)

	dp = [0 for _ in range(n + 1)]

	bfs(start, end)

file.close()

# 백준 제출용
import sys
import heapq

file = sys.stdin

def bfs(start, end) : 
	queue = [(0, start)]
	heapq.heapify(queue)

	step = 1

	while queue : 
		weight, node = heapq.heappop(queue)
		weight = -1 * weight

		print("step ", step, "weight, node : ", weight, node)
		print(queue)

		if node == end :
			print(weight) 
			break

		# 갱신을 할 필요가 없다
		if dp[node] > weight : 
			continue

		for wt, nd in adj[node] : 
			# start node 일 때
			if weight == 0 :
				dp[nd] = wt
				heapq.heappush(queue, (-1 * wt, nd))
			elif dp[nd] < weight and dp[nd] < wt : 
				dp[nd] = min(weight, wt)
				heapq.heappush(queue, (-1 * dp[nd], nd))
	

n, m = map(int,file.readline().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m) :
	a, b, c = map(int, file.readline().split())
	adj[a].append((c, b))
	adj[b].append((c, a))
start, end = map(int, file.readline().split())

for i in range(1, n+1) :
	adj[i].sort(reverse = True)

dp = [0 for _ in range(n + 1)]

bfs(start, end)
