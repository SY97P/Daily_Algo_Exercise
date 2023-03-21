#1 2
#2 6
#3 6
#4 0
#5 14
#6 2
#7 45
#8 0
#9 98
#10 7

file = open("./SWEA/D2/어디에단어가들어갈수있을까.txt", "r")

input = file.readline

t = int(input())

for tc in range(1, t + 1) : 
	n, k = map(int, input().split())
	matrix = [list(map(int, input().split())) for _ in range(n)]

	count = 0 

	# if tc != 1: 
	# 	continue

	
	for i in range(n) : 
		# horizontal
		if sum(matrix[i]) >= k :
			temp = 0
			for j in range(n) : 
				if matrix[i][j] == 1 : 
					temp += 1
				else: 
					if temp == k :
						count += 1
					temp = 0
			if temp == k : 
				count += 1

		# vertical
		if sum([matrix[j][i] for j in range(n)]) >= k : 
			temp = 0
			for j in range(n) : 
				if matrix[j][i] == 1 : 
					temp += 1
				else :
					if temp == k : 
						count += 1
					temp = 0
			if temp == k :
				count += 1

	print("#%d %d" %(tc, count))

file.close()