# 1
# 2
# 1 2
# 9
# 3
# 4 3 1 5 or 4 3 5
# 4
# 3
# 1 3 5

file = open("./백준/dp/역추적/최소비용구하기2.txt", "r")

input = file.readline

import heapq
import sys

input = sys.stdin.readline

def trace() :
	city = end
	cost = dp[end]

	while city != start : 
		for pre_cost, pre_city in rev[city] :
			if dp[city] - pre_cost == dp[pre_city] : 
				path.append(pre_city)
				city = pre_city
				cost = pre_cost
				break
	

def solve() : 
	q = [(dp[start], start)]
	heapq.heapify(q)

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
rev = [[] for _ in range(n + 1)]
for _ in range(m) : 
	a, b, c = map(int, input().split())
	adj[a].append((c, b))
	rev[b].append((c, a))

start, end = map(int, input().split())

dp = [float('inf') for _ in range(n + 1)]
dp[start] = 0

solve()

print(dp[end])

path = [end]
trace()

print(len(path))
print(*path[::-1])


file.close()