file = open("./Daily_Algo_Exercise/이코테/기출/그래프이론/최종순위.txt")

input = file.readline 

from collections import deque

t = int(input())
for tc in range(t):
	n = int(input())
	degree = list(map(int, input().split()))
	indgree = [0] * (n+1)
	graph = [[False] * (n+1) for _ in range(n+1)]
	for i in range(n):
		for j in range(i+1, n):
			graph[degree[i]][degree[j]] = True 
			indgree[degree[j]] += 1
	m = int(input())
	for _ in range(m):
		a, b = map(int, input().split())
		if graph[a][b]:
			graph[a][b] = False
			graph[b][a] = True
			indgree[a] += 1
			indgree[b] -= 1
		else:
			graph[a][b] = True
			graph[b][a] = False
			indgree[a] -= 1
			indgree[b] += 1

	q = deque()
	for i in range(1, n+1):
		if indgree[i] == 0:
			q.append(i)

	cycle = False
	impos = False
	result = []
	for _ in range(n):
		if len(q) > 1:
			impos = True
			break
		elif len(q) == 0:
			cycle = True
			break
		now = q.popleft()
		result.append(now)
		for i in range(1, n + 1):
			if graph[now][i]:
				indgree[i] -= 1
				if indgree[i] == 0:
					q.append(i)


	if cycle:
		print("IMPOSSIBLE")
	elif impos:
		print("?")
	else:
		print(* result)
		
	

file.close()