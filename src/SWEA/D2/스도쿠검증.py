#1 1
#2 0
#3 1
#4 0
#5 0
#6 1
#7 0
#8 1
#9 1
#10 0

file = open("./SWEA/D2/스도쿠검증.txt", "r")

input = file.readline

t = int(input())

def rowCheck() : 
	result = True
	for i in range(9) :
		if sum(yard[i]) != 45 : 
			result = False
			break
	return result
	
def colCheck() : 
	result = True
	for i in range(9) : 
		if sum([yard[k][i] for k in range(9)]) != 45 : 
			result = False 
			break
	return result

def regionCheck() : 
	d = [(i, j) for i in range(3) for j in range(3)]
	result = True
	for i in range(0, 7, 3) : 
		for j in range(0, 7, 3) : 
			if sum([yard[i+dx][j+dy] for dx, dy in d]) != 45 :
				result = False
				break
	return result
				

for tc in range(1, t + 1) : 
	yard = [list(map(int, input().split())) for _ in range(9)]

	isProper = True

	print("#%d %d" % (tc, 1 if rowCheck() and colCheck() and regionCheck() else 0))
			

file.close()