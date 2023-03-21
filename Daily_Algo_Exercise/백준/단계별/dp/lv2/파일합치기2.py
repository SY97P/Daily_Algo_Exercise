file = open("./백준/dp/lv2/파일합치기.txt", "r")

input = file.readline

t = int(input())

for tc in range(1, t + 1) : 

	n = int(input())
	files = list(map(int, input().split()))

	# if tc != 1 :
	# 	continue

	dp = [[0 for _ in range(n)] for _ in range(n)]

	for i in range(n - 1) : 
		dp[i][i+1] = files[i] + files[i+1]
		for j in range(i + 2, n) : 
			dp[i][j] = dp[i][j-1] + files[j]

	# j - i = d (1, 2, 3)
	for d in range(2, n) : 
		for i in range(n-d) :
			j = d + i
			dp[i][j] += min([dp[i][k] + dp[k+1][j] for k in range(i, j)])

	# for d in dp : 
	# 	print(d)

	print(dp[0][-1])

file.close()