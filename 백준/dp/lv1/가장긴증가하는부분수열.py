# 4

file = open("./백준/dp/lv1/가장긴증가하는부분수열.txt", "r")

input = file.readline

n = int(input())

num = [0] + list(map(int, input().split()))

dp = [0, 1] + [0 for _ in range(n - 1)]

for i in range(1, n + 1) : 
	for j in range(i-1, -1, -1) :
		if num[i] > num[j] : 
			dp[i] = max(dp[i], dp[j] + 1)

# print(dp)

print(max(dp))

file.close()