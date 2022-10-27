# 해결방안 3번 :
# bfs 
# 순간이동은 큐 앞에 추가하는 방식
from collections import deque

file = open("./bfs/숨바꼭질3tc.txt", "r")

def bfs(queue) :
	global k 
	global maxindex
	
	while queue : 
		curr, time = queue.popleft()
		
		candi = [(curr * 2, time), (curr + 1, time +1), (curr-1, time + 1)]
		for i, c in enumerate(candi) : 
			loc, tim = c
			if visited[k] != 0 and visited[k] < tim :
				continue
			if 0 < loc < maxindex :
				# 갑이 있는데 tim이 더 작을 때 -> 추가
				if visited[loc] == 0 or (visited[loc] != 0 and visited[loc] > tim) :
					# print(loc, tim)
					visited[loc] = tim
					if i == 0 :
						queue.appendleft(c)
					else : 
						queue.append(c)
		
for _ in range(10) : 
	n, k = map(int, file.readline().split())
	answer = int(file.readline())
	file.readline()

	print(n, k, answer)

	if n >= k :
		print(n-k)
	else :
		maxindex = 200000
		visited = [0 for _ in range(maxindex)]
		bfs(deque([(n, 1)]))
		print(visited[k]-1)
	print()

file.close()

# # 백준 제출용
# from collections import deque
# from sys import stdin

# def bfs(queue) :
# 	global k 
# 	global maxindex
	
# 	while queue : 
# 		curr, time = queue.popleft()
		
# 		candi = [(curr * 2, time), (curr + 1, time +1), (curr-1, time + 1)]
# 		for i, c in enumerate(candi) : 
# 			loc, tim = c
# 			if visited[k] != 0 and visited[k] < tim :
# 				continue
# 			if 0 < loc < maxindex :
# 				# 갑이 있는데 tim이 더 작을 때 -> 추가
# 				if visited[loc] == 0 or (visited[loc] != 0 and visited[loc] > tim) :
# 					# print(loc, tim)
# 					visited[loc] = tim
# 					if i == 0 :
# 						queue.appendleft(c)
# 					else : 
# 						queue.append(c)
		
# n, k = map(int, stdin.readline().split())

# if n >= k :
# 	print(n-k)
# else :
# 	maxindex = 200000
# 	visited = [0 for _ in range(maxindex)]
# 	bfs(deque([(n, 1)]))
# 	print(visited[k]-1)



# # 해결방안 2번 
# # 다익스트라 (heapq)
# import heapq

# file = open("./bfs/숨바꼭질3tc.txt", "r")

# def dijkstra(queue) : 
# 	global k
	
# 	while queue : 
# 		time, curr = heapq.heappop(queue)

# 		# print(curr, time)

# 		# 원래 있던 값보다 작을 때만 연산
# 		candi = [(time, curr * 2), (time + 1, curr + 1), (time + 1, curr-1)]
# 		for c in candi : 
# 			tim, loc = c
# 			if visited[k] != 0 and visited[k] < tim :
# 				continue
# 			if 0 < loc < 200000 :
# 				# 갑이 있는데 tim이 더 작을 때 -> 추가
# 				if visited[loc] == 0 or (visited[loc] != 0 and visited[loc] > tim) :
# 					# print(loc, tim)
# 					visited[loc] = tim
# 					heapq.heappush(queue, c)
			
# for _ in range(10) :
# 	n, k = map(int, file.readline().split())
# 	answer = int(file.readline())
# 	file.readline()

# 	print(n, k, answer)
	
# 	if n >= k :
# 		print(n-k)
# 	else : 
# 		visited = [0 for i in range(200001)]
# 		queue = [(0, n)]
# 		heapq.heapify(queue)
# 		dijkstra(queue)
# 		print(visited[k])


# # 백준 제출용
# # 해결방안 2번 
# # 다익스트라 (heapq)
# import heapq
# from sys import stdin

# def dijkstra(queue) : 
# 	global k
	
# 	while queue : 
# 		time, curr = heapq.heappop(queue)

# 		# print(curr, time)

# 		# 원래 있던 값보다 작을 때만 연산
# 		candi = [(time, curr * 2), (time + 1, curr + 1), (time + 1, curr-1)]
# 		for c in candi : 
# 			tim, loc = c
# 			if visited[k] != 0 and visited[k] < tim :
# 				continue
# 			if 0 < loc < 200000 :
# 				# 갑이 있는데 tim이 더 작을 때 -> 추가
# 				if visited[loc] == 0 or (visited[loc] != 0 and visited[loc] > tim) :
# 					# print(loc, tim)
# 					visited[loc] = tim
# 					heapq.heappush(queue, c)
			
# n, k = map(int, stdin.readline().split())

# if n >= k :
# 	print(n-k)
# else : 
# 	visited = [0 for i in range(200001)]
# 	queue = [(0, n)]
# 	heapq.heapify(queue)
# 	dijkstra(queue)
# 	print(visited[k])

		

# # # # 해결방안 1번 
# # # BFS (Dijkstra Algorithm)
# # from collections import deque

# # file = open("./bfs/숨바꼭질3tc.txt", "r")

# # def bfs(queue) : 
# # 	global k
	
# # 	while queue : 
# # 		curr, time = queue.popleft()

# # 		# print(curr, time)

# # 		# 원래 있던 값보다 작을 때만 연산
# # 		candi = [(curr * 2, time), (curr + 1, time +1), (curr-1, time + 1)]
# # 		for c in candi : 
# # 			loc, tim = c
# # 			if visited[k] != 0 and visited[k] < tim :
# # 				continue
# # 			if 0 < loc < 200000 :
# # 				# 갑이 있는데 tim이 더 작을 때 -> 추가
# # 				if visited[loc] == 0 or (visited[loc] != 0 and visited[loc] > tim) :
# # 					# print(loc, tim)
# # 					visited[loc] = tim
# # 					if not queue or queue[0][1] < tim :
# # 						queue.append(c)
# # 					else : 
# # 						queue.appendleft(c)
			
# # for _ in range(10) :
# # 	n, k = map(int, file.readline().split())
# # 	answer = int(file.readline())
# # 	file.readline()

# # 	print(n, k, answer)
	
# # 	if n >= k :
# # 		print(n-k)
# # 	else : 
# # 	visited = [0 for i in range(200001)]
# # 		bfs(deque([(n, 0)]))
# # 		print(visited[k])

# # # 백준 제출용
# # # # 해결방안 1번 
# # # # BFS (Dijkstra Algorithm)
# # # from collections import deque
# # # import sys

# # # def bfs(queue) : 
# # # 	global k
	
# # # 	while queue : 
# # # 		curr, time = queue.popleft()

# # # 		# print(curr, time)

# # # 		# 원래 있던 값보다 작을 때만 연산
# # # 		candi = [(curr * 2, time), (curr + 1, time +1), (curr-1, time + 1)]
# # # 		for c in candi : 
# # # 			loc, tim = c
# # # 			if visited[k] != 0 and visited[k] < tim :
# # # 				continue
# # # 			if 0 < loc < 200000 :
# # # 				# 갑이 있는데 tim이 더 작을 때 -> 추가
# # # 				if visited[loc] == 0 or (visited[loc] != 0 and visited[loc] > tim) :
# # # 					# print(loc, tim)
# # # 					visited[loc] = tim
# # # 					if not queue or queue[0][1] < tim :
# # # 						queue.append(c)
# # # 					else : 
# # # 						queue.appendleft(c)
			
# # # n, k = map(int, sys.stdin.readline().split())

# # # if n >= k :
# # # 	print(n-k)
# # # else : 
# # # 	visited = [0 for i in range(200000)]
# # # 	bfs(deque([(n, 0)]))
# # # 	print(visited[k])

