file = open("./Daily_Algo_Exercise/이코테/기출/구현/치킨배달.txt")

input = file.readline

from itertools import combinations

n, m = map(int, input().split())

chicken = []
house = []

for i in range(n):
	line = list(map(int, input().split()))
	for j, l in enumerate(line):
		if l == 1:
			house.append((i, j))
		elif l == 2:
			chicken.append((i, j))

cases = list(combinations([i for i in range(len(chicken))], m))

answer = 1e9

for case in cases:
	survives = [chicken[x] for x in case]
	chicken_dist = 0
	for hi, hj in house:
		dist = 1e9
		for ci, cj in survives:
			dist = min(dist, abs(hi-ci) + abs(hj-cj))
		chicken_dist += dist
	answer = min(answer, chicken_dist)

print(answer)


file.close()