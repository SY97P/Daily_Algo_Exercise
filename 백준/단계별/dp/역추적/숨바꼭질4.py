# 4
# 5 10 9 18 17
# 4
# 5 4 8 16 17

file = open("./백준/dp/역추적/숨바꼭질4.txt", "r")

input = file.readline

n, k = map(int, input().split())

def trace(k, value) :
	num = k
	val = value

	while num != n : 
		# print(num, val)
		if num+1 < bound and val - 1 == dp[num+1] : 
			temp.append(num+1)
			val -= 1
			num += 1
		elif num-1 >= 0 and val - 1 == dp[num-1] : 
			temp.append(num-1)
			val -= 1
			num -= 1
		elif num/2 == int(num/2) and val - 1 == dp[num//2] : 
			temp.append(num//2)
			val -= 1
			num //= 2
	

def solve() :
	for i in range(n) : 
		dp[i] = n-i
		if i != 0 and i*2 < bound : 
			dp[i*2] = dp[i] + 1 if i*2 != n else dp[n]
	# printDP(dp)
	for i in range(1, n) :
		item = n * (2**i)
		if item >= bound : 
			break
		dp[item] = i
	# printDP(dp)
	for i in range(n+1, bound) :
		origin = dp[i]
		if i+1 < bound : 
			dp[i] = min(dp[i], dp[i+1]+1)
		if i-1 >= 0 : 
			dp[i] = min(dp[i], dp[i-1]+1)
		if i/2 == int(i/2) : 
			dp[i] = min(dp[i], dp[i//2]+1)

		if origin != dp[i] : 
			if i+1 < bound :
				dp[i+1] = min(dp[i+1], dp[i]+1)
			if i-1 >= 0 : 
				dp[i-1] = min(dp[i-1], dp[i]+1)
			if i*2 < bound : 
				dp[i*2] = min(dp[i*2], dp[i]+1)

	# printDP(dp)

def printDP(dp) : 
	count = 0
	for d in dp : 
		print(d, end = " ")
		count += 1
		if count > 4 : 
			print()
			count = 0
	print()
	print()

# 역순으로 가는 방법은 x-1 뿐임. 이걸 생각못하네 박대가리쉑
if n >= k : 
	print(n - k)
	for i in range(n, k-1, -1) : 
		print(i, end = " ")
	print()
else : 
	bound = k + 2
	dp = [float('inf') for _ in range(bound)]
	dp[n] = 0

	solve()
	print(dp[k])

	temp = [k]
	trace(k, dp[k])
	print(*temp[::-1])

file.close()