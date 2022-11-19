file = open("./빈출_알고리즘/lca.txt", "r")

input = file.readline

import sys

sys.setrecursionlimit(int(1e5))



LOG = 21 # 2 ^ 20 = 1,000,000

n = int(input())

par = [[0] * LOG for _ in range(n + 1)]
dep = [-1] * (n + 1)
adj = [[] for _ in range(n + 1)]

for _ in range(n) : 
	a, b = map(int, input().split())
	adj[a].append(b)
	adj[b].append(a)

# 모든 노드 depth 구함
def dfs(node, depth) : 
	dep[node] = depth
	for ad in adj[node] : 
		if dep[ad] < 0 : 
			continue
		par[ad][0] = node
		dfs(ad, depth + 1)

# 모든 노드와 2^i 만큼 떨어진 부모 노드 구함
def set_parent() : 
	dfs(1, 0)
	for i in range(1, LOG) : 
		for j in range(LOG - 1, -1, -1) : 
			par[j][i] = par[par[j][i-1]][i-1]

def lca(u, w) : 
	# 두 정점 depth가 같아지도록 한 쪽을 올림
	if dep[a] > dep[b] : # 무조건 b가 더 깊도록 조정
		a, b = b, a

	for i in range(LOG - 1, -1, -1) : 
		if d[b] - d[a] >= (1 << i) : 
			b = par[b][i]

	# 두 정점의 공통 부모를 찾을 때까지 거슬러올라감
	if a == b :
		return a

	for i in range(LOG - 1, -1, -1) : 
		if par[a][i] != par[b][i] : 
			a = par[a][i]
			b = par[b][i]

	return par[a][0]
			
# 모든 노드에 대해서 깊이와 2^i 만큼 거리의 부모 정보를 가져옴
set_parent()

m = int(input())

for _ in range(m) :
	u, w = map(int, input().split())
	print(lca(u, w))

file.close()