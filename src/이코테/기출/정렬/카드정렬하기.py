import heapq

n = int(input())
q = [int(input()) for _ in range(n)]
heapq.heapify(q)

answer = 0
while len(q) > 1:
	a, b = heapq.heappop(q), heapq.heappop(q)
	answer += a + b
	heapq.heappush(q, a+b)

print(answer)