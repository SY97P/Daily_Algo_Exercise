file = open("./Daily_Algo_Exercise/이코테/기출/구현/치킨배달.txt")

input = file.readline

from itertools import combinations

n, m = map(int, input().split())

house = []
chicken = []

for i in range(n):
	line = list(map(int, input().split()))
	for j in range(n):
		if line[j] == 1:
			house.append((i, j))
		elif line[j] == 2:
			chicken.append((i, j))

answer = 1e9
for case in combinations([i for i in range(len(chicken))], m):
	chicken_dist = 0
	for home in house:
		dist = 1e9
		for x in case:
			chicken_house = chicken[x]
			dist = min(dist, abs(home[0]-chicken[x][0]) + abs(home[1]-chicken[x][1]))
		chicken_dist += dist
	answer = min(answer, chicken_dist)

print(answer)


file.close()