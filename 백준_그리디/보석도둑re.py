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
	# print()

	temp = []
	heapq.heapify(temp)

	result = 0
	for bag in bags : 
		# 보석이 남아있고
		# 보석무게가 현재 가방 용량보다 작으면 다 힙에 넣어줌
		while jams and jams[0][0] <= bag : 
			# temp는 최대힙 (고가치 보석 넣어야 하니까)
			heapq.heappush(temp, -1 * heapq.heappop(jams)[1])
		if temp : 
			result += -1 * heapq.heappop(temp)

	print(result)
	print()

file.close()

# 백준 제출용
# import sys
# import heapq

# file = sys.stdin

# n, k = map(int, file.readline().split())
# jams = [list(map(int, file.readline().split())) for _ in range(n)]
# bags = [int(file.readline()) for _ in range(k)]

# jams.sort()
# bags.sort()

# temp = []
# heapq.heapify(temp)

# result = 0
# for bag in bags : 
# 	# 보석이 남아있고
# 	# 보석무게가 현재 가방 용량보다 작으면 다 힙에 넣어줌
# 	while jams and jams[0][0] <= bag : 
# 		# temp는 최대힙 (고가치 보석 넣어야 하니까)
# 		heapq.heappush(temp, -1 * heapq.heappop(jams)[1])
# 	if temp : 
# 		result += -1 * heapq.heappop(temp)

# print(result)
