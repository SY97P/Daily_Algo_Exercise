# 35

file = open("./백준/dp/lv3/외판원순회.txt", "r")

input = file.readline

def dfs(curr, visited, cost, start) : 
	dp[curr][visited] = cost

	if visited == (1<<n) - 1 : 
		print(start, visited)
		dp[start][visited] += w[curr][start]
		return

	for i in range(n) : 
		if not visited & (1<<i) and dp[i][visited|1<<i] > cost + w[curr][i] :
			dfs(i, visited | 1<<i, cost + w[curr][i], start)
			

n = int(input())
w = [list(map(int ,input().split())) for _ in range(n)]

# dp[curr][visited] : curr 도시에 있을 때 방문상황 visited 에 대한 최소비용
dp = [[float('inf') for _ in range(1 << n)] for _ in range(n)]

for i in range(n) : 
	dfs(i, 1<<i, 0, i)

for d in dp : 
	print(d)

file.close()