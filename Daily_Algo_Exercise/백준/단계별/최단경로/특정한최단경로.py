# 7

file = open("./백준/최단경로/특정한최단경로.txt", "r")

input = file.readline

import heapq
from copy import deepcopy
import sys 

input = sys.stdin.readline

def solve(start, end) : 
	q = [(0, start)]
	heapq.heapify(q)

	dp = [INF for _ in range(n+1)]
	dp[start] = 0

	while q : 
		cost, node = heapq.heappop(q)

		if cost > dp[end] : 
			continue 

		for next_cost, next_node in adj[node] : 
			if next_cost + cost < dp[next_node] :
				dp[next_node] = next_cost + cost
				heapq.heappush(q, (dp[next_node], next_node))

	# print(dp)
	return dp[end]
			


n, e = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(e) : 
	a, b, c = map(int, input().split())
	adj[a].append((c, b))
	adj[b].append((c, a))

v = list(map(int, input().split()))

INF = float('inf')

result = INF

dist2 = solve(v[0], v[1])
for i in range(2) : 
	result = min(result, solve(1, v[i]) + dist2 + solve(v[~i], n))

print(result if result != INF else -1)


file.close()