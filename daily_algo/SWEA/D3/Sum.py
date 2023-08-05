#1 1712
#2 1743
#3 1713
#4 1682
#5 1715
#6 1730
#7 1703
#8 1714
#9 1727
#10 1731

file = open("./SWEA/D3/Sum.txt", "r")

input = file.readline

for _ in range(10) : 
	tc = int(input())
	matrix = [list(map(int, input().split())) for _ in range(100)]

	result = 0
	dia_sum1, dia_sum2 = 0, 0

	for i in range(100) :
		col_sum = 0
		for j in range(100) : 
			col_sum += matrix[j][i]
			if i + j == 99 : 
				dia_sum1 += matrix[i][j]
			if i == j : 
				dia_sum2 += matrix[i][j]
		result = max(result, sum(matrix[i]), col_sum)

	print("#%d %d" %(tc, max(result, dia_sum1, dia_sum2)))
		

file.close()