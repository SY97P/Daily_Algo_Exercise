# 96
# 3
# 102
# 208
# 253

file = open("./백준/dp/RGB거리.txt", "r")

input = file.readline

def solve() :
	for i in range(1, n + 1) : 
		for j in range(3) : 
			temp = float('inf')
			for k in range(3) : 
				if k == j : 
					continue
				temp = min(temp, dp[i-1][k])
			dp[i][j] = costs[i][j] + temp

# for _ in range(5) : 
n = int(input())
costs = [[0 for _ in range(3)]] + [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(3)] for _ in range(n + 1)]

solve()

print(min(dp[-1]))

file.close()