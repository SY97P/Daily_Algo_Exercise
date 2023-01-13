
file = open("./백준/dp/역추적/경찰차.txt", "r")

input = file.readline

def trace() : 
	p1 = 0
	i, j = 0, 0
	k = 0
	while k < w :
		value = dp[i][j]
		k += 1
		if value - dist(True, p1, k-1) == dp[k][j] :
			print(1)
			i = k
			p1 = i
		else : 
			print(2)
			j = k
			

def dist(is_police1, pol, num) : 
	if pol == 0 : 
		if is_police1 : 
			return (case[num][0]-1) + (case[num][1]-1)
		else : 
			return (n-case[num][0]) + (n-case[num][1])
	else : 
		pol -= 1
		return abs(case[num][0] - case[pol][0]) + abs(case[num][1] - case[pol][1])
		

def solve(num, p1, p2) :
	if num > w :
		return 0

	if dp[p1][p2] != float('inf') : 
		return dp[p1][p2]

	dp[p1][p2] = min(
		dp[p1][p2],
		dist(True, p1, num-1) + solve(num+1, num, p2),
		dist(False, p2, num-1) + solve(num+1, p1, num)
	)

	return dp[p1][p2]
	
	

n = int(input())
w = int(input())

case = [tuple(map(int, input().split())) for _ in range(w)]

dp = [[float('inf') for _ in range(w+1)] for _ in range(w+1)]

solve(1, 0, 0)

print(dp[0][0])

for i in range(w+1) : 
	dp[-1][i] = 0
	dp[i][-1] = 0

# for d in dp : 
# 	print(d)

trace()

file.close()