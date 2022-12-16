#1 45

file = open("./SWEA/D3/조합.txt", "r")

input = file.readline

import math

t = int(input())

# 2^5 = 2^2 * 2^2 * 2^1
# 2^4 = 2^2 * 2^2
def pow(a, b) : 
	global p 
	
	if b == 0 : 
		return 1
	sub = pow(a, b//2)
	result = (sub ** 2) % p

	if b % 2 == 0 : 
		return result
	else : 
		return (result * a) % p

for tc in range(1, t + 1) : 
	n, r = map(int, input().split())

	p = 1234567891

	result = math.factorial(n) * pow(math.factorial(r) * math.factorial(n-r) % p , p - 2) % p

	print("#%d %d" %(tc, result))

file.close()