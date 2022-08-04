# DFS
# 이진 트리 아니란다!!
file = open("./dfs/트리의지름tc.txt", "r")

for tc in range(8) :
	n = int(file.readline())
	adj = [[] for _ in range(n+1)]
	dp = [dict() for _ in range(n+1)]
	for _ in range(n-1) :
		p, c, w = map(int, file.readline().split())
		adj[p].append((c, w))
		dp[p][c] = 0
		adj[c].append((p, w))
		dp[c][p] = 0
	answer = int(file.readline())
	file.readline()
	
	print(n, answer)
	for ad in adj :
		print(ad)
	
	maxValue = 0
	
	def dfs(info, visited) :
		pre, now, weight = info

		if dp[pre][now] != 0 :
			return dp[pre][now]

		visited[now] = True

		dp_value = 0
		for ad in adj[now] :
			n, w = ad
			if not visited[n] :
				rtn = dfs((now, n, w), visited)
				if dp_value < rtn :
					dp_value = rtn
					
		dp[pre][now] = dp_value + weight
		return dp[pre][now]
		
	
	# 모든 노드를 기준으로 지름을 만들어야 함
	for node in range(1, n+1) :

		visited = [False for _ in range(n+1)]
		visited[node] = True
		
		# 1 depth에서는 모든 방향을 다 가봐야 함. 
		weights = []
		for ad in adj[node] :
			next, weight = ad
			# 가려는 방향의 dp값이 있으면 그냥 가지고 있으면 됨
			weights.append(dfs((node, next, weight), visited))

		weights.sort(reverse = True)
		
		if len(weights) < 2: 
			if maxValue < sum(weights) :
				maxValue = sum(weights)
		else : 
			if maxValue < sum(weights[:2]) :
				maxValue = sum(weights[:2])
			
		
	print("maxValue : ", maxValue)
	

file.close()