file = open("./Daily_Algo_Exercise/이코테/기출/dbfs/특정거리의도시찾기.txt")

input = file.readline 

from collections import deque

n, m, k, x = map(int, input().split())

adj = [[] for _ in range(n+1)]
for _ in range(m):
	a, b = map(int, input().split())
	adj[a].append(b)

visited = [False] * (n+1)
visited[x] = True

q = deque([(0, x)])

result = []
while q:
	depth, node = q.popleft()

	if depth >= k:
		result.append(node)
		continue 

	for next_node in adj[node]:
		if not visited[next_node]:
			visited[next_node] = True
			q.append((depth + 1, next_node))

if not result:
	print(-1)
else:
	for r in result:
		print(r)


file.close()