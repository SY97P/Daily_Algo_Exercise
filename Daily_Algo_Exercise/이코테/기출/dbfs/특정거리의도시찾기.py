file = open("./Daily_Algo_Exercise/이코테/기출/dbfs/특정거리의도시찾기.txt")

input = file.readline 

import heapq

n, m, k, x = map(int, input().split())

adj = [[] for _ in range(n+1)]
for _ in range(m):
	a, b = map(int, input().split())
	adj[a].append(b)

def bfs():
	dp = [1e9 for _ in range(n+1)]
	dp[x] = 0
	
	q = []
	heapq.heappush(q, (dp[x], x))

	while q:
		cost, node = heapq.heappop(q)

		# print(node, adj[node])
		for next_node in adj[node]:
			if cost + 1 < dp[next_node]:
				dp[next_node] = cost + 1
				heapq.heappush(q, (dp[next_node], next_node))

	is_none = True
	for i, d in enumerate(dp):
		if d == k:
			is_none = False
			print(i)
	if is_none:
		print(-1)

bfs()

file.close()