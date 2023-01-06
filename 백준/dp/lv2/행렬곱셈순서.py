# 90 

file = open("./백준/dp/lv2/행렬곱셈순서.txt", "r")

input = file.readline

def getCount() : 
	for d in range(1, n) : 
		for i in range(n-d) : 
			j = i + d
			dp[i][j] = matrix[i][0] * matrix[j][0] * matrix[j][1]
			dp[i][j] += min([dp[i][k] + dp[k+1][j] for k in range(i, j)])

	# for d in dp : 
	# 	print(d)

	return dp[0][-1]

n = int(input())
matrix = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

print(getCount())

file.close()