file = open("./Daily_Algo_Exercise/이코테/기출/dbfs/특정거리의도시찾기.txt")

input = file.readline 

import heapq

n, m, k, x = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
	a, b = map(int, input().split())
	adj[a].append(b)

def bfs():
	dp = [int(1e9)] * (n+1)
	dp[x] = 0
	
	q = [(dp[x], x)]
	heapq.heapify(q)

	while q:
		cost, node = heapq.heappop(q)

		if cost > dp[node]:
			continue

		for next_node in adj[node]:
			if dp[next_node] > cost + 1:
				dp[next_node] = cost + 1
				heapq.heappush(q, (dp[next_node], next_node))

	result = []
	for i in range(1, n+1):
		if dp[i] == k:
			result.append(i)
	if not result:
		result.append(-1)
	return result
	

answer = bfs()
for a in answer:
	print(a)

file.close()