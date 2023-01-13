# 1
# 9
# 4

# 다익스트라 알고리즘은 
# 1. 우선순위 큐 (힙큐) 사용
# 2. 중복확인 안 해도 됨
# 3. 인접리스트 만들 때 dict 쓰면 시간초과 남 -> list 사용
# 4. sys.stdin.readline 안 쓰면 시간초과 남 -> 적당히 데이터 많겠다 싶으면 쓸 것.

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