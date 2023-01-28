# 35

file = open("./백준/dp/lv3/외판원순회.txt", "r")

input = file.readline

def dfs(node, visited) : 
	if visited == (1<<n) - 1: 
		if w[node][0] == 0 : 
			return float('inf')
		else : 
			return w[node][0]

	if dp[node][visited] != -1 : 
		return dp[node][visited]

	dist = float('inf')
	for i in range(1, n) : 
		if visited & 1<<i == 0 and w[node][i] != 0 : 
			dist = min(dist, dfs(i, visited|1<<i) + w[node][i])

	dp[node][visited] = dist
	return dp[node][visited]

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * (1<<n) for _ in range(n)]

print(dfs(0, 1))

file.close()