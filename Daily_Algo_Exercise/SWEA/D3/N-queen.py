#1 1
#2 0

file = open("./SWEA/D3/N-queen.txt", "r")

input = file.readline

from collections import deque

t = int(input())

def bfs(n) :
	q = deque([[]])
	
	count = 0

	while q : 
		curr = q.popleft()

		# print(curr)

		if len(curr) == n : 
			count += 1
			# print("count aug : ", count)
			continue

		for location in range(n) :
			if not curr : 
				q.append([location])
				continue

			proper = True
			for j, c in enumerate(curr) : 
				if location == c or abs(location - c) == len(curr) - j : 
					proper = False
			if proper : 
				q.append(curr + [location])
				

	return count
	
	
for tc in range(1, t + 1) : 
	n = int(input())
	print(f"#{tc} {bfs(n)}")

file.close()