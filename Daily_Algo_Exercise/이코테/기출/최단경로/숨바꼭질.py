import heapq

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
	a, b = map(int, input().split())
	adj[a].append(b)
	adj[b].append(a)

dp = [int(1e9) for _ in range(n+1)]
dp[1] = 0

q = []
heapq.heappush(q, (0, 1))

while q:
	cost, node = heapq.heappop(q)

	if cost > dp[node]:
		continue

	for next_node in adj[node]:
		if dp[node] + 1 < dp[next_node]:
			dp[next_node] = dp[node] + 1
			heapq.heappush(q, (dp[next_node], next_node))

answer_idx, answer_dist = 0, 0
for i in range(1, n+1):
	if answer_dist <= dp[i]:
		if answer_dist < dp[i]:
			answer_idx = i
		answer_dist = dp[i]
print(answer_idx, answer_dist, dp.count(answer_dist))
		
		