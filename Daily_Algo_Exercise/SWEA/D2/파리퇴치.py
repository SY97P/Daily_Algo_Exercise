#1 49
#2 159
#3 428
#4 620
#5 479
#6 941
#7 171
#8 968
#9 209
#10 1242

file = open("./SWEA/D2/파리퇴치.txt", "r")

input = file.readline

t = int(input())

for tc in range(1, t + 1) :
	n, m = map(int, input().split())
	
	yard = []
	for _ in range(n) : 
		yard.append(list(map(int, input().split())))
	# print(yard)
	
	# if tc != 3 : 
	# 	continue

	# print(n, m)
		
	max_flies = 0
	d = [(i, j) for i in range(m) for j in range(m)]

	# for ya in yard : 
	# 	for y in ya :
	# 		if y < 10 : 
	# 			print(" ", end = "")
	# 		print(y, end = " ")
	# 	print()

	for i in range(n - m + 1) :
		for j in range(n - m + 1) : 
			max_flies = max(max_flies, sum([yard[i+dx][j+dy] for dx, dy in d]))
			# temp = [yard[i + dx][j + dy] for dx, dy in d]
			# print(i, j, " / ", sum(temp), temp)

	print("#%d %d" % (tc, max_flies))

file.close()