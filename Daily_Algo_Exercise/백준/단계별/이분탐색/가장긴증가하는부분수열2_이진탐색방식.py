file = open("./이진탐색/가장긴증가하는부분수열2tc.txt", "r")

def bin(item) : 
	left, right = 0, len(lis) - 1
	while left <= right : 
		mid = (left + right) // 2

		if nl > lis[mid] :
			left = mid + 1
		else : 
			right = mid - 1
	print(left)
	return left

	
for tc in range(3) : 
	n = int(file.readline())
	nlist = list(map(int, file.readline().split()))
	answer = int(file.readline())
	file.readline()

	print(n, answer)
	print(nlist)


	lis = [nlist[0]]
	for nl in nlist : 
		if lis[-1] < nl : 
			lis.append(nl)
		elif lis[-1] > nl : 
			index = bin(nl)
			lis[index] = nl

	print(lis)
	print(len(lis))
	print()

file.close()

# 백준 제출용
# import sys

# def bin(item) : 
# 	left, right = 0, len(lis) - 1
# 	while left <= right : 
# 		mid = (left + right) // 2

# 		if nl > lis[mid] :
# 			left = mid + 1
# 		else : 
# 			right = mid - 1
# 	return left

# n = int(sys.stdin.readline())
# nlist = list(map(int, sys.stdin.readline().split()))

# lis = [nlist[0]]
# for nl in nlist : 
# 	if lis[-1] < nl : 
# 		lis.append(nl)
# 	elif lis[-1] > nl : 
# 		index = bin(nl)
# 		lis[index] = nl

# print(len(lis))