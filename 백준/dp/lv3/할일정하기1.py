# 12
# 6

file = open("./백준/dp/lv3/할일정하기1.txt", "r")

input = file.readline

def countOccupied(x) : 
	count = 0
	for i in range(n) :
		if not x & (1 << i) : 
			count += 1
	return count

def solve() : 
	for i in range(1 << n) : 
		k = countOccupied(i)
		for j in range(n) : 
			if i & (1 << j) == 0 and dp[i | (1<<j)] > dp[i] + d[k-1][j] : 
				dp[i | (1<<j)] = dp[i] + d[k-1][j]

	# print(dp)
	return dp[-1]
		

n = int(input())

d = [list(map(int, input().split())) for _ in range(n)]

dp = [10 ** 6 for _ in range(1 << n)]
dp[0] = 0

print(solve())

file.close()