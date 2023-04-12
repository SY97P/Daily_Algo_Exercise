n = int(input())
array = list(map(int, input().split())) + [0]
array.reverse()

dp = [0] * (n+1)

for i in range(1, n+1):
	max_val = 0
	for j in range(i-1, -1, -1):
		if array[j] < array[i]:
			max_val = max(max_val, dp[j]+1)
	dp[i] = max_val

# print(dp)
print(n - max(dp))