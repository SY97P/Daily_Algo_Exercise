# 6

file = open("./백준/dp/lv2/앱.txt", "r")

input = file.readline

def solve() : 
	for i in range(1, n + 1) : 
		for j in range(1, bound + 1) :
			if j >= cost[i] :
				dp[i][j] = max(dp[i-1][j], memo[i] + dp[i-1][j-cost[i]])
			else : 
				dp[i][j] = dp[i-1][j]

def findAnswer() :
	for i in range(1, bound + 1) :
		for j in range(1, n + 1) :
			if dp[j][i] >= m : 
				return i
	return 0

n, m = map(int, input().split())
memo = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))

bound = sum(cost)

dp = [[0 for _ in range(bound + 1)] for _ in range(n + 1)]

solve()

print(findAnswer())

file.close()