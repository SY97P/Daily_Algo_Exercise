# 0
# 2
# 3
# 7
# INF

file = open("./백준/최단경로/최단경로.txt", "r")

input = file.readline

import heapq

def makeMap() : 
	adj = [[] for _ in range(v+1)]
	for _ in range(e) : 
		a, b, w = map(int, input().split())
		adj[a].append([w, b])

	return adj

def printDP() : 
	for val in dp[1:] : 
		if val == float('inf') : 
			print("INF")
		else : 
			print(val)

def solve() : 
	q = [(0, k)]
	heapq.heapify(q)

	while q : 
		cost, node = heapq.heappop(q)

		if cost > dp[node] : 
			continue

		for next_cost, next_node in adj[node] : 
			if next_cost + cost < dp[next_node] : 
				dp[next_node] = next_cost + cost
				heapq.heappush(q, (dp[next_node], next_node))

v, e = map(int, input().split())
k = int(input())

dp = [float('inf') for _ in range(v+1)]
dp[k] = 0

adj = makeMap()

solve()

printDP()

file.close()