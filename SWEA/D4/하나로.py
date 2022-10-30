#1 10000
#2 180000
#3 1125000
#4 1953913
#5 27365366
#6 337122
#7 711268755613
#8 280157
#9 521568761
#10 34
#11 375890356686
#12 68427157
#13 21404
#14 16620885
#15 4776395492
#16 54860981981
#17 24236206202
#18 132410
#19 12876964085
#20 7016649393

file = open("./SWEA/D4/하나로.txt", "r")

input = file.readline

t = int(input())

for tc in range(1, t + 1) : 
	n = int(input())
	coor_x = list(map(int, input().split()))
	coor_y = list(map(int, input().split()))
	tax = float(input())
	
	coor = []
	for i in range(n) :
		coor.append((coor_x[i], coor_y[i]))

	print(coor)
	print(tax)

file.close()