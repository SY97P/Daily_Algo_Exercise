file = open("./이진탐색/가장긴증가하는부분수열2tc.txt", "r")

import bisect

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
			index = bisect.bisect(lis, nl)
			lis[index] = nl

	print(lis)
	print(len(lis))
	print()


file.close()

# 백준 제출용
# import sys
# import bisect

# file = sys.stdin

# n = int(file.readline())
# nlist = list(map(int, file.readline().split()))

# lis = [nlist[0]]
# for nl in nlist : 
# 	if lis[-1] < nl : 
# 		lis.append(nl)
# 	elif lis[-1] > nl : 
# 		index = bisect.bisect_left(lis, nl)
# 		lis[index] = nl

# print(len(lis))
	