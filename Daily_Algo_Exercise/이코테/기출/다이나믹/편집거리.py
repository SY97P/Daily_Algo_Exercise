a = input().strip()
b = input().strip()

n, m = len(a), len(b)

dp = [[0] * (m) for _ in range(n)]

if a[0] != b[0]:
	dp[0][0] = 1
for i in range(1,m):
	if a[0] != b[i]:
		dp[0][i] = dp[0][i-1] + 1
for i in range(1, n):
	if a[i] != b[0]:
		dp[i][0] = dp[i-1][0] + 1

for i in range(1, n):
	for j in range(1, m):
		if a[i] == b[j]:
			dp[i][j] = dp[i-1][j-1]
		else:
			dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

print(dp[-1][-1])
		