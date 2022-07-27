# 해결방안 1번 : 
# DFS
# 모든 노드를 시작점으로 하는 DFS연산
# 각 노드에 대해 0집합, 1집합으로 구분. 초기값 -1
# 원래 값과 다르면 no, 연산 종료까지 모순 없으면 yes

file = open("./dfs/이분그래프tc.txt", "r")

def dfs(node, adj, code) : 
	print(node, code, set_div)
	# 종료조건
	# 넣어야 할 값 != 이미 있는 값 -> 모순 : return "paradox"
	if set_div[node] != -1 and code != set_div[node] : 
		print("paradox")
		return "paradox"

	set_div[node] = code

	# 재귀
	for ad in adj[node] :
		adj[node].remove(ad)
		adj[ad].remove(node)
		return dfs(ad, adj, 0 if code != 0 else 1)
		adj[node].append(ad)
		adj[ad].append(node)

	

k = int(file.readline())
for tc in range(k) :
	print(tc + 1, "번째 테스트 케이스 : ")
	v, e = map(int, file.readline().split())
	adj = [[] for _ in range(v+1)] # size : v + 1 (index 0 not used)
	for _ in range(e) : 
		x, y = map(int, file.readline().split())
		adj[x].append(y)
		adj[y].append(x)

	print(v, e)
	for ad in adj : 
		print(ad)

	set_div = [-1 for _ in range(v+1)] # 배열 크기 v + 1 (index 0 미사용!!)
	set_div[1] = 0	# 1번 노드는 0집합으로 고정
	paradox = False
	for n in range(1,v) : 
		# 현재 시작점 노드가 어떤 집합에 속해있는지 알아야 함. 
		if dfs(n, adj, set_div[n]) == "paradox" :
			paradox = True
			break
	if paradox : 
		print("NO")
	else :
		print("YES")
	print()

print()
for tc in range(k) : 
	print(tc + 1, "번째 테스트 케이스 정답 : ", (file.readline().strip("\n")))


file.close()

# 백준 제출용
# 해결방안 1번 : 
# DFS
# 모든 노드를 시작점으로 하는 DFS연산
# 각 노드에 대해 0집합, 1집합으로 구분. 초기값 -1
# 원래 값과 다르면 no, 연산 종료까지 모순 없으면 yes
import sys

def dfs(node, adj, code) : 
	# print(node, code, set_div)
	# 종료조건
	# 넣어야 할 값 != 이미 있는 값 -> 모순 : return "paradox"
	if set_div[node] != -1 and code != set_div[node] : 
		# print("paradox")
		return "paradox"

	set_div[node] = code

	# 재귀
	for ad in adj[node] :
		adj[node].remove(ad)
		adj[ad].remove(node)
		return dfs(ad, adj, 0 if code != 0 else 1)
		adj[node].append(ad)
		adj[ad].append(node)

k = int(sys.stdin.readline())
for tc in range(k) :
	print(tc + 1, "번째 테스트 케이스 : ")
	v, e = map(int, sys.stdin.readline().split())
	adj = [[] for _ in range(v+1)] # size : v + 1 (index 0 not used)
	for _ in range(e) : 
		x, y = map(int, sys.stdin.readline().split())
		adj[x].append(y)
		adj[y].append(x)

	set_div = [-1 for _ in range(v+1)] # 배열 크기 v + 1 (index 0 미사용!!)
	set_div[1] = 0	# 1번 노드는 0집합으로 고정
	paradox = False
	for n in range(1,v) : 
		# 현재 시작점 노드가 어떤 집합에 속해있는지 알아야 함. 
		if dfs(n, adj, set_div[n]) == "paradox" :
			paradox = True
			break
	if paradox : 
		print("NO")
	else :
		print("YES")