n, m = map(int, input().split())

dp = [float('inf')] * (m+1)

array = [int(input()) for _ in range(n)]

dp[0] = 0
for a in array:
	for i in range(a, m+1):
		dp[i] = min(dp[i], dp[i-a] + 1)

if dp[m] == float('inf'):
	print(-1)
else:
	print(dp[m])