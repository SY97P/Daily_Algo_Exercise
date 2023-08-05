# 1
# 2 1
# 3
# 10 9 3 1

file = open("./백준/dp/역추적/1로만들기2.txt", "r")

input = file.readline

n = int(input())
# n = 10

dp = [float('inf') for _ in range(n + 1)]
dp[0:2] = [0, 0]

track = [[1] for _ in range(n + 1)]

for i in range(1, n) : 
	if i * 3 <= n :
		if dp[i*3] >= dp[i] + 1 :
			dp[i*3] = dp[i] + 1
			track[i*3] = track[i] + [i*3]
	if i * 2 <= n :
		if dp[i*2] >= dp[i] + 1 :
			dp[i*2] = dp[i] + 1
			track[i*2] = track[i] + [i*2]
	if i + 1 <= n : 
		if dp[i+1] >= dp[i] + 1 :
			dp[i+1] = dp[i] + 1
			track[i+1] = track[i] + [i+1]

# print(dp)
print(dp[-1])
for i in range(len(track[n]) - 1, -1, -1) : 
	print(track[n][i], end = " ")
print()

file.close()