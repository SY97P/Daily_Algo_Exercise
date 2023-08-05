#1 1
#2 1
#3 1
#4 0
#5 1
#6 1
#7 0
#8 0
#9 0
#10 0

file = open("./SWEA/D4/길찾기.txt", "r")

input = file.readline

from collections import deque

def bfs() : 
	visited = {0}
	q = deque([(0, visited)])

	while q : 
		node, visi = q.popleft()

		if node == 99 : 
			return 1

		for i in range(2) : 
			# 현재 노드에서 갈 수 있는 곳이 경로상에 없으면
			# 이쪽으로 더 갈 수 있다. 
			temp = visi
			if tree[i][node] not in visi : 
				temp.add(tree[i][node])
				q.append((tree[i][node], temp))

	return 0
	

for _ in range(10) : 
	tc, n = map(int, input().split())
	temp = list(map(int, input().split()))
	tree = [[-1 for _ in range(100)] for _ in range(2)]

	for i in range(0, len(temp), 2) : 
		s, e = temp[i], temp[i+1]
		if tree[0][s] != -1 : 
			tree[1][s] = e
		else : 
			tree[0][s] = e

	print("#%d %d" % (tc, bfs()))

file.close()