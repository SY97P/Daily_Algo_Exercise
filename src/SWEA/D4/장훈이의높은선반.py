#1 1
#2 4
#3 27
#4 11
#5 42
#6 32
#7 2
#8 3
#9 25
#10 0

file = open("./SWEA/D4/장훈이의높은선반.txt", "r")

input = file.readline

t = int(input())

def dfs(index, height) : 
	global min_h, n, b

	if b <= height : 
		min_h = min(min_h, height)
		return

	for i in range(index + 1, n) :
		dfs(i, height + heights[i])

for tc in range(1, t + 1) : 
	n, b = map(int, input().split())
	heights = list(map(int, input().split()))

	min_h = float('inf')

	for i in range(n) : 
		dfs(i, heights[i])

	print("#%d %d" %(tc, min_h - b))

file.close()