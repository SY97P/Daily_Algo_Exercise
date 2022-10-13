#1 7
#2 11


file = open("./SWEA/D4/가능한시험점수.txt", "r")

input = file.readline

from collections import deque

t = int(input())

for tc in range(1, t + 1) : 
	n = int(input())
	scores = list(map(int, input().split()))
	
	scores.sort()
	
	length = sum(scores)

	visited = [0 for _ in range(length + 1)]
	visited[0] = 1

	scores = deque(scores) 
	
	while scores : 
		score = scores.popleft()

		for i in range(length, -1, -1) : 
			if visited[i] == 1 and i + score <= length : 
				visited[i + score] = 1


	print("#%d %d" % (tc, sum(visited)))

file.close()