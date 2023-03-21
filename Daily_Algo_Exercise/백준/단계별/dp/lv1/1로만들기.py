# 2  -> 1
# 10 -> 3
# 572 -> 10
# 40 -> 5
# 642 -> 10

def debug() :
	temp = n
	count = 0
	while temp > 1 :
		count += 1
		print("count : ", count, " n : ", temp, " oper : ", dp[temp])
		temp_lst = [float('inf'), float('inf'), float('inf')]
		if temp % 3 == 0 : 
			temp_lst[0] = dp[temp//3]
		if temp % 2 == 0 : 
			temp_lst[1] = dp[temp//2]
		temp_lst[2] = dp[temp - 1]
		value = 0
		for i in range(3) : 
			if min(temp_lst) == temp_lst[i] : 
				value = i
				break
		if value == 0 : 
			temp //= 3
		elif value == 1: 
			temp //= 2
		else : 
			temp -= 1
	

n = 16
n = int(input())

dp = [0, 0, 1, 1]

for i in range(4, n + 1) : 
	temp = []
	if i % 3 == 0 : 
		temp.append(dp[i//3])
	if i % 2 == 0 : 
		temp.append(dp[i//2]) 
	temp.append(dp[i-1])
	dp.append(1 + min(temp))

debug()

print(dp[n])