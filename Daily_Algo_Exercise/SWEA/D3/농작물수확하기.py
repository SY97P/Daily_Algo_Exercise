#1 23
#2 1190
#3 946
#4 112
#5 1886
#6 3000
#7 1032
#8 1330
#9 939
#10 2960
#11 547
#12 3016
#13 1712
#14 2049
#15 1294
#16 354
#17 1634
#18 1901
#19 2518
#20 1750
#21 2144
#22 940
#23 0
#24 1712
#25 1685
#26 559
#27 874
#28 75
#29 139
#30 3
#31 13
#32 331
#33 2646
#34 1531
#35 156
#36 1663
#37 934
#38 1725
#39 107
#40 2291
#41 84
#42 590
#43 31
#44 1351
#45 1364
#46 1187
#47 1059
#48 1771
#49 1228
#50 2065

file = open("./SWEA/D3/농작물수확하기.txt", "r")

input = file.readline

t = int(input())

def calTop(bound) :
	result = 0
	for i in range(bound) :
		temp = set()
		for j in range(i+1) :
			temp.update([bound + j, bound - j])
		# for t in temp : 
		# 	print(matrix[i][t], end = " ")
		# print()
		for t in temp : 
			result += matrix[i][t]
	return result

def calBot(bound) : 
	result = 0
	length = len(matrix)
	index = length - bound
	for i in range(length - 1, length - bound - 1, -1) :
		temp = set()
		for j in range(i - bound) :
			temp.update([bound + j, bound - j])
		# print(temp)
		# for t in temp : 
		# 	print(matrix[index][t] , end = " ")
		# print()
			
		for t in temp : 
			result += matrix[index][t]
			
		index += 1
	return result
		

for tc in range(1, t + 1) : 
	n = int(input())
	matrix = [list(map(int, list(input().strip()))) for _ in range(n)]

	# if tc != 4 : 
	# 	continue

	result = calTop(n//2) + sum(matrix[n//2]) + calBot(n//2)

	print("#%d %d" % (tc, result))

file.close()