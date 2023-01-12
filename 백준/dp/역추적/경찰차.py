# 9
# 2
# 2
# 1

file = open("./백준/dp/역추적/경찰차.txt", "r")

input = file.readline

def dist(police, loc1, loc2) : 
	if loc1 == 0 :
		if police == 1 : 
			return case[loc2][0] + case[loc2][1] - 2 
		elif police == 2: 
			return 2 * n - case[loc2][0] - case[loc2][1]
	return abs(case[loc1][0] - case[loc2][0]) + abs(case[loc1][1] - case[loc2][1])

def solve(case_num, loc1, loc2) :
	if case_num > w : 
		return 0

	if dp[loc1][loc2] != 0 : 
		return dp[loc1][loc2]

	dist1 = dist(1, loc1, case_num) + solve(case_num + 1, case_num, loc2)
	dist2 = dist(2, loc2, case_num) + solve(case_num + 1, loc1, case_num)

	dp[loc1][loc2] = min(dist1, dist2)

	return dp[loc1][loc2]

def trace() : 
	for i in range(w) : 
		if dp[i][0] - dist(1, i, i + 1) == dp[i+1][0] : 
			print(1)
		else : 
			print(2)

n = int(input())
w = int(input())

case = [tuple()] + [tuple(map(int, input().split())) for _ in range(w)]

dp = [[0 for _ in range(w + 1)] for _ in range(w + 1)]

solve(1, 0, 0)

print(dp[0][0])

trace()

# for d in dp : 
# 	print(d)

file.close()