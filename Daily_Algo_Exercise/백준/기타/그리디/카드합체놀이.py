import heapq

file = open("./그리디/카드합체놀이tc.txt", "r")

for _ in range(2) : 
	n, m = map(int, file.readline().split())
	cards = list(map(int, file.readline().split()))
	answer = int(file.readline().strip("\n"))
	file.readline()

	print(n, m, cards, answer)

	heapq.heapify(cards)

	for i in range(m) :
		# print(i+1, "번째 시도")
		a, b = heapq.heappop(cards), heapq.heappop(cards)
		# print(a, b)
		heapq.heappush(cards, a + b)
		heapq.heappush(cards, a + b)

	print(sum(cards))

file.close()


# 백준 제출용
# import heapq

# n, m = map(int, input().split())
# cards = list(map(int, input().split()))

# heapq.heapify(cards)

# for _ in range(m) : 
# 	a, b = heapq.heappop(cards), heapq.heappop(cards)
# 	heapq.heappush(cards, a + b)
# 	heapq.heappush(cards, a + b)
# print(sum(cards))