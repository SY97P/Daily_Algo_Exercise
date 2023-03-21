file = open("./이진탐색/용액tc.txt", "r")

for tc in range(2) :
	n = int(file.readline())
	solutions = list(map(int, file.readline().split()))
	answer = list(map(int, file.readline().split()))
	file.readline()

	print(n, answer)
	print(solutions)


	left, right = 0, n-1
	result = 2 * 10 ** 9
	lst = (left, right)
	while left < right :
		sol = solutions[left] + solutions[right]

		if abs(sol) < result :
			result = abs(sol)
			lst = (left, right)

		print(left, right, sol, result)

		if sol < 0 :
			left += 1
		elif sol > 0 :
			right -= 1
		else :
			break

	print(result, lst[0], lst[1], solutions[lst[0]], solutions[lst[1]])

	print()

file.close()


# 백준 제출용
# import sys

# file = sys.stdin

# n = int(file.readline())
# solutions = list(map(int, file.readline().split())

# left, right = 0, n-1
# result = 2 * 10 ** 9
# lst = (left, right)
# while left < right :
# 	sol = solutions[left] + solutions[right]

# 	if abs(sol) < result :
# 		result = abs(sol)
# 		lst = (left, right)


# 	if sol < 0 :
# 		left += 1
# 	elif sol > 0 :
# 		right -= 1
# 	else :
# 		break

# print(result, lst[0], lst[1], solutions[lst[0]], solutions[lst[1]])