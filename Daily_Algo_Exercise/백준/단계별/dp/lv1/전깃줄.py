# 6
# 3

file = open("./백준/dp/lv1/전깃줄.txt", "r")

input = file.readline

n = int(input())
wire = sorted([list(map(int, input().split())) for _ in range(n)])

dp = [1 for _ in range(n)]

for i in range(1, n) :
	for j in range(i) : 
		if wire[i][1] > wire[j][1] : 
			dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))

file.close()