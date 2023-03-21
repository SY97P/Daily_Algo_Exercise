#1 12
#2 10
#3 31
#4 11
#5 1
#6 43
#7 2
#8 11
#9 34
#10 8

file = open("./SWEA/D3/회문1.txt", "r")

input = file.readline

def isPalin(st, n) : 
	bound = n//2 if n % 2 == 0 else n//2 + 1
	for i in range(bound) : 
		if st[i] != st[-i-1] :
			return False
	return True

for tc in range(1, 11) : 
	n = int(input())
	matrix = [list(input().strip()) for _ in range(8)]

	# if tc != 3: 
	# 	continue

	# print(n, len(matrix), len(matrix[0]))

	count = 0

	for i in range(8) : 
		for j in range(8 - n + 1) :
			if isPalin(matrix[i][j:j+n], n) :
				count += 1
			# print("가로 : ", matrix[i][j:j+n], isPalin(matrix[i][j:j+n], n))
			temp = []
			for k in range(n) : 
				temp.append(matrix[j+k][i])
			# print("세로 : ", temp, isPalin(temp, n))
			if isPalin(temp, n) : 
				count += 1
		# print()

	print("#%d %d" % (tc, count))
	
file.close()