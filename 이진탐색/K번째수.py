file = open("./이진탐색/K번째수tc.txt", "r")

def lower_count(mid) :
	result = 0
	for v in range(1, min(n, mid+1)) :
		result += mid // v
		# print(result)
	return result

def bin(n, k) : 
	left, right = 1, n**2
	while left <= right : 
		mid = (left + right) // 2

		count = lower_count(mid)

		# print("mid : ", mid, "count : ", count)
		
		if count <= k :
			left = mid + 1
		elif count > k: 
			right = mid - 1
	return left

for tc in range(6) : 
	n = int(file.readline())
	k = int(file.readline())
	answer = int(file.readline())
	file.readline()

	print(n, k, answer)

	print(bin(n, k))

	print()

file.close()

# 백준 제출용
