import math

m, n = map(int, input().split())

prime = [True] * (10**6+1)
prime[0], prime[1] = False, False

for i in range(2, int(math.sqrt(n))+1):
	if prime[i]:
		j = 2
		while i*j <= n:
			prime[i*j] = False
			j += 1

for i in range(m, n+1):
	if prime[i]:
		print(i)