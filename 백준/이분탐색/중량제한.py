file = open("./이진탐색/중량제한tc.txt", "r")

from collections import deque

def bfs(mid) : 
	global start
	global end

	queue = deque([start])
	while queue : 
		curr = queue.popleft()

		if curr == end :
			return True

		for nd, wt in adj[curr] :
			if not visited[nd] and mid <= wt :
				visited[nd] = True
				queue.append(nd)
	return False
	

for tc in range(2) : 
	n, m = map(int, file.readline().split())
	adj = [set() for _ in range(n + 1)]
	for _ in range(m) :
		a, b, c = map(int, file.readline().split())
		adj[a].add((b, c))
		adj[b].add((a, c))
	start, end = map(int, file.readline().split())
	answer = int(file.readline())
	file.readline()

	print(n, m, answer)
	print(start, end)
	print(adj)

	left, right = 1, 10 ** 9
	answer = 0
	while left <= right : 
		mid = (left + right) // 2
		visited = [False for _ in range(n + 1)]

		# 해당 값으로 경로가 가능하면
		# 더 큰 값으로 가능한지 이분탐색 시도
		if bfs(mid) :
			left = mid + 1
			answer = mid
		else : 
			right = mid - 1

	print(answer)
	print()


file.close()


# 백준 제출용
# import sys
# from collections import deque

# file = sys.stdin

# def bfs(mid) : 
# 	global start
# 	global end

# 	queue = deque([start])
# 	while queue : 
# 		curr = queue.popleft()

# 		if curr == end :
# 			return True

# 		for nd, wt in adj[curr] :
# 			if not visited[nd] and mid <= wt :
# 				visited[nd] = True
# 				queue.append(nd)
# 	return False
	

# n, m = map(int, file.readline().split())
# adj = [set() for _ in range(n + 1)]
# for _ in range(m) :
# 	a, b, c = map(int, file.readline().split())
# 	adj[a].add((b, c))
# 	adj[b].add((a, c))
# start, end = map(int, file.readline().split())

# left, right = 1, 10 ** 9
# answer = 0
# while left <= right : 
# 	mid = (left + right) // 2
# 	visited = [False for _ in range(n + 1)]

# 	# 해당 값으로 경로가 가능하면
# 	# 더 큰 값으로 가능한지 이분탐색 시도
# 	if bfs(mid) :
# 		left = mid + 1
# 		answer = mid
# 	else : 
# 		right = mid - 1

# print(answer)
	