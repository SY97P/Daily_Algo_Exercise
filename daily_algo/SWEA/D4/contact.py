#1 17
#2 96
#3 49
#4 39
#5 49
#6 1
#7 28
#8 45
#9 59
#10 64

file = open("./SWEA/D4/contact.txt", "r")

input = file.readline

from collections import deque
from collections import defaultdict

def bfs(start) : 
	candi = []
	max_depth = 0
	visited = [False for _ in range(101)]

	q = deque([(0, start)])

	while q : 
		depth, node = q.popleft()

		max_depth = max(max_depth, depth)

		is_leaf = True
		for ad in adj[node] : 
			if not visited[ad] :
				is_leaf = False
				visited[ad] = True
				q.append((depth + 1, ad))
		if is_leaf :
			candi.append((depth, node))

	result = 0
	for depth, node in candi : 
		if max_depth <= depth : 
			result = max(result, node)

	return result
		

for tc in range(1, 11) : 
	length, start = map(int, input().split())
	data = list(map(int, input().split()))

	adj = defaultdict(set)

	for i in range(0, length, 2) : 
		adj[data[i]].add(data[i+1])

	print("#%d %d" % (tc, bfs(start)))

file.close()