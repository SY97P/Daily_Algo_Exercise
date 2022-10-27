file = open("./백준_그리디/카드정렬하기retc.txt", "r")

import heapq

for tc in range(7) : 
	n = int(file.readline())
	cards = [int(file.readline()) for _ in range(n)]
	answer = int(file.readline())
	file.readline()

	print(n, answer)
	print(cards)

	heapq.heapify(cards)

	result = []
	
	while len(cards) > 1 : 
		x, y = heapq.heappop(cards), heapq.heappop(cards)
		result.append(x + y)
		heapq.heappush(cards, x + y)

	print(sum(result))
	print()

file.close()

# 백준 제출용
# import sys
# import heapq

# file = sys.stdin

# n = int(file.readline())
# cards = [int(file.readline()) for _ in range(n)]

# heapq.heapify(cards)

# result = []
	
# while len(cards) > 1 : 
# 	x, y = heapq.heappop(cards), heapq.heappop(cards)
# 	result.append(x + y)
# 	heapq.heappush(cards, x + y)

# print(sum(result))
