# 9
# 4
# 1

file = open("./백준/단계별/트리dp/트리와쿼리.txt")

input = file.readline 

# import sys 

# input = sys.stdin.readline 

# sys.setrecusionlimit(10**6)

def dfs(node) : 
	if dp[node] != 0 : 
		return dp[node]

	count = 1
	for next_node in adj[node] : 
		if not visited[next_node] : 
			visited[next_node] = True
			count += dfs(next_node)
		
	dp[node] = count
	return dp[node]


n, r, q = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(n-1) : 
	a, b = map(int, input().split())
	adj[a].append(b)
	adj[b].append(a)

dp = [0 for _ in range(n+1)]

visited = [False for _ in range(n+1)]
visited[r] = True

dfs(r)

for _ in range(q) : 
	print(dp[int(input())])


file.close()