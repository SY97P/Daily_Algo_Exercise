# 4
# 10 20 30 50

file = open("./백준/dp/역추적/가장긴증가하는부분수열4.txt", "r")

input = file.readline

n = int(input())
a = [0] + list(map(int, input().split()))

dp = [0 for _ in range(n + 1)]
track = [[] for _ in range(n + 1)]
index = -1
maxLen = -1

for i in range(1, n + 1) : 
	for j in range(i-1, -1, -1) : 
		if a[j] < a[i] and dp[i] < dp[j] + 1: 
			dp[i] = dp[j] + 1
			track[i] = track[j] + [a[i]]
			if maxLen < dp[i] : 
				maxLen = dp[i]
				index = i
			
print(maxLen)
for tr in track[index] : 
	print(tr, end = " ")
print()


file.close()