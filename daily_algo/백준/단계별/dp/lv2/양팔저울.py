# Y N
# Y Y N
# Y


file = open("./백준/dp/lv2/양팔저울.txt", "r")

input = file.readline

def solve() : 
	for weight in babel :
		temp = set()
		for j in range(bound + 1) : 
			if dp[j] == 1 : 
				if weight + j <= bound : 
					temp.add(weight + j)
				if j < weight : 
					temp.add(weight - j)
				else : 
					temp.add(j - weight)
		for te in temp : 
			dp[te] = 1

m = int(input())
babel = list(map(int, input().split()))

n = int(input())
marble = list(map(int, input().split()))

bound = sum(babel)

# print(bound)

dp = [0 for _ in range(bound + 1)]
dp[0] = 1

solve()

for mar in marble : 
	if mar > bound or dp[mar] == 0 : 
		print("N", end = " ")
	else :
		print("Y", end = " ")


file.close()