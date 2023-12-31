# 75

file = open("./백준/dp/계단오르기.txt", "r")

input = file.readline

def getScore() : 
	for i in range(2, n+1) : 
		dp[i][1] = dp[i-2][0] + stairs[i]
		dp[i][2] = dp[i-1][1] + stairs[i]
		dp[i][0] = max(dp[i][1], dp[i][2])
	return dp[-1][0]

n = int(input())

stairs = [0] + [int(input()) for _ in range(n)]

dp = [[0, 0, 0], [stairs[1], stairs[1], stairs[1]]] + [[0, 0, 0] for _ in range(n - 1)]

print(getScore())


file.close()