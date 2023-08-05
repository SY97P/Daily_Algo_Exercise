file = open("./그리디/수묶기retc.txt", "r")

from collections import deque

for tc in range(13) : 
	n = int(file.readline())
	arr = [int(file.readline()) for _ in range(n)]
	answer = int(file.readline())
	file.readline()

	arr.sort(reverse = True)
	arr = deque(arr)

	print(n, answer)
	print(arr)

	result = 0
	convert = True
	while arr : 
		# 첫 값이 음수면 최소힙으로 전환
		if convert and arr[0] < 0 :
			convert = False
			arr = list(arr)
			arr.sort()
			arr = deque(arr)
			continue

		x = arr.popleft()

		# print(x, arr)

		if arr and x + arr[0] <= x * arr[0] :
			result += x * arr.popleft()
		else : 
			result += x

	print(result)
	print()


file.close()

# 백준 제출용
# import sys
# from collections import deque

# file = sys.stdin

# n = int(file.readline())
# arr = [int(file.readline()) for _ in range(n)]

# arr.sort(reverse = True)
# arr = deque(arr)

# result = 0
# convert = True
# while arr : 
# 	# 첫 값이 음수면 최소힙으로 전환
# 	if convert and arr[0] < 0 :
# 		convert = False
# 		arr = list(arr)
# 		arr.sort()
# 		arr = deque(arr)
# 		continue

# 	x = arr.popleft()

# 	if arr and x + arr[0] <= x * arr[0] :
# 		result += x * arr.popleft()
# 	else : 
# 		result += x

# print(result)
