from collections import deque
from copy import deepcopy

n = int(input())

indegree = [0] * (n+1)
time = [0] * (n+1)
adj = [[] for _ in range(n+1)]

for i in range(1, n+1):
	data = list(map(int, input().split()))
	time[i] = data[0]
	for x in data[1:-1]:
		indegree[i] += 1
		adj[x].append(i)

def topology_sort():
	result = deepcopy(time)
	q = deque()

	for i in range(1, n+1):
		if indegree[i] == 0:
			q.append(i)

	while q:
		node = q.popleft()

		for next_node in adj[node]:
			result[next_node] = max(result[next_node], result[node] + time[next_node])
			indegree[next_node] -= 1
			if indegree[next_node] == 0:
				q.append(next_node)

	print(result)

topology_sort()