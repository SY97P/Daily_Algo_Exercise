file = open("./SWEA/D5/이상한피라미드탐험.txt", "r")

input = file.readline

from collections import deque

t = int(input())

room = [[] for _ in range(150)]
num_loc = [tuple()]
visited = [[] for _ in range(150)]
d = [(0, 1), (1, 1), (1, 0), (0, -1)]

def setRoom() : 
	value = 1
	for i in range(150) :
		for j in range(i+1) :
			room[i].append(value)
			visited[i].append(0)
			num_loc.append((i, j))
			value += 1

def getDist(tc, q) : 
	global result, bi, bj
	
	while q : 
		i, j, dist = q.popleft()

		if i == bi and j == bj : 
			return dist
	
		for dx, dy in d : 
			di = i + dx
			dj = j + dy
			if 0 <= di < 150 and 0 <= dj < len(room[di]) and visited[di][dj] != tc : 
				visited[di][dj] = tc
				q.appendleft((di, dj, dist + 1))
	
setRoom()

for tc in range(1, t + 1) : 
	a, b = map(int, input().split())

	if a > b: 
		a, b = b, a

	ai, aj = num_loc[a]
	bi, bj = num_loc[b]

	# result = float('inf')

	visited[ai][aj] = tc
	result = getDist(tc, deque([(ai, aj, 0)]))

	print("#%d %d" % (tc, result))

file.close()