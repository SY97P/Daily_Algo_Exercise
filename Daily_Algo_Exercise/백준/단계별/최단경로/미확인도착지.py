# 4 5
# 6

file = open("./백준/최단경로/미확인도착지.txt", "r")

input = file.readline

import sys, heapq

# input = sys.stdin.readline

def solve(start) : 
	q = [(0, start)]
	heapq.heapify(q)

	while q : 
		cost, node = heapq.heappop(q)

		# print(cost, node)

		if cost > max(dp) : 
			continue 

		# print("adj : ", adj[node])

		for next_cost, next_node in adj[node] : 
			# print(next_node, next_cost + cost, dp[next_node])
			if next_cost + cost < dp[next_node] :
				dp[next_node] = next_cost + cost
				heapq.heappush(q, (dp[next_node], next_node))

		# print(node, q)

tc = int(input())

for _ in range(tc) : 
	n, m, t = map(int, input().split())
	s, g, h = map(int, input().split())

	adj = [[] for _ in range(n+1)]
	for _ in range(m) : 
		a, b, d = map(int, input().split())
		if (a == g and b == h) or (a == h and b == g) : 
			d -= 0.1
		adj[a].append((d, b))
		adj[b].append((d, a))

	# for i in range(1, n+1) : 
	# 	print(i, " ", adj[i])

	targets = [int(input()) for _ in range(t)]
	targets.sort()

	dp = [float('inf') for _ in range(n+1)]
	dp[s] = 0

	solve(s)

	# print(dp)

	result = []
	
	for target in targets : 
		if dp[target] < float('inf') and type(dp[target]) == float : 
			result.append(target)

	print(*result)

file.close()