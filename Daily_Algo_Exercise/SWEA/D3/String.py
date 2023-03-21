#1 4
#2 2
#3 19
#4 4
#5 6
#6 2
#7 5
#8 5
#9 8
#10 14

file = open("./SWEA/D3/String.txt", "r")

input = file.readline

for _ in range(10) : 
	tc = int(input())
	token = input().strip()
	line = input().strip()

	count = line.count(token)

	print("#%d %d" %(tc, count))

file.close()