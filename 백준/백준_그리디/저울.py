file = open("./백준_그리디/저울tc.txt", "r")

for tc in range(10) : 
	n = int(file.readline())
	weights = list(map(int, file.readline().split()))
	answer = int(file.readline())
	file.readline()

	weights.sort()

	print(n, answer)
	print(weights)

	sum = 0

	for weight in weights :
		# print(sum)
		if sum == 0 :
			if weight != 1 :
				break
			sum += weight
		else : 
			if sum + 1 < weight :
				break
			sum += weight

	print(sum + 1)
	print()

file.close()

# 백준 제출용
# import sys

# file = sys.stdin

# n = int(file.readline())
# weights = list(map(int, file.readline().split()))

# weights.sort()

# sum = 0

# for weight in weights :
# 	if sum == 0 :
# 		if weight != 1 :
# 			break
# 		sum += weight
# 	else : 
# 		if sum + 1 < weight :
# 			break
# 		sum += weight

# print(sum + 1)