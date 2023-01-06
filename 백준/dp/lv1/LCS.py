# 3
# 4

file = open("./백준/dp/lv1/LCS.txt", "r")

input = file.readline

def lcs_2d() : 
	dp = [[0 for _ in range(b_len + 1)] for _ in range(a_len + 1)]

	for i in range(1, a_len + 1) : 
		for j in range(1, b_len + 1) : 
			if a[i-1] == b[j-1] : 
				dp[i][j] = dp[i-1][j-1] + 1
			else : 
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])

	return dp[-1][-1]

# 이 방법으로는 풀 수 없었음
# def lcs_1d() : 
# 	dp = [0 for _ in range(b_len)]

# 	for i in range(a_len) :
# 		count = 0
# 		for j in range(b_len) : 
# 			if a[i] == b[j] : 
# 				dp[j] = count + 1
# 			elif count < dp[j] : 
# 				count = dp[j]

# 	return max(dp)

a = input().strip()
b = input().strip()

a_len = len(a)
b_len = len(b)
	 
print(lcs_2d())
# print(lcs_1d())

file.close()