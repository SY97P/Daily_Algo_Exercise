import heapq

n, m, c = map(int, input().split())

adj = [[] for _ in range(n+1)]
for _ in range(m):
	a, b, cost = map(int, input().split())
	adj[a].append((cost, b))

dp = [1e9] * (n+1)
dp[c] = 0

q = [(0, c)]
heapq.heapify(q)

while q:
	cost, node = heapq.heappop(q)

	if dp[node] < cost:
		continue

	for next_cost, next_node in adj[node]:
		if cost + next_cost < dp[next_node]:
			dp[next_node] = cost + next_cost
			heapq.heappush(q, (dp[next_node], next_node))

count = 0
max_cost = 0
for d in dp[1:]:
	if d < 1e9 and d > 0:
		count += 1
		if max_cost < d:
			max_cost = d
print(count, max_cost)
		