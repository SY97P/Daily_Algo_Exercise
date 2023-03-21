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

# # 방법 2 ( O(n) )
# def eratosthenes2(num) :
# 	max = num + 1
# 	lim = int(num ** 0.5) + 1
	
# 	prime_set = set(range(5, num + 1, 6)) | set(range(7, num + 1, 6))

# 	if num > 2 : prime_set.add(3)
# 	if num > 1 : prime_set.add(2)

# 	for i in range(5, lim, 6) :
# 		if i in prime_set : 
# 			prime_set -= SET(i*i, max, i + 6) | SET(i*(i+2), max, i * 6)
# 		j = i + 2
# 		if j in prime_set : 
# 			prime_set -= SET(j * j, max, j + 6) | SET(j * (j + 4), max, j * 6)
	
# 	return prime_set


def main() : 
	num = 100
	print("1번 방법 ( O(n**2) ) : ", len(eratosthenes1(num)))
	# print("2번 방법 ( O( n  ) ) : ", len(eratosthenes2(num)))

if __name__ == '__main__' : 
	main()