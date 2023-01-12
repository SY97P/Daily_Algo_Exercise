# 1
# 9
# 4

file = open("./백준/dp/역추적/최소비용구하기2.txt", "r")

input = file.readline

import heapq

def solve() : 
	q = []
	heapq.heappush(q, (dp[start], start))

	while q : 
		cost, city = heapq.heappop(q)

		if cost > dp[end] : 
			continue

		for next_cost, next_city in adj[city] :
			if next_cost + cost < dp[next_city] : 
				dp[next_city] = next_cost + cost
				heapq.heappush(q, (dp[next_city], next_city))

n = int(input())
m = int(input())

adj = [[] for _ in range(n + 1)]
for _ in range(m) : 
	a, b, c = map(int, input().split())
	adj[a].append((c, b))

start, end = map(int, input().split())

dp = [float('inf') for _ in range(n+1)]
dp[start] = 0

solve()

print(dp[end])
print(dp)

file.close()