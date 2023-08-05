#1 24
#2 29
#3 27

file = open("./SWEA/D1/평균값구하기.txt", "r")

input = file.readline

t = int(input())

for tc in range(1, t + 1) : 
	print("#%d %d" % (tc, round(sum(map(int, input().split())) / 10)))
	

file.close()