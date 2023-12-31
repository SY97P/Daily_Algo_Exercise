file = open("./이진탐색/두용액tc.txt", "r")

def bin(solutions, n) : 
	left, right = 0, n - 1
	value = 2 * (10 ** 9) + 1
	rtn = ()
	while left < right : 
		left_value = solutions[left]
		right_value = solutions[right]

		sum_value = left_value + right_value

		# 갱신
		if abs(sum_value) < value : 
			value = abs(sum_value)
			rtn = (left_value, right_value)

		# 조정
		if sum_value < 0 : # 음수면 더 크게 만들어야 함
			left += 1
		else : 
			right -= 1

	return rtn

for _ in range(20) : 
	n = int(file.readline())
	solutions = list(map(int, file.readline().split()))
	answer = list(map(int, file.readline().split()))
	file.readline()

	solutions.sort()

	print(n, answer)
	print(solutions)

	rtn = bin(solutions, n)
	rtn = list(rtn)
	rtn.sort()
	for r in rtn  :
		print(r, end = " ")
	print()
	print()

file.close()

# 백준 제출용
# import sys

# file = sys.stdin

# def bin(solutions, n) : 
# 	left, right = 0, n - 1
# 	value = 2 * (10 ** 9) + 1
# 	rtn = ()
# 	while left < right : 
# 		left_value = solutions[left]
# 		right_value = solutions[right]

# 		sum_value = left_value + right_value

# 		# 갱신
# 		if abs(sum_value) < value : 
# 			value = abs(sum_value)
# 			rtn = (left_value, right_value)

# 		# 조정
# 		if sum_value < 0 : # 음수면 더 크게 만들어야 함
# 			left += 1
# 		else : 
# 			right -= 1

# 	return rtn

# n = int(file.readline())
# solutions = list(map(int, file.readline().split()))

# solutions.sort()

# rtn = bin(solutions, n)
# rtn = list(rtn)
# rtn.sort()
# for r in rtn  :
# 	print(r, end = " ")
