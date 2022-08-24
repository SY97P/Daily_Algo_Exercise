file = open("./이진탐색/K번째수tc.txt", "r")

def lower_count(mid) :
	result = 0

	for v in range(1, n + 1) :
		result += min(mid//v, n)
					
	return result

def bin(n, k) : 
	answer = 0
	left, right = 1, n ** 2
	while left <= right : 
		mid = (left + right) // 2

		count = lower_count(mid)

		print("right : ", right, "left : ", left, "mid : ", mid, "count : ", count)
		
		if count < k :
			left = mid + 1
		elif count >= k:
			answer = mid
			right = mid - 1
	return answer

for tc in range(12) : 
	n = int(file.readline())
	k = int(file.readline())
	answer = int(file.readline())
	file.readline()

	print(n, k, answer)

	print(bin(n, k))

	print()

file.close()

# 백준 제출용
# def lower_count(mid) :
# 	result = 0

# 	for v in range(1, n + 1) :
# 		result += min(mid//v, n)
					
# 	return result

# def bin(n, k) : 
# 	answer = 0
# 	left, right = 1, k
# 	while left <= right : 
# 		mid = (left + right) // 2

# 		count = lower_count(mid)

# 		# print("right : ", right, "left : ", left, "mid : ", mid, "count : ", count)
		
# 		if count < k :
# 			left = mid + 1
# 		elif count >= k:
# 			answer = mid
# 			right = mid - 1
# 	return answer

# n = int(file.readline())
# k = int(file.readline())

# print(bin(n, k))
