# 2

file = open("./백준/투포인터/부분합.txt", "r")

input = file.readline

n, s = map(int, input().split())
a = list(map(int, input().split()))

i, j = 0, 1

count = float('inf')

dp = [a[0]]
for k in range(1, n) : 
	dp.append(dp[k-1] + a[k])

# print(a)
# print(dp)

if dp[0] >= s : 
	count = 1

while True : 
	sumof = dp[j] - dp[i] + a[i]

	print(j, i, dp[j], dp[i], sumof, count)

	if sumof < s : 
		j += 1
	else : 
		count = min(count, j-i+1)
		i += 1

	if i == j : 
		if a[i] >= s : 
			count = min(count, 1)
		j += 1

	if j >= n : 
		break

print(count if count != float('inf') else 0)
	

file.close()