# 300
# 826

file = open("./Daily_Algo_Exercise/백준/문제집/그리디/파일합치기3.txt")

input = file.readline

import heapq

t = int(input())
for tc in range(t):
	n = int(input())
	size = list(map(int, input().split()))
	heapq.heapify(size)

	result = 0
	while len(size) > 1:
		a, b = heapq.heappop(size), heapq.heappop(size)
		result += a + b
		heapq.heappush(size, a + b)

	print(result)
	

file.close()