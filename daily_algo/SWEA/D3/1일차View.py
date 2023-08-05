file = open("./SWEA/D3/1일차View.txt", "r")

input = file.readline

for tc in range(1, 11) : 
		
	n = int(input())
	buildings = list(map(int, input().split()))

	count = 0
	for i in range(2, n - 2) : 
		nearby = max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
		if nearby < buildings[i] : 
			count += buildings[i] - nearby

	print("#%d %d" % (tc, count))
				

file.close()