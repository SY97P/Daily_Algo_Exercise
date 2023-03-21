# 30

file = open("./백준/dp/정수삼각형.txt", "r")

input = file.readline

def getCost() : 
	for i in range(n - 2, -1, -1) :
		for j in range(len(triangle[i])) :
			dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])
	return dp[0][0]

n = int(input())

triangle = [list(map(int, input().split())) for _ in range(n)]

dp = []

for i in range(n) :
	dp.append([])
	for j in range(len(triangle[i])) :
		if i == n - 1 : 
			dp[i].append(triangle[i][j])
			continue
		dp[i].append(0)

print(getCost())


file.close()