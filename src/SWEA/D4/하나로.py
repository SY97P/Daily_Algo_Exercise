#1 10000
#2 180000
#3 1125000
#4 1953913
#5 27365366
#6 337122
#7 711268755613
#8 280157
#9 521568761
#10 34
#11 375890356686
#12 68427157
#13 21404
#14 16620885
#15 4776395492
#16 54860981981
#17 24236206202
#18 132410
#19 12876964085
#20 7016649393

file = open("./SWEA/D4/하나로.txt", "r")

input = file.readline

from collections import defaultdict
import heapq

t = int(input())

def getTax(dist) : 
	return rate * (dist ** 2)

def getCandi(node) : 
	global n
	
	result = []
	
	curr_x, curr_y = coor[node]

	for i in range(n) : 
		if not visited[i] : 
			next_x, next_y = coor[i]
			dist = (((curr_x - next_x) ** 2) + ((curr_y - next_y) ** 2)) ** (1/2)
			result.append((dist, i))

	return result

def prim(node) : 
	visited[node] = True

	candi = getCandi(node)
	heapq.heapify(candi)

	total_tax = 0

	while candi : 
		dist, next = heapq.heappop(candi)

		if not visited[next] : 
			visited[next] = True
			total_tax += getTax(dist)

			temp = getCandi(next)
			for i in range(len(temp)) : 
				heapq.heappush(candi, temp[i])
				
	return total_tax

for tc in range(1, t + 1) : 
	n = int(input())
	coor_x = list(map(int, input().split()))
	coor_y = list(map(int, input().split()))
	rate = float(input())

	# coor = [(node, x, y)]
	coor = []
	for i in range(n) : 
		coor.append((coor_x[i], coor_y[i]))

	visited = [False for _ in range(n)]

	print("#%d %d" % (tc, round(prim(0))))

file.close()