a = "cat"
b = "cut"

a = list(input().strip())
b = list(input().strip())

n, m = len(a), len(b)

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(n):
	dp[i][0] = i
for i in range(m):
	dp[0][i] = i

for d in dp:
	print(d)