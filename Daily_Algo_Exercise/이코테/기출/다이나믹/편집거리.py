a = "cat"
b = "cut"

a = "sunday"
b = "saturday"

a = list(input().strip())
b = list(input().strip())

n, m = len(a), len(b)

dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
	dp[i][0] = i
for i in range(1, m+1):
	dp[0][i] = i

for i in range(n):
	for j in range(m):
		if a[i] == b[j]:
			dp[i+1][j+1] = dp[i][j]
		else:
			dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1

print(dp[-1][-1])