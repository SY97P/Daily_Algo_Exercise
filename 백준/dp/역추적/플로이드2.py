# 0 2 3 1 4
# 12 0 15 2 5
# 8 5 0 1 1
# 10 7 13 0 3
# 7 4 10 6 0
# 0
# 2 1 2
# 2 1 3
# 2 1 4
# 3 1 3 5
# 4 2 4 5 1
# 0
# 5 2 4 5 1 3
# 2 2 4
# 3 2 4 5
# 2 3 1
# 3 3 5 2
# 0
# 2 3 4
# 2 3 5
# 3 4 5 1
# 3 4 5 2
# 4 4 5 1 3
# 0
# 2 4 5
# 2 5 1
# 2 5 2
# 3 5 1 3
# 3 5 2 4
# 0

file = open("./백준/dp/역추적/플로이드2.txt", "r")

input = file.readline

import heapq
# import sys

# input = sys.stdin.readline

def printTr() : 
	for i in range(1, n + 1) : 
		for pa in path[i][1:] :
			print(len(pa), * pa[::-1])

def printDP() : 
	for i in range(1, n + 1) : 
		print(*dp[i][1:])

def trace(start, end) :
	cost, city = dp[start][end], end

	while city != start : 
		for pre_cost, pre_city in rev[city] : 
			if dp[start][city] - pre_cost == dp[start][pre_city] : 
				path[start][end].append(pre_city)
				cost, city = pre_cost, pre_city
				break 

def solve(start, end) : 
	q = [(dp[start][start], start)]
	heapq.heapify(q)

	while q : 
		cost, city = heapq.heappop(q)

		if cost > dp[start][end] : 
			continue

		for next_cost, next_city in adj[city] : 
			if next_cost + cost < dp[start][next_city] : 
				dp[start][next_city] = next_cost + cost
				heapq.heappush(q, (dp[start][next_city], next_city))

n = int(input())
m = int(input())

adj = [[] for _ in range(n + 1)]
rev = [[] for _ in range(n + 1)]
for _ in range(m) : 
	a, b, c = map(int, input().split())
	adj[a].append((c, b))
	rev[b].append((c, a))

dp = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
path = [[[] for _ in range(n + 1)] for _ in range(n + 1)]

for start in range(1, n + 1) : 
	dp[start][start] = 0
	for end in range(1, n + 1) :
		if start == end : 
			continue
			
		solve(start, end)

		path[start][end] = [end]
		trace(start, end)

printDP()
printTr()
	
file.close()