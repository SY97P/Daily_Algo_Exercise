file = open("./Daily_Algo_Exercise/이코테/기출/다이나믹/퇴사.txt")

input = file.readline 


n = int(input())
t, p = [], []
dp = [0] * (n+1)
for _ in range(n):
	a, b = map(int, input().split())
	t.append(a)
	p.append(b)

max_val = 0
for i in range(n-1, -1, -1):
	if i + t[i] <= n:
		dp[i] = max(max_val, dp[i+t[i]]) + p[i]
		max_val = dp[i]
	else:
		dp[i] = max_val

print(max_val)


file.close()