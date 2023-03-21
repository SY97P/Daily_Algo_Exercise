# 0
# 1
# 3
# 2

file = open("./백준/투포인터/소수의연속합.txt", "r")

input = file.readline

def eratos(n) : 
	primes = [True for _ in range(n+1)]
	primes[0] = primes[1] = False

	for i in range(2, int(n**0.5+1)) : 
		if primes[i] : 
			for j in range(i+i, n+1, i) :
				primes[j] = False

	result = []
	for i in range(n+1) : 
		if primes[i] : 
			result.append(i)
	return result

# for _ in range(5) : 
n = int(input())

if n < 2 : 
	print(0)
else : 

	primes = eratos(n)
	
	dp = [primes[0]]
	for i in range(1, len(primes)) : 
		dp.append(dp[i-1] + primes[i])
	# print(dp)
	
	i = j = 0
	
	count = 0
	length = len(primes)
	
	while i < length and j < length : 
		sumof = dp[j] - dp[i] + primes[i]
	
		# print(i, j, sumof, count)
	
		if sumof < n : 
			j += 1
		elif sumof > n : 
			i += 1
		else : 
			count += 1
			i += 1
	
	print(count)
			
	
file.close()