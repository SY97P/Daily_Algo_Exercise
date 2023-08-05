#1 1
#2 2

file = open("./SWEA/D3/원재의메모리복구하기.txt", "r")

input = file.readline

t = int(input())

for tc in range(1, t + 1) : 
	origin = list(input().strip())
	n = len(origin)
	init = ['0' for _ in range(n)]

	count = 0

	for i in range(n) : 
		if origin[i] != init[i] : 
			count += 1
			for k in range(i, n) : 
				init[k] = origin[i]	

	print("#%d %d" % (tc, count))

file.close()