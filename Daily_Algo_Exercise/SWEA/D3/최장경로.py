#1 1
#2 3

file = open("./SWEA/D3/최장경로.txt", "r")

input = file.readline

t = int(input())

def dfs(node, dept) : 
	global dist

	dist = max(dist, dept)
	
	for ad in adj[node] : 
		if not visited[ad] : 
			visited[ad] = True
			dfs(ad, dept + 1)
			visited[ad] = False

for tc in range(1, t + 1) : 
	n, m = map(int, input().split())
	adj = [set() for _ in range(n + 1)]

	for _ in range(m) : 
		x, y = map(int, input().split())
		adj[x].add(y)
		adj[y].add(x)

	dist = 0
	
	for i in range(1, n + 1) : 
		visited = [False for _ in range(n + 1)]
		visited[i] = True
		dfs(i, 1)
		visited[i] = False

	print("#%d %d" % (tc, dist))

file.close()