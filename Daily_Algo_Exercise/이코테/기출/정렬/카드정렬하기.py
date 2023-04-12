import heapq

n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)

answer = 0
while len(cards) > 1:
	a, b = heapq.heappop(cards), heapq.heappop(cards)
	answer += a + b
	heapq.heappush(cards, a + b)

print(answer)