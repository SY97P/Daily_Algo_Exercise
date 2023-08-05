import heapq

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
	a, b = map(int, input().split())
	adj[a].append(b)
	adj[b].append(a)

dp = [1e9] * (n+1)
dp[1] = 0

q = [(dp[1], 1)]
heapq.heapify(q)

while q: 
	cost, node = heapq.heappop(q)

	for next_node in adj[node]:
		if cost + 1 < dp[next_node]:
			dp[next_node] = cost + 1
			heapq.heappush(q, (dp[next_node], next_node))

max_dist = 0
max_idx = 0
for i in range(1, n+1):
	if dp[i] > max_dist:
		max_dist = dp[i]
		max_idx = i
print(max_idx, max_dist, dp.count(max_dist))