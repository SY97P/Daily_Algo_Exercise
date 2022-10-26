#1 1	// Test Case 1의 정답
#2 2	// Test Case 2의 정답
#3 3	// Test Case 3의 정답

file = open("./SWEA/D4/자기방으로돌아가기.txt", "r")

input = file.readline

t = int(input())

for tc in range(1, t + 1) : 
	n = int(input())
	jammin = [tuple(map(int, input().split())) for _ in range(n)]

	jammin.sort()

	# print(jammin)

	time = 0

	while jammin : 
		time += 1
		curr = jammin.pop()[0]

		toge = []
		
		for i in range(len(jammin) - 1, -1, -1) :
			if curr >= jammin[i][1] : 
				toge.append(i)
				curr = jammin[i][0]

		for man in toge : 
			jammin.pop(man)

	print("#%d %d" % (tc, time))

file.close()