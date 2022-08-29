file = open("./백준_그리디/보석도둑retc.txt", "r")

import heapq

for _ in range(6) : 
	n, k = map(int, file.readline().split())
	jams = [list(map(int, file.readline().split())) for _ in range(n)]
	bags = [int(file.readline()) for _ in range(k)]
	answer = int(file.readline())
	file.readline()

	jams.sort()
	bags.sort()

	print(n, k, answer)
	print(jams)
	print(bags)

	temp = []
	result = 0
	for bag in bags :
		while jams and jams[0][0] <= bag :
			heapq.heappush(temp, -1 * heapq.heappop(jams)[1])
		print(temp)
		if temp : 
			result -= heapq.heappop(temp)

	print(result)
	print()

file.close()