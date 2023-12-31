# 100

file = open("./Daily_Algo_Exercise/백준/문제집/그리디/카드정렬하기.txt")

input = file.readline

import heapq

n = int(input())

q = []
heapq.heapify(q)

for _ in range(n):
	heapq.heappush(q, int(input()))

result = 0

while len(q) > 1:
	a, b = heapq.heappop(q), heapq.heappop(q)
	result += a + b
	heapq.heappush(q, a + b)

print(result)


file.close()