file = open("./이진탐색/공유기설치tc.txt", "r")

for tc in range(3) : 
	n, c = map(int, file.readline().split())
	houses = [int(file.readline()) for _ in range(n)]
	answer = int(file.readline())
	file.readline()

	houses.sort()

	print(n, c, " / ", answer)
	print(houses)

	left, right = 1, houses[-1] - houses[0]
	mid = 0
	while left <= right : 
		mid = (left + right) // 2

		curr = houses[0]
		count = 1

		for i in range(1, n) : 
			if houses[i] >= curr + mid :
				curr = houses[i]
				count += 1

		print("count : ", count)

		if count < c :
			right = mid - 1
		else : 
			left = mid + 1

	print(mid)

	print()

file.close()

# 백준 제출용
# from sys import stdin

# def bin() :
# 	left, right = 1, houses[-1] - houses[0]
# 	while left <= right : 
# 		mid = (left + right) // 2
	
# 		curr = houses[0]
# 		count = 1
	
# 		for i in range(1, n) : 
# 			if houses[i] >= curr + mid :
# 				curr = houses[i]
# 				count += 1
	
# 		# print("count : ", count)
	
# 		if count >= c : 
# 			global answer
# 			left = mid + 1
# 			answer = mid
# 		else : 
# 			right = mid - 1

# n, c = map(int, stdin.readline().split())
# houses = [int(stdin.readline()) for _ in range(n)]
# # answer = int(file.readline())
# # file.readline()

# houses.sort()

# # print(n, c, " / ", answer)
# # print(houses)

# answer = 0
# bin()
# print(answer)
