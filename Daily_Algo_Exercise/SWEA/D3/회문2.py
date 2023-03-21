#1 18
#2 17
#3 17
#4 20
#5 18
#6 21
#7 18
#8 18
#9 17
#10 18

file = open("./SWEA/D3/회문2.txt", "r")

input = file.readline

def getPalinLen(st, l) : 
	bound = l // 2 if l % 2 == 0 else l // 2 + 1
	isPalin = True
	for i in range(bound) : 
		if st[i] != st[l-1-i] :
			isPalin = False
	return l if isPalin else -1

for _ in range(10) : 
	tc = int(input())
	matrix = [list(input()) for _ in range(100)]

	result = 0

	for i in range(100) : 
		# 가로 검사
		hasPalin = False
		for k in range(100, 0, -1) :
			for j in range(100 - k + 1) :
				palin = getPalinLen(matrix[i][j:j+k], k)
				result = max(result, palin)
				if palin != -1 : 
					hasPalin = True
					break
			if hasPalin :
				break

	temp = [[matrix[i][j] for i in range(100)] for j in range(100)]

	for i in range(100) : 
		# 가로 검사
		hasPalin = False
		for k in range(100, 0, -1) :
			for j in range(100 - k + 1) :
				palin = getPalinLen(temp[i][j:j+k], k)
				result = max(result, palin)
				if palin != -1 : 
					hasPalin = True
					break
			if hasPalin :
				break
			
	print("#%d %d" % (tc, result))

file.close()