file = open("./Daily_Algo_Exercise/이코테/기출/그래프이론/최종순위.txt")

input = file.readline 


from collections import deque

t = int(input())
for tc in range(t):
	n = int(input())
	grade = list(map(int, input().split()))
	indgree = [0] * (n+1)
	matrix = [[False] * (n+1) for _ in range(n+1)]
	for i in range(n-1):
		for j in range(i+1, n):
			matrix[grade[i]][grade[j]] = True
			indgree[grade[j]] += 1
			
	m = int(input())
	for _ in range(m):
		a, b = map(int, input().split())
		if matrix[a][b]:
			matrix[a][b] = False 
			matrix[b][a] = True
			indgree[a] += 1
			indgree[b] -= 1
		else:
			matrix[a][b] = True
			matrix[b][a] = False
			indgree[a] -= 1
			indgree[b] += 1

	q = deque()
	for i in range(1, n+1):
		if indgree[i] == 0:
			q.append(i)

	result = []
	cycle = False
	incorr = False
	for k in range(n):
		if not q:
			cycle = True
			break
		if len(q) > 1:
			incorr = True
			break
		node = q.popleft()
		result.append(node)
		for i in range(1,n+1):
			if matrix[node][i]:
				indgree[i] -= 1
				if indgree[i] == 0:
					q.append(i)

	if cycle:
		print("IMPSSIBLE")
	elif incorr:
		print("?")
	else:
		for r in result:
			print(r, end=" ")
		print()
			
	

file.close()