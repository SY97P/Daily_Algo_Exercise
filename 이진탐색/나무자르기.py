file = open("./이진탐색/나무자르기tc.txt", "r")

for _ in range(5) : 
	n, m = map(int, file.readline().split())
	trees = list(map(int, file.readline().split()))
	answer = int(file.readline())
	file.readline()
	
	print(n, m, answer)
	print(trees)

	result = 0
	left, right = 0, max(trees)
	while left <= right : 
		mid = (left + right) // 2

		sumof = 0
		for i in range(n) : 
			bulk = trees[i] - mid
			if bulk > 0 : 
				sumof += bulk

		if sumof < m : # 덜 잘랐으면
			right = mid - 1
		elif sumof > m : 
			left = mid + 1
		elif sumof == m or left > right :
			left = mid + 1
			break
	
	print(left - 1)
	print()

file.close()

# 백준 제출용
# import sys

# sys.setrecursionlimit(10 ** 9)

# n, m = map(int, input().split())
# trees = list(map(int, input().split()))

# left, right = 0, max(trees)
# while left <= right : 
# 	mid = (left + right) // 2

# 	sumof = 0
# 	for tree in trees : 
# 		if mid < tree : 
# 			sumof += tree - mid

# 	if sumof < m : # 덜 잘랐으면
# 		right = mid - 1
# 	elif sumof > m : 
# 		left = mid + 1
# 	elif sumof == m :
# 		left = mid + 1
# 		break

# print(left - 1)


