import sys

sys.setrecursionlimit(10**5)

def dfs(node, depth):
	dep[node] = depth
	cal[node] = True

	for next_node in adj[node]:
		if cal[next_node]:
			continue
		par[next_node] = node
		dfs(next_node, depth + 1)

def lca(u, v):
	while dep[u] != dep[v]:
		if dep[u] > dep[v]:
			u = par[u]
		else:
			v = par[v]
	while u != v:
		u = par[u]
		v = par[v]
	return u

# n = int(input())
# arr = []
# max_node = 0

# for _ in range(n):
# 	x, y = map(int, input().split())
# 	arr.append([x, y])
# 	max_node = max(max_node, x, y)

# adj = [[] for _ in range(max_node+1)]
# for x, y in arr:
# 	adj[x].append(y)
# 	adj[y].append(x)


n = 7
max_node = 7
adj = [[], [2, 3], [1,4,5], [1,6,7], [2], [2], [3], [3]]


par = [0] * (max_node+1)
dep = [0] * (max_node+1)
cal = [0] * (max_node+1)

dfs(1, 0)

m = int(input())
for _ in range(m):
	u, v = map(int, input().split())
	print(lca(u, v))