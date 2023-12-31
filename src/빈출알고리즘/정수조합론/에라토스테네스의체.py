# 방법 1 ( O(n**2) )
def eratosthenes1(num) : 
	prime_list = [False, False] + [True] * (num - 1)
	prime = []

	for i in range(2, num + 1) : 
		if prime_list[i] : 
			prime.append(i)
			for j in range(2 * i, num + 1, i) : 
				prime_list[j] = False

	return prime

def eratosthenes2(num):
	prime_list = [True] * (10 ** 6 + 1)
	prime_list[0], prime_list[1] = False, False
	prime = []

	for i in range(2, n**0.5 + 1):
		if prime_list[i]:
			j = 2
			while i * j <= n:
				prime_list[i*j] = False
				j += 1
	for i in range(2, len(prime_list)):
		if prime_list[i]:
			prime.append(i)
	return prime
	

def main() : 
	num = 100
	print("1번 방법 ( O(n**2) ) : ", len(eratosthenes1(num)))
	pirnt("2번 방법 ( O(nloglogn) : ", len(eratosthenes2(num)))

if __name__ == '__main__' : 
	main()