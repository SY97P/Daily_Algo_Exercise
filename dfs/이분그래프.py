# 해결방안 3번 : 
# BFS
# 1, 2번 시간초과, 메모리초과 문제 때문에 방식 변경
from collections import deque

file = open("./dfs/이분그래프tc.txt", "r")

def bfs(queue, visited) : 
	while queue : 
		node, code = queue.popleft()

		if set_div[node] != -1 and set_div[node] != code : 
			print("False")
			return False

		set_div[node] = code

		print(node, code, set_div)

		for ad in adj[node] :
			if not visited[ad] : 
				next_code = 0 if code != 0 else 1
				visited[ad] = True
				queue.append((ad, next_code))
	return True

result = []
k = int(file.readline())
for tc in range(k) : 
	v, e = map(int, file.readline().split())
	adj = [deque() for _ in range(v+1)]
	for _ in range(e) : 
		x, y = map(int, file.readline().split())
		adj[x].append(y)
		adj[y].append(x)

	for i, a in enumerate(adj) : 
		print(i, a)

	set_div = [-1 for _ in range(v+1)]
	set_div[1] = 0

	para = False
	for node in range(1, v+1) :
		visited = [False for _ in range(v+1)]
		visited[node] = True
		if not bfs(deque([(node, set_div[node])]), visited) :
			para = True
			break

	if para : 
		result.append("NO")
		print("NO")
	else : 
		result.append("YES")
		print("YES")

answer = [(file.readline().strip("\n")) for _ in range(k)]

for kk in range(k) : 
	print("answer , result : ", answer[kk], result[kk])

file.close()

# 백준 제출용
# BFS
# 1, 2번 시간초과, 메모리초과 문제 때문에 방식 변경
from collections import deque
import sys

def bfs(queue, visited) : 
	while queue : 
		node, code = queue.popleft()

		if set_div[node] != -1 and set_div[node] != code : 
			return False

		set_div[node] = code

		print(node, code, set_div)

		for ad in adj[node] :
			if not visited[ad] : 
				next_code = 0 if code != 0 else 1
				visited[ad] = True
				queue.append((ad, next_code))
	return True

k = int(sys.stdin.readline())
for tc in range(k) : 
	v, e = map(int, sys.stdin.readline().split())
	adj = [deque() for _ in range(v+1)]
	for _ in range(e) : 
		x, y = map(int, sys.stdin.readline().split())
		adj[x].append(y)
		adj[y].append(x)

	set_div = [-1 for _ in range(v+1)]
	set_div[1] = 0

	para = False
	for node in range(1, v+1) :
		visited = [False for _ in range(v+1)]
		visited[node] = True
		if not bfs(deque([(node, set_div[node])]), visited) :
			para = True
			break

	if para : 
		print("NO")
	else : 
		print("YES")

# # 해결방안 2번 :
# # DFS
# # 해결방안 1번을 좀 더 직관적으로 풀이
# from itertools import cycle

# file = open("./dfs/이분그래프tc.txt", "r")

# def dfs(node, adj, code) : 
# 	print("node : ", node, " code : ", code)

# 	if set_div[node] != -1 and code != set_div[node] :
# 		return False

# 	# 지금 노드에 들어오면서 set_div코드 갱신해줌
# 	set_div[node] = code

# 	# 갈 수 있는 곳을 다 가봄
# 	for ad in adj[node] : 
# 		# 재귀 전 해야할 일
# 		# 1. visited True
# 		# 2. adj[node] remove
# 		# 3. adj[ad] remove
# 		visited[node] = True
# 		adj[node].remove(ad)
# 		adj[ad].remove(node)
# 		next_code = 0 if code != 0 else 1
# 		return dfs(ad, adj, next_code)
# 		visited[node] = False
# 		adj[node].append(ad)
# 		adj[ad].append(node)
	

# 	return True


	
# k = int(file.readline())
# for tc in range(k) : 
# 	print(tc + 1, "번째 테스트 케이스")
# 	v, e = map(int, file.readline().split())
# 	adj = [[] for _ in range(v+1)] # size = v + 1
# 	for _ in range(e) : 
# 		x, y = map(int, file.readline().split())
# 		adj[x].append(y)
# 		adj[y].append(x)

# 	print(v, e)
# 	for a in adj :
# 		print(a)

# 	visited = [False for _ in range(v + 1)]
# 	set_div = [-1 for _ in range(v + 1)]
# 	para = []
	
# 	for node in range(1, v+1) : 
# 		if not visited[node] :
# 			visited[node] = True
# 			temp = set_div
# 			para.append(dfs(node, adj, 0))
# 			set_div = temp
# 			para.append(dfs(node, adj, 1))

# 	print(para)
				

# 	# para에 True가 하나라도 있으면 YES
# 	# 나머지는 NO
# 	if True in para : 
# 		print("YES")
# 	else : 
# 		print("NO")
# 	print()

# for tc in range(k):
# 	print(tc + 1, "번째 TC 정답 : ", file.readline().strip("\n"))

# file.close()

# # 백준 제출용
# import sys

# sys.setrecursionlimit(10 ** 9)

# def dfs(node, adj, code) : 
# 	if set_div[node] != -1 and code != set_div[node] :
# 		return False

# 	# 지금 노드에 들어오면서 set_div코드 갱신해줌
# 	set_div[node] = code

# 	# 갈 수 있는 곳을 다 가봄
# 	for ad in adj[node] : 
# 		# 재귀 전 해야할 일
# 		# 1. visited True
# 		# 2. adj[node] remove
# 		# 3. adj[ad] remove
# 		visited[node] = True
# 		adj[node].remove(ad)
# 		adj[ad].remove(node)
# 		next_code = 0 if code != 0 else 1
# 		return dfs(ad, adj, next_code)
# 		visited[node] = False
# 		adj[node].append(ad)
# 		adj[ad].append(node)
	

# 	return True


	
# k = int(sys.stdin.readline())
# for tc in range(k) : 
# 	v, e = map(int, sys.stdin.readline().split())
# 	adj = [[] for _ in range(v+1)] # size = v + 1
# 	for _ in range(e) : 
# 		x, y = map(int, sys.stdin.readline().split())
# 		adj[x].append(y)
# 		adj[y].append(x)

# 	visited = [False for _ in range(v + 1)]
# 	set_div = [-1 for _ in range(v + 1)]
	
# 	for node in range(1, v+1) : 
# 		if not visited[node] :
# 			visited[node] = True
# 			temp = set_div
# 			if not dfs(node, adj, 0) :
# 				set_div = temp
# 				if not dfs(node, adj, 1) :
# 					print("NO")
# 					exit(0)
# 	print("YES")
				


# # # 해결방안 1번 : 오답
# # # DFS
# # # 모든 노드를 시작점으로 하는 DFS연산
# # # 각 노드에 대해 0집합, 1집합으로 구분. 초기값 -1
# # # 원래 값과 다르면 no, 연산 종료까지 모순 없으면 yes

# # file = open("./dfs/이분그래프tc.txt", "r")

# # def dfs(node, adj, code) : 
# # 	print(node, code, set_div)
# # 	# 종료조건
# # 	# 넣어야 할 값 != 이미 있는 값 -> 모순 : return "paradox"
# # 	if set_div[node] != -1 and code != set_div[node] : 
# # 		print("paradox")
# # 		return "paradox"

# # 	set_div[node] = code

# # 	# 재귀
# # 	for ad in adj[node] :
# # 		adj[node].remove(ad)
# # 		adj[ad].remove(node)
# # 		return dfs(ad, adj, 0 if code != 0 else 1)
# # 		adj[node].append(ad)
# # 		adj[ad].append(node)

	

# # k = int(file.readline())
# # for tc in range(k) :
# # 	print(tc + 1, "번째 테스트 케이스 : ")
# # 	v, e = map(int, file.readline().split())
# # 	adj = [[] for _ in range(v+1)] # size : v + 1 (index 0 not used)
# # 	for _ in range(e) : 
# # 		x, y = map(int, file.readline().split())
# # 		adj[x].append(y)
# # 		adj[y].append(x)

# # 	print(v, e)
# # 	for ad in adj : 
# # 		print(ad)

# # 	visited = [False for _ in range(v+1)]
# # 	set_div = [-1 for _ in range(v+1)] # 배열 크기 v + 1 (index 0 미사용!!)
# # 	set_div[1] = 0	# 1번 노드는 0집합으로 고정
# # 	paradox = False
# # 	for n in range(1,v) : 
# # 		# 현재 시작점 노드가 어떤 집합에 속해있는지 알아야 함. 
# # 		if not visited[n] :
# # 			if dfs(n, adj, set_div[n]) == "paradox" :
# # 				paradox = True
# # 				break
# # 	if paradox : 
# # 		visited = [False for _ in range(v+1)]
# # 		set_div = [-1 for _ in range(v + 1)]
# # 		set_div[1] = 1
# # 		paradox2 = False
# # 		for ad in adj :
# # 			print(ad)
# # 		for n in range(1, v) :
# # 			if not visited[n] :
# # 				print(n, set_div[n])
# # 				if dfs(n, adj, set_div[n]) == "paradox" :
# # 					paradox2 = True
# # 					break
# # 		if paradox2 :
# # 			print("NO")
# # 		else : 
# # 			print("YES")
# # 	else :
# # 		print("YES")
# # 	print()

# # print()
# # for tc in range(k) : 
# # 	print(tc + 1, "번째 테스트 케이스 정답 : ", (file.readline().strip("\n")))


# # file.close()

# # # # 백준 제출용
# # # # 해결방안 1번 : 
# # # # DFS
# # # # 모든 노드를 시작점으로 하는 DFS연산
# # # # 각 노드에 대해 0집합, 1집합으로 구분. 초기값 -1
# # # # 원래 값과 다르면 no, 연산 종료까지 모순 없으면 yes
# # # import sys

# # # sys.setrecursionlimit(10 ** 9)

# # # def dfs(node, adj, code) : 
# # # 	# print(node, code, set_div)
# # # 	# 종료조건
# # # 	# 넣어야 할 값 != 이미 있는 값 -> 모순 : return "paradox"
# # # 	if set_div[node] != -1 and code != set_div[node] : 
# # # 		# print("paradox")
# # # 		return "paradox"

# # # 	set_div[node] = code

# # # 	# 재귀
# # # 	for ad in adj[node] :
# # # 		adj[node].remove(ad)
# # # 		adj[ad].remove(node)
# # # 		return dfs(ad, adj, 0 if code != 0 else 1)
# # # 		adj[node].append(ad)
# # # 		adj[ad].append(node)

# # # k = int(sys.stdin.readline())
# # # for tc in range(k) :
# # # 	print(tc + 1, "번째 테스트 케이스 : ")
# # # 	v, e = map(int, sys.stdin.readline().split())
# # # 	adj = [[] for _ in range(v+1)] # size : v + 1 (index 0 not used)
# # # 	for _ in range(e) : 
# # # 		x, y = map(int, sys.stdin.readline().split())
# # # 		adj[x].append(y)
# # # 		adj[y].append(x)

# # # 	visited = [False for _ in range(v+1)]
# # # 	set_div = [-1 for _ in range(v+1)] # 배열 크기 v + 1 (index 0 미사용!!)
# # # 	set_div[1] = 0	# 1번 노드는 0집합으로 고정
# # # 	paradox = False
# # # 	for n in range(1,v) : 
# # # 		# 현재 시작점 노드가 어떤 집합에 속해있는지 알아야 함. 
# # # 		if not visited[n] :
# # # 			if dfs(n, adj, set_div[n]) == "paradox" :
# # # 				paradox = True
# # # 				break
# # # 	if paradox : 
# # # 		visited = [False for _ in range(v+1)]
# # # 		set_div = [-1 for _ in range(v+1)]
# # # 		set_div[1] = 1
# # # 		paradox2 = False
# # # 		for n in range(1, v) : 
# # # 			if not visited[n] :
# # # 				if dfs(n, adj, set_div[n]) == "paradox" :
# # # 					paradox2 = True
# # # 					break
# # # 		if paradox2 :
# # # 			print("NO")
# # # 		else : 
# # # 			print("YES")
# # # 	else :
# # # 		print("YES")
