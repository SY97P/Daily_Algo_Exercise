file = open("./이진탐색/중량제한tc.txt", "r")

for tc in range(1) : 
	n, m = map(int, file.readline().split())
	adj = [set() for _ in range(n + 1)]
	for _ in range(m) :
		a, b, c = map(int, file.readline().split())
		adj[a].add((b, c))
		adj[b].add((a, c))
	start, end = map(int, file.readline().split())
	answer = int(file.readline())

	print(n, m, answer)
	print(start, end)
	print(adj)

	left, right = 1, 10 ** 9
	while left <= right : 
		mid = (left + right) // 2

		if 

file.close()