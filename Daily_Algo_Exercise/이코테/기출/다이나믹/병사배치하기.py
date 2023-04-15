n = int(input())
array = list(map(int, input().split()))

# n = 7
# array = [15, 11, 4, 8, 5, 2, 4]

array.reverse()
array = [0] + array

dp = [0] * (n+1)

for i in range(1, n+1):
	max_val = -1
	for j in range(i):
		if array[j] < array[i]:
			max_val = max(max_val, dp[j])
	dp[i] = max_val + 1

print(n - max(dp))