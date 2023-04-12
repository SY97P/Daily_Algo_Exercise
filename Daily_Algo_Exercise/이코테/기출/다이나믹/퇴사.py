file = open("./Daily_Algo_Exercise/이코테/기출/다이나믹/퇴사.txt")

input = file.readline 

n = int(input())
t, p = [], []
for _ in range(n):
	a, b = map(int, input().split())
	t.append(a)
	p.append(b)

dp = [0] * (n+1)

max_val = 0

for i in range(n-1, -1, -1):
	time = t[i] + i

	if time <= n:
		dp[i] = max(p[i] + dp[time], max_val)
		max_val = dp[i]
	else:
		dp[i] = max_val

print(dp)

print(max_val)
	

file.close()